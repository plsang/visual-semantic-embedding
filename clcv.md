# Image/Caption Retrieval Task

## How to run?

  * Edit Makefile, update `COCO_DATA` path
  * Edit `FEATS` to set feature types
  * `make train GID=1`
  * `make test GID=2`
  
## Results

  **MS COCO**
  Image to text -- Text to image

| Method | aR@1 | aR@5 | aR@10 | aMedr | sR@1 | sR@5 | sR@10 | sMedr |
| ----- | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| vgg (fc7) | 43.4 | 75.7 | 85.8 | 2 | 31.0 | 66.7 | 79.9 | 3 
| exconceptsv3 (fc7) | 42.6 | 74.5 | 85.6 | 2 | 32.6 | 67.2 | 80.0 | 3 
| exdepsv4 (fc7) | 34.0 | 67.4 | 80.8 | 3 | 28.9 | 63.6 | 77.5 | 3 
| expasv4 (fc7) | - | 67.4 | 80.8 | 3 | 28.9 | 63.6 | 77.5 | 
| expasprepv4 (fc7) | - | 67.4 | 80.8 | 3 | 28.9 | 63.6 | 77.5 | 
| exconceptsv3exdepsv4 (fc7) | 35.5 | 69.8 | 81.6 | 2 | 29.5 | 64.6 | 78.9 | 3 
| exconceptsv3-exdepsv4 (concat) | 41.5 |  75.0 | 86.4 | 2 | 33.6 | 67.5 | 80.7 | 3
| exconceptsv3-expasv4 (concat) | 41.5 |  75.0 | 86.4 | 2 | 33.6 | 67.5 | 80.7 | 3
| exconceptsv3-expasprepv4 (concat) | 41.5 |  75.0 | 86.4 | 2 | 33.6 | 67.5 | 80.7 | 3
| | 
| myconceptsv3 (fc7) | 42.6 | 74.5 | 85.6 | 2 | 32.6 | 67.2 | 80.0 | 3 
| mydepsv4 (fc7) | 34.0 | 67.4 | 80.8 | 3 | 28.9 | 63.6 | 77.5 | 3 
| mypasv4 (fc7) | - | 67.4 | 80.8 | 3 | 28.9 | 63.6 | 77.5 | 
| mypasprepv4 (fc7) | - | 67.4 | 80.8 | 3 | 28.9 | 63.6 | 77.5 | 
| myconceptsv3-mydepsv4 (concat) | 41.5 |  75.0 | 86.4 | 2 | 33.6 | 67.5 | 80.7 | 3
| myconceptsv3-mypasv4 (concat) | 41.5 |  75.0 | 86.4 | 2 | 33.6 | 67.5 | 80.7 | 3
| myconceptsv3-mypasprepv4 (concat) | 41.5 |  75.0 | 86.4 | 2 | 33.6 | 67.5 | 80.7 | 3
