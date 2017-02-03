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
    argparser.add_argument("feat_file1", type=str, help="Feature provided by clcv project")
    argparser.add_argument("feat_file2", type=str, help="Feature provided by clcv project")
    argparser.add_argument("output_feat", type=str, help="Feature in vse format")
    
    args = argparser.parse_args()
    
    logger.info('Loading feature 1: %s', args.feat_file1)
    f1 = np.load(args.feat_file1)
    
    logger.info('Loading feature 2: %s', args.feat_file2)
    f2 = np.load(args.feat_file2)
    
    logger.info('concatenate')
    f = np.concatenate((f1, f2), axis=1)
    
    logger.info('Saving feature file: %s', args.output_feat)
    np.save(args.output_feat, f)
    
    logger.info('done')
    logger.info('Time: %s', datetime.now() - start)