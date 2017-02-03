"""
Matching based on cosine similarity
"""

from __future__ import print_function
import logging
from datetime import datetime
import argparse
import h5py, json
import numpy as np
import re

from evaluation import i2t, t2i

logger = logging.getLogger(__name__)
    
if __name__ == '__main__':
    start = datetime.now()

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s: %(message)s')

    argparser = argparse.ArgumentParser(description = "Matching based on cosine similarity")
    argparser.add_argument("--pred", type=str, nargs='+', help="Feature provided by clcv project")
    argparser.add_argument("--gold", type=str, nargs='+', help="Feature provided by clcv project")
    argparser.add_argument("--output_json", type=str, help="Feature provided by clcv project")
    argparser.add_argument("--topk", type=int, default=5000, help="Feature provided by clcv project")
    
    args = argparser.parse_args()
    
    logger.info('Loading prediction: %s', args.pred)
    lim = None
    for pred_file in args.pred:
        lim_t = np.load(pred_file)
        if lim is None:
            lim = lim_t
        else:
            lim = np.concatenate((lim, lim_t), axis=1)
    lim = lim[:args.topk]
    
    logger.info('Loading gold: %s', args.gold)
    ls = None
    for gold_file in args.gold:
        ls_t = np.load(gold_file)
        if ls is None:
            ls = ls_t
        else:
            ls = np.concatenate((ls, ls_t), axis=1)
    ls = ls[:args.topk]
    
    logger.info('Evaluating')
    (r1, r5, r10, medr) = i2t(lim, ls)
    logger.info("Image to text: %.1f, %.1f, %.1f, %.1f", r1, r5, r10, medr)
    (r1i, r5i, r10i, medri) = t2i(lim, ls)
    logger.info("Text to image: %.1f, %.1f, %.1f, %.1f", r1i, r5i, r10i, medri)
    
    logger.info('Writing output to: %s', args.output_json)
    out = {}
    out['i2t'] = (r1, r5, r10, medr)
    out['t2i'] = (r1i, r5i, r10i, medri)
    json.dump(out, open(args.output_json, 'w'))
    
    logger.info('done')
    logger.info('Time: %s', datetime.now() - start)