
COCO_DATA=/home/ubuntu/s3/data-20170127/Microsoft_COCO

VSE_DATA=data/coco
MODEL_DIR=data/models
RESULT_DIR=data/results

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
FEATS = depnet-vgg-myconceptsv3-fc7 depnet-vgg-mydepsv4-fc7 depnet-vgg-mydepsprepv4-fc7 depnet-vgg-mypasv4-fc7 depnet-vgg-mypasprepv4-fc7 \
	depnet-vgg-myconceptsv3-mydepsv4-fc7 depnet-vgg-myconceptsv3-mydepsprepv4-fc7 depnet-vgg-myconceptsv3-mypasv4-fc7 depnet-vgg-myconceptsv3-mypasprepv4-fc7


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

concat_feature: $(patsubst %,$(VSE_DATA)/depnet-vgg-myconceptsv3-mydepsv4-fc7_%_ims.npy,$(SETS)) \
	$(patsubst %,$(VSE_DATA)/depnet-vgg-myconceptsv3-mydepsprepv4-fc7_%_ims.npy,$(SETS)) \
	$(patsubst %,$(VSE_DATA)/depnet-vgg-myconceptsv3-mypasv4-fc7_%_ims.npy,$(SETS)) \
	$(patsubst %,$(VSE_DATA)/depnet-vgg-myconceptsv3-mypasprepv4-fc7_%_ims.npy,$(SETS))

$(VSE_DATA)/depnet-vgg-myconceptsv3-mydepsv4-fc7_%_ims.npy: \
	$(VSE_DATA)/depnet-vgg-myconceptsv3-fc7_%_ims.npy \
	$(VSE_DATA)/depnet-vgg-mydepsv4-fc7_%_ims.npy
	python concat_feature.py $^ $@
$(VSE_DATA)/depnet-vgg-myconceptsv3-mydepsprepv4-fc7_%_ims.npy: \
	$(VSE_DATA)/depnet-vgg-myconceptsv3-fc7_%_ims.npy \
	$(VSE_DATA)/depnet-vgg-mydepsprepv4-fc7_%_ims.npy
	python concat_feature.py $^ $@
$(VSE_DATA)/depnet-vgg-myconceptsv3-mypasv4-fc7_%_ims.npy: \
	$(VSE_DATA)/depnet-vgg-myconceptsv3-fc7_%_ims.npy \
	$(VSE_DATA)/depnet-vgg-mypasv4-fc7_%_ims.npy
	python concat_feature.py $^ $@
$(VSE_DATA)/depnet-vgg-myconceptsv3-mypasprepv4-fc7_%_ims.npy: \
	$(VSE_DATA)/depnet-vgg-myconceptsv3-fc7_%_ims.npy \
	$(VSE_DATA)/depnet-vgg-mypasprepv4-fc7_%_ims.npy
	python concat_feature.py $^ $@


### Training

FEAT_DIM?=4096

train: $(patsubst %,$(MODEL_DIR)/%/coco.npz,$(FEATS))

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


### CONCEPT/DEP MATCHING 
MATCHING_FEATS = depnet-vgg-myconceptsv3-fc8 depnet-vgg-mydepsv4-fc8 depnet-vgg-mydepsprepv4-fc8 depnet-vgg-mypasv4-fc8 depnet-vgg-mypasprepv4-fc8

convert_gold: $(patsubst %,$(VSE_DATA)/%_test_labels.npy,$(MATCHING_FEATS))
$(VSE_DATA)/depnet-vgg-myconceptsv3-fc8_test_labels.npy: $(VSE_DATA)/dataset.json \
	$(COCO_DATA)/mscoco2014_val_image_depnet-vgg-myconceptsv3-fc8.h5 \
	$(COCO_DATA)/mscoco2014_val_captions_coarselemmas.jsonl
	python convert_gold.py $^ $@ --target_concept coarse_lemmas
$(VSE_DATA)/depnet-vgg-mydepsv4-fc8_test_labels.npy: $(VSE_DATA)/dataset.json \
	$(COCO_DATA)/mscoco2014_val_image_depnet-vgg-mydepsv4-fc8.h5 \
	$(COCO_DATA)/mscoco2014_val_captions_coarsedeps.jsonl
	python convert_gold.py $^ $@ --target_concept coarse_dependencies
$(VSE_DATA)/depnet-vgg-mydepsprepv4-fc8_test_labels.npy: $(VSE_DATA)/dataset.json \
	$(COCO_DATA)/mscoco2014_val_image_depnet-vgg-mydepsprepv4-fc8.h5 \
	$(COCO_DATA)/mscoco2014_val_captions_coarsedepsprep.jsonl
	python convert_gold.py $^ $@ --target_concept coarse_dependencies
$(VSE_DATA)/depnet-vgg-mypasv4-fc8_test_labels.npy: $(VSE_DATA)/dataset.json \
	$(COCO_DATA)/mscoco2014_val_image_depnet-vgg-mypasv4-fc8.h5 \
	$(COCO_DATA)/mscoco2014_val_captions_pas.jsonl
	python convert_gold.py $^ $@ --target_concept pas
$(VSE_DATA)/depnet-vgg-mypasprepv4-fc8_test_labels.npy: $(VSE_DATA)/dataset.json \
	$(COCO_DATA)/mscoco2014_val_image_depnet-vgg-mypasprepv4-fc8.h5 \
	$(COCO_DATA)/mscoco2014_val_captions_pasprep.jsonl
	python convert_gold.py $^ $@ --target_concept pas

convert_pred: $(patsubst %,$(VSE_DATA)/%_test_ims.npy,$(MATCHING_FEATS))

dep_matching: $(patsubst %,$(RESULT_DIR)/%_test_matching.json,$(MATCHING_FEATS)) 
$(RESULT_DIR)/%_test_matching.json: $(VSE_DATA)/%_test_ims.npy $(VSE_DATA)/%_test_labels.npy
	THEANO_FLAGS=device=gpu$(GID) python dep_matching.py --pred $(word 1,$^) --gold $(word 2,$^) --output_json $@ --topk 5000

CONCAT_FEATS = mydepsv4 mydepsprepv4 mypasv4 mypasprepv4
dep_matching_concat: $(patsubst %,$(RESULT_DIR)/depnet-vgg-myconceptsv3-%-fc8_test_matching.json,$(CONCAT_FEATS))
$(RESULT_DIR)/depnet-vgg-myconceptsv3-%-fc8_test_matching.json: \
	$(VSE_DATA)/depnet-vgg-myconceptsv3-fc8_test_ims.npy $(VSE_DATA)/depnet-vgg-%-fc8_test_ims.npy \
	$(VSE_DATA)/depnet-vgg-myconceptsv3-fc8_test_labels.npy $(VSE_DATA)/depnet-vgg-%-fc8_test_labels.npy
	THEANO_FLAGS=device=gpu$(GID) python dep_matching.py --pred $(word 1,$^) $(word 2,$^) \
		--gold $(word 3,$^) $(word 4,$^) --output_json $@ --topk 5000


