"""
Convert format in clcv project to format of the visual semantic embedding project
"""

from __future__ import print_function
import logging
from datetime import datetime
import argparse
import h5py, json
import numpy as np
import re

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    start = datetime.now()

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s: %(message)s')

    argparser = argparse.ArgumentParser(description = "Convert format in clcv project to format of the visual semantic embedding project")
    argparser.add_argument("input_json", type=str, help="Json file contains splits provided by Karpathy http://cs.stanford.edu/people/karpathy/deepimagesent/")
    argparser.add_argument("feat_file", type=str, help="Feature provided by clcv project")
    argparser.add_argument("output_feat", type=str, help="Feature in vse format")
    argparser.add_argument("--split", type=str, default='train', help="split name")
    argparser.add_argument("--max_dim", type=int, default=4096, help="max number of features")
    args = argparser.parse_args()
    
    logger.info(args)
    logger.info('Loading file: %s', args.input_json)
    infos = json.load(open(args.input_json))
    
    split = args.split
    if split == 'dev':
        split = 'val'
        
    image_ids = []
    for info in infos['images']:
        if info['split'] == split:
            image_id = str(info['cocoid'])
            image_ids.append(image_id)
    
    feats = {}
    h5f = h5py.File(args.feat_file, 'r')
    feat_size = h5f['data'].shape[1]
    if feat_size > args.max_dim:
        feat_size = args.max_dim
    
    logger.info('Reading features')
    for ii,image_id in enumerate(h5f['index']):
        feats[image_id] = ii
    
    out = np.zeros((len(image_ids), feat_size), dtype=np.float32)
    
    logger.info('Converting features')
    for ii,image_id in enumerate(image_ids):
        fi = feats[image_id]
        out[ii] = h5f['data'][fi,:feat_size]
    
    logger.info('Apply unit normalization')
    l2norm = np.linalg.norm(out, axis=1)
    out = out / l2norm[:, None]
    
    logger.info('Repeating feature 5 times, corresponding to 5 images')
    out = np.repeat(out, 5, 0)
        
    logger.info('Saving feature file: %s', args.output_feat)
    np.save(args.output_feat, out)
    h5f.close()
        
    logger.info('done')
    logger.info('Time: %s', datetime.now() - start)