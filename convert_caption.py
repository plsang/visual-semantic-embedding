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
    argparser.add_argument("output_caption", type=str, help="Feature in vse format")
    argparser.add_argument("--split", type=str, default='train', help="split name")
    args = argparser.parse_args()
    
    logger.info(args)
    logger.info('Loading file: %s', args.input_json)
    infos = json.load(open(args.input_json))
    
    split = args.split
    if split == 'dev':
        split = 'val'
        
    captions = []
    for info in infos['images']:
        if info['split'] == split:
            raw_captions = [' '.join(s['tokens']) for s in info['sentences']]
            if len(raw_captions) > 5:
                raw_captions = raw_captions[:5]
            elif len(raw_captions) < 5:
                logger.error('Less than 5 captions')
            captions.extend(raw_captions)
    
    logger.info('Saving caption file: %s', args.output_caption)
    with open(args.output_caption, 'w') as f:
        for caption in captions:
            f.write(caption + '\n')
    
    logger.info('done')
    logger.info('Time: %s', datetime.now() - start)