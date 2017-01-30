# Image/Caption Retrieval Task

## How to run?

  * Edit Makefile, update `COCO_DATA` path
  * Edit `FEATS` to set feature types
  * `make train GID=1`
  * `make test GID=2`
  
## Results on MS COCO dataset (Image to text -- Text to image)

### Using Joint Embedding

| Method | aR@1 | aR@5 | aR@10 | aMedr | sR@1 | sR@5 | sR@10 | sMedr |
| ----- | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| vgg (fc7) | 43.4 | 75.7 | 85.8 | 2 | 31.0 | 66.7 | 79.9 | 3 
| exconceptsv3 (fc7) | 42.6 | 74.5 | 85.6 | 2 | 32.6 | 67.2 | 80.0 | 3 
| exdepsv4 (fc7) | 34.0 | 67.4 | 80.8 | 3 | 28.9 | 63.6 | 77.5 | 3 
| expasv4 (fc7) | 33.2 | 66.2 | 81.3 | 3 | 28.9 | 62.9 | 78.4 | 3
| expasprepv4 (fc7) | 33.7 | 69.6 | 81.5 | 3 | 28.4 | 64.0 | 78.2 | 3
| exconceptsv3exdepsv4 (fc7) | 35.5 | 69.8 | 81.6 | 2 | 29.5 | 64.6 | 78.9 | 3 
| exconceptsv3-exdepsv4 (concat) | 41.5 |  75.0 | 86.4 | 2 | 33.6 | 67.5 | 80.7 | 3
| exconceptsv3-expasv4 (concat) | 40.3 |  74.7 | 85.0 | 2 | 33.4 | 68.0 | 81.4 | 3
| exconceptsv3-expasprepv4 (concat) | 42.4 |  74.1 | 85.0 | 2 | 33.2 | 68.7 | 82.1 | 3
| | 
| myconceptsv3 (fc7) | 41.8 | 72.9 | 85.1 | 2 | 32.5 | 66.2 | 80.1 | 3 
| mydepsv4 (fc7) | 31.6 | 63.8 | 78.0 | 3 | 26.8 | 60.2 | 74.9 | 4 
| mypasv4 (fc7) | 35.4 | 67.8 |  78.8 | 3 | 28.3 | 62.1 | 76.5 | 3
| mypasprepv4 (fc7) | 32.8 | 68.1 | 79.6 | 3 | 27.7 | 62.4 | 77.3 | 3
| myconceptsv3-mydepsv4 (concat) | 38.9 |  72.9 | 83.3 | 2 | 32.4 | 66.9 | 80.5 |  3 
| myconceptsv3-mypasv4 (concat) |  41.6 | 73.9 | 84.7 | 2 | 33.8 | 67.3 | 80.6 | 3
| myconceptsv3-mypasprepv4 (concat) | 41.2 |  75.3 | 84.1 | 2 | 33.1 | 67.3 | 80.0 | 3

### Using Concept Matching
  * With feature normlization on image features

| Method | aR@1 | aR@5 | aR@10 | aMedr | sR@1 | sR@5 | sR@10 | sMedr |
| ----- | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| exconceptsv3 (fc8) | 11.2 | 29.3 | 43.5 | 14 | 18.3 | 44.9 | 59.6 | 7
| exdepsv4 (fc8) | 5.9 | 20.5 | 31.6 | 24 | 9.3 | 29.1 | 43.0 | 14
| expasv4 (fc8) | 7.2 | 21.9 | 34.1 | 25 | 8.9 | 28.3 | 42.9 | 14
| expasprepv4 (fc8) | 6.5 | 21.4 | 32.8 | 24 | 8.4 | 28.2 | 43.0 | 14
| exconceptsv3-exdepsv4 (fc8) | 9.4 | 27.6 | 40.5 | 16 | 16.7 | 43.8 | 59.8 | 7
| exconceptsv3-expasv4 (fc8) | 9.3 | 28.2 | 40.2 | 16 | 16.9 | 43.9 | 59.8 | 7
| exconceptsv3-expasprepv4 (fc8) | 9.8 | 29.0 | 41.1 | 15 | 16.8 | 44.1 | 60.1 | 7

  * Without feature normlization on image features

| Method | aR@1 | aR@5 | aR@10 | aMedr | sR@1 | sR@5 | sR@10 | sMedr |
| ----- | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| exconceptsv3 (fc8) | 11.2 | 29.3 | 43.5 | 14 | 15.4 | 40.6 | 55.8 | 8
| exdepsv4 (fc8) | 5.9 | 20.5 | 31.6 | 24 | 7.3 | 25.8 | 40.3 | 16
| expasv4 (fc8) | 7.2 | 21.9 | 34.1 | 25 | 7.1 | 25.6 | 39.2 | 17
| expasprepv4 (fc8) | 6.5 | 21.4 | 32.8 | 24 | 7.3 | 25.5 | 39.5 | 16
| exconceptsv3-exdepsv4 (fc8) | 9.8 | 30.7 | 42.2 | 15 | 14.0 | 39.8 | 55.4 | 9
| exconceptsv3-expasv4 (fc8) | 9.6 | 29.6 | 41.9 | 15 | 13.7 | 40.3 | 55.8 | 8
| exconceptsv3-expasprepv4 (fc8) | 10.0 | 30.2 | 42.9 | 14 | 14.0 | 40.1 | 55.6 | 8
