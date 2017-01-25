
COCO_DATA=/home/ubuntu/s3/data-20160817/Microsoft_COCO

VSE_DATA=data/coco
MODEL_DIR=data/models

GID?=0

### Download dataset splits, provided by Karpathy
$(VSE_DATA)/dataset.json:
	mkdir -p $(VSE_DATA)
	wget -P $(VSE_DATA) http://cs.stanford.edu/people/karpathy/deepimagesent/caption_datasets.zip 
	cd $(VSE_DATA); unzip caption_datasets.zip; mv dataset_coco.json dataset.json; rm caption_datasets.zip; rm dataset_*.json; cd -

### Convert caption format
SETS = train dev test
convert_caption: $(patsubst %,$(VSE_DATA)/coco_%_captions.txt,$(SETS))
$(VSE_DATA)/coco_%_captions.txt: $(VSE_DATA)/dataset.json 
	python convert_caption.py $^ $@ --split $*

### Convert feature format
FEATS = depnet-vgg-exdepsv4-fc7 #depnet-vgg-exconceptsv3-fc7 depnet-vgg-exconceptsv3exdepsv4-fc7
convert_feature: $(patsubst %,$(VSE_DATA)/%_train_ims.npy,$(FEATS)) \
	$(patsubst %,$(VSE_DATA)/%_dev_ims.npy,$(FEATS)) \
	$(patsubst %,$(VSE_DATA)/%_test_ims.npy,$(FEATS))

$(VSE_DATA)/%_train_ims.npy: $(VSE_DATA)/dataset.json \
	$(COCO_DATA)/mscoco2014_train_image_%.h5
	python convert_format.py $^ $@ --split train
$(VSE_DATA)/%_dev_ims.npy: $(VSE_DATA)/dataset.json \
	$(COCO_DATA)/mscoco2014_val_image_%.h5
	python convert_format.py $^ $@ --split dev
$(VSE_DATA)/%_test_ims.npy: $(VSE_DATA)/dataset.json \
	$(COCO_DATA)/mscoco2014_val_image_%.h5
	python convert_format.py $^ $@ --split test

### Training

FEAT_DIM?=4096

train: $(patsubst %,$(MODEL_DIR)/%/coco.npz,$(FEATS))

train_exconceptsv3: $(MODEL_DIR)/depnet-vgg-exconceptsv3-fc7/coco.npz
train_exdepsv4: $(MODEL_DIR)/depnet-vgg-exdepsv4-fc7/coco.npz
train_exconceptsv3exdepsv4: $(MODEL_DIR)/depnet-vgg-exconceptsv3exdepsv4-fc7/coco.npz

$(MODEL_DIR)/%/coco.npz: $(VSE_DATA)/%_train_ims.npy $(VSE_DATA)/%_dev_ims.npy $(VSE_DATA)/%_test_ims.npy \
	$(VSE_DATA)/coco_train_captions.txt $(VSE_DATA)/coco_dev_captions.txt $(VSE_DATA)/coco_test_captions.txt
	mkdir -p $(MODEL_DIR)/$*
	THEANO_FLAGS=device=gpu$(GID) python train.py coco $* $(FEAT_DIM) $@

### Testing

test: $(patsubst %,test_%,$(FEATS))
test_%: $(MODEL_DIR)/%/coco.npz \
	$(VSE_DATA)/%_test_ims.npy \
	$(VSE_DATA)/coco_test_captions.txt
	THEANO_FLAGS=device=gpu$(GID) python evaluation.py coco $* $< test

