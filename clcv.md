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

## Results data-20170127

### Using Joint Embedding
#### VGG features

| Method                                   | aR@1 | aR@5 | aR@10 | aMedr | sR@1  | sR@5  | sR@10 | sMedr |
|------------------------------------------|------|------|-------|-------|-------|-------|-------|-------|
| depnet-vgg-myconceptsv3-fc7              | 40.8 | 74.4 | 85.3  | 2.0   | 33.14 | 68.26 | 80.94 | 3.0   |
| depnet-vgg-exconceptsv3-fc7              | 40.9 | 75.0 | 85.6  | 2.0   | 32.64 | 67.12 | 80.68 | 3.0   |
| depnet-vgg-mydepsv4-fc7                  | 35.6 | 67.2 | 77.9  | 3.0   | 27.62 | 62.1  | 76.48 | 3.0   |
| depnet-vgg-exdepsv4-fc7                  | 34.9 | 66.0 | 80.5  | 3.0   | 28.04 | 62.44 | 76.7  | 3.0   |
| depnet-vgg-mydepsprepv4-fc7              | 33.8 | 67.6 | 79.7  | 3.0   | 28.04 | 61.88 | 75.78 | 3.0   |
| depnet-vgg-exdepsprepv4-fc7              | 35.4 | 68.7 | 81.6  | 2.0   | 29.12 | 63.22 | 76.84 | 3.0   |
| depnet-vgg-mypasv4-fc7                   | 32.7 | 65.2 | 78.4  | 3.0   | 27.66 | 62.6  | 76.9  | 3.0   |
| depnet-vgg-expasv4-fc7                   | 35.1 | 68.1 | 80.1  | 3.0   | 29.06 | 63.28 | 77.56 | 3.0   |
| depnet-vgg-mypasprepv4-fc7               | 33.3 | 66.6 | 78.0  | 3.0   | 28.62 | 61.0  | 75.26 | 4.0   |
| depnet-vgg-expasprepv4-fc7               | 34.5 | 67.7 | 81.2  | 3.0   | 29.48 | 62.7  | 76.86 | 3.0   |
| depnet-vgg-myconceptsv3-mydepsv4-fc7     | 43.9 | 73.7 | 84.6  | 2.0   | 33.52 | 68.08 | 80.68 | 3.0   |
| depnet-vgg-exconceptsv3-exdepsv4-fc7     | 42.6 | 73.7 | 85.7  | 2.0   | 33.4  | 68.18 | 81.68 | 3.0   |
| depnet-vgg-myconceptsv3-mydepsprepv4-fc7 | 40.8 | 75.2 | 85.4  | 2.0   | 33.82 | 68.66 | 81.76 | 3.0   |
| depnet-vgg-exconceptsv3-exdepsprepv4-fc7 | 42.1 | 74.9 | 85.3  | 2.0   | 33.48 | 68.46 | 81.36 | 3.0   |
| depnet-vgg-myconceptsv3-mypasv4-fc7      | 40.1 | 73.9 | 84.1  | 2.0   | 33.16 | 67.74 | 80.6  | 3.0   |
| depnet-vgg-exconceptsv3-expasv4-fc7      | 41.8 | 75.3 | 86.3  | 2.0   | 33.52 | 68.16 | 81.44 | 3.0   |
| depnet-vgg-myconceptsv3-mypasprepv4-fc7  | 41.3 | 75.4 | 84.7  | 2.0   | 33.26 | 67.86 | 80.92 | 3.0   |
| depnet-vgg-exconceptsv3-expasprepv4-fc7  | 43.7 | 76.4 | 86.8  | 2.0   | 33.78 | 68.76 | 81.24 | 3.0   |

#### MSMIL features

| Method                                     | aR@1 | aR@5 | aR@10 | aMedr | sR@1  | sR@5  | sR@10 | sMedr |
|--------------------------------------------|------|------|-------|-------|-------|-------|-------|-------|
| depnet-msmil-myconceptsv3-fc7              | 54.2 | 86.4 | 93.7  | 1.0   | 40.9  | 75.9  | 87.28 | 2.0   |
| depnet-msmil-exconceptsv3-fc7              | 56.0 | 84.6 | 92.9  | 1.0   | 40.02 | 74.7  | 86.82 | 2.0   |
| depnet-msmil-mydepsv4-fc7                  | 50.9 | 84.6 | 92.6  | 1.0   | 38.92 | 74.1  | 85.9  | 2.0   |
| depnet-msmil-exdepsv4-fc7                  | 48.8 | 83.0 | 91.1  | 2.0   | 37.28 | 72.0  | 84.6  | 2.0   |
| depnet-msmil-mydepsprepv4-fc7              | 52.9 | 83.4 | 92.1  | 1.0   | 38.92 | 73.82 | 85.5  | 2.0   |
| depnet-msmil-exdepsprepv4-fc7              | 51.2 | 83.6 | 91.7  | 1.0   | 38.94 | 72.84 | 85.02 | 2.0   |
| depnet-msmil-mypasv4-fc7                   | 49.5 | 83.2 | 92.1  | 2.0   | 39.16 | 73.38 | 85.78 | 2.0   |
| depnet-msmil-expasv4-fc7                   | 10.5 | 31.0 | 46.5  | 12.0  | 8.4   | 27.94 | 42.7  | 14.0  |
| depnet-msmil-mypasprepv4-fc7               | 51.5 | 83.6 | 91.6  | 1.0   | 38.86 | 73.62 | 85.58 | 2.0   |
| depnet-msmil-expasprepv4-fc7               | 51.1 | 83.9 | 92.6  | 1.0   | 38.32 | 72.92 | 85.32 | 2.0   |
| depnet-msmil-myconceptsv3-mydepsv4-fc7     | 53.9 | 85.8 | 93.4  | 1.0   | 41.82 | 75.78 | 86.96 | 2.0   |
| depnet-msmil-exconceptsv3-exdepsv4-fc7     | 52.8 | 83.3 | 92.0  | 1.0   | 39.9  | 75.46 | 86.76 | 2.0   |
| depnet-msmil-myconceptsv3-mydepsprepv4-fc7 | 54.8 | 86.8 | 93.9  | 1.0   | 40.8  | 75.94 | 87.02 | 2.0   |
| depnet-msmil-exconceptsv3-exdepsprepv4-fc7 | 54.6 | 85.5 | 93.5  | 1.0   | 40.5  | 75.7  | 86.82 | 2.0   |
| depnet-msmil-myconceptsv3-mypasv4-fc7      | 53.0 | 84.2 | 92.2  | 1.0   | 41.3  | 75.88 | 86.76 | 2.0   |
| depnet-msmil-myconceptsv3-mypasprepv4-fc7  | 54.3 | 84.5 | 92.3  | 1.0   | 41.66 | 75.66 | 86.98 | 2.0   |
| depnet-msmil-exconceptsv3-expasprepv4-fc7  | 53.6 | 85.6 | 91.9  | 1.0   | 41.76 | 75.5  | 87.42 | 2.0   |

### Using Concept Matching
#### VGG features

| Method                                   | aR@1 | aR@5 | aR@10 | aMedr | sR@1  | sR@5  | sR@10 | sMedr |
|------------------------------------------|------|------|-------|-------|-------|-------|-------|-------|
| depnet-vgg-myconceptsv3-fc8              | 10.7 | 31.8 | 45.9  | 12.0  | 19.22 | 47.34 | 62.7  | 6.0   |
| depnet-vgg-exconceptsv3-fc8              | 10.8 | 30.0 | 43.1  | 14.0  | 18.8  | 45.34 | 61.28 | 7.0   |
| depnet-vgg-mydepsv4-fc8                  | 5.5  | 20.2 | 30.8  | 28.0  | 8.4   | 28.5  | 43.36 | 14.0  |
| depnet-vgg-exdepsv4-fc8                  | 5.6  | 20.2 | 31.1  | 25.0  | 8.68  | 28.48 | 43.12 | 14.0  |
| depnet-vgg-mydepsprepv4-fc8              | 5.6  | 20.5 | 31.7  | 24.0  | 8.86  | 27.96 | 41.18 | 15.0  |
| depnet-vgg-exdepsprepv4-fc8              | 6.3  | 21.4 | 32.3  | 24.0  | 7.94  | 28.78 | 43.08 | 14.0  |
| depnet-vgg-mypasv4-fc8                   | 6.5  | 22.1 | 34.0  | 24.0  | 9.56  | 29.78 | 43.62 | 14.0  |
| depnet-vgg-expasv4-fc8                   | 6.3  | 22.2 | 34.2  | 23.0  | 9.3   | 29.84 | 44.6  | 13.0  |
| depnet-vgg-mypasprepv4-fc8               | 6.2  | 22.0 | 33.4  | 25.0  | 8.82  | 29.0  | 43.72 | 14.0  |
| depnet-vgg-expasprepv4-fc8               | 6.4  | 22.9 | 34.3  | 22.0  | 8.8   | 28.3  | 42.94 | 14.0  |
| depnet-vgg-myconceptsv3-mydepsv4-fc8     | 9.1  | 28.4 | 42.0  | 14.0  | 17.3  | 45.56 | 62.28 | 7.0   |
| depnet-vgg-exconceptsv3-exdepsv4-fc8     | 8.9  | 28.0 | 39.3  | 15.0  | 16.94 | 44.36 | 60.42 | 7.0   |
| depnet-vgg-myconceptsv3-mydepsprepv4-fc8 | 8.1  | 28.9 | 43.9  | 14.0  | 17.68 | 46.58 | 62.36 | 6.0   |
| depnet-vgg-exconceptsv3-exdepsprepv4-fc8 | 10.3 | 29.0 | 41.2  | 15.0  | 17.42 | 44.64 | 60.66 | 7.0   |
| depnet-vgg-myconceptsv3-mypasv4-fc8      | 10.2 | 31.0 | 44.5  | 14.0  | 18.04 | 46.0  | 61.96 | 6.0   |
| depnet-vgg-exconceptsv3-expasv4-fc8      | 10.0 | 28.4 | 41.2  | 15.0  | 17.48 | 44.88 | 60.98 | 7.0   |
| depnet-vgg-myconceptsv3-mypasprepv4-fc8  | 9.5  | 29.5 | 42.1  | 15.0  | 17.52 | 46.1  | 61.76 | 6.0   |
| depnet-vgg-exconceptsv3-expasprepv4-fc8  | 9.7  | 28.1 | 42.1  | 15.0  | 17.06 | 44.96 | 60.54 | 7.0   |

#### MSMIL features

| Method                                     | aR@1 | aR@5 | aR@10 | aMedr | sR@1  | sR@5  | sR@10 | sMedr |
|--------------------------------------------|------|------|-------|-------|-------|-------|-------|-------|
| depnet-msmil-myconceptsv3-fc8              | 19.0 | 47.3 | 61.3  | 6.0   | 27.7  | 58.36 | 72.52 | 4.0   |
| depnet-msmil-exconceptsv3-fc8              | 16.2 | 44.8 | 57.4  | 7.0   | 24.12 | 55.32 | 70.16 | 4.0   |
| depnet-msmil-mydepsv4-fc8                  | 12.3 | 35.5 | 46.2  | 13.0  | 14.64 | 40.04 | 55.44 | 8.0   |
| depnet-msmil-exdepsv4-fc8                  | 12.1 | 35.2 | 45.8  | 13.0  | 14.4  | 39.86 | 55.0  | 8.0   |
| depnet-msmil-mydepsprepv4-fc8              | 14.0 | 36.1 | 46.8  | 12.0  | 13.74 | 40.22 | 55.38 | 9.0   |
| depnet-msmil-exdepsprepv4-fc8              | 12.6 | 35.3 | 45.7  | 13.0  | 13.32 | 38.94 | 53.7  | 9.0   |
| depnet-msmil-mypasv4-fc8                   | 12.7 | 34.2 | 46.5  | 12.0  | 14.22 | 41.36 | 56.62 | 8.0   |
| depnet-msmil-expasv4-fc8                   | 11.4 | 33.8 | 45.5  | 14.0  | 13.24 | 39.5  | 54.76 | 9.0   |
| depnet-msmil-mypasprepv4-fc8               | 13.0 | 34.5 | 47.0  | 12.0  | 14.02 | 40.06 | 55.84 | 8.0   |
| depnet-msmil-expasprepv4-fc8               | 11.7 | 33.5 | 45.7  | 13.0  | 13.04 | 39.14 | 54.58 | 9.0   |
| depnet-msmil-myconceptsv3-mydepsv4-fc8     | 18.1 | 44.9 | 58.1  | 7.0   | 26.06 | 57.56 | 72.38 | 4.0   |
| depnet-msmil-exconceptsv3-exdepsv4-fc8     | 17.3 | 43.8 | 58.0  | 7.0   | 23.26 | 55.7  | 70.26 | 4.0   |
| depnet-msmil-myconceptsv3-mydepsprepv4-fc8 | 18.8 | 45.0 | 57.3  | 7.0   | 26.32 | 57.94 | 72.3  | 4.0   |
| depnet-msmil-exconceptsv3-exdepsprepv4-fc8 | 16.5 | 43.7 | 57.6  | 7.0   | 23.58 | 55.48 | 70.28 | 4.0   |
| depnet-msmil-myconceptsv3-mypasv4-fc8      | 17.4 | 43.9 | 57.8  | 7.0   | 26.54 | 58.1  | 72.98 | 4.0   |
| depnet-msmil-exconceptsv3-expasv4-fc8      | 16.3 | 40.8 | 56.5  | 8.0   | 23.12 | 55.14 | 70.44 | 4.0   |
| depnet-msmil-myconceptsv3-mypasprepv4-fc8  | 17.3 | 44.2 | 58.7  | 7.0   | 26.62 | 57.7  | 72.64 | 4.0   |
| depnet-msmil-exconceptsv3-expasprepv4-fc8  | 16.2 | 41.6 | 57.2  | 8.0   | 23.1  | 55.56 | 70.42 | 4.0   |


