"""
Collecting results
"""

from __future__ import print_function
import logging
from datetime import datetime
import argparse
import h5py, json
import numpy as np
import os

logger = logging.getLogger(__name__)

    
if __name__ == '__main__':
    start = datetime.now()

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s: %(message)s')

    argparser = argparse.ArgumentParser(description = "Convert format in clcv project to format of the visual semantic embedding project")
    argparser.add_argument("result_dir", type=str, default='data/results')
    argparser.add_argument("output_txt", type=str, default='data/results/output.txt')
    argparser.add_argument("--prefix", type=str, default='depnet')
    argparser.add_argument("--feat", type=str, default='fc7')
    argparser.add_argument("--split", type=str, default='test')
    argparser.add_argument("--task", type=str, default='vse')
    
    args = argparser.parse_args()
    
    feats = ['conceptsv3',
         'depsv4',
         'depsprepv4',
         'pasv4',
         'pasprepv4']
    model_types = ['vgg', 'msmil']
    feat_types = ['my', 'ex']
    
    data_names = []
    concat_names = []
    for feat in feats:
        for model_type in model_types:
            for feat_type in feat_types:
                data_name = '{}-{}-{}{}-{}'.format(args.prefix, model_type,
                                                  feat_type, feat, args.feat)
                data_names.append(data_name)
                if feats.index(feat) != 0:
                    concat_name = '{}-{}-{}{}-{}{}-{}'.format(args.prefix, model_type,
                                                              feat_type, feats[0],
                                                  feat_type, feat, args.feat)
                    concat_names.append(concat_name)
    data_names.extend(concat_names)
        
    with open(args.output_txt, 'w') as of:
        of.write('{},{},{},{},{},{},{},{},{}\n'.format('Method', 'aR@1', 'aR@5', 'aR@10', 
                                                     'aMedr', 'sR@1', 'sR@5', 'sR@10', 
                                                     'sMedr'))
        for data_name in data_names:
            json_file = '{}_{}_{}.json'.format(data_name, args.split, args.task)
            json_path = os.path.join(args.result_dir, json_file)
            if not os.path.exists(json_path):
                logger.info('File not found: %s', json_path)
                continue
            json_data = json.load(open(json_path))         
            of.write('{},{},{},{},{},{},{},{},{}\n'.format(data_name, json_data['i2t'][0],
                                                           json_data['i2t'][1],
                                                           json_data['i2t'][2],
                                                           json_data['i2t'][3],
                                                           json_data['t2i'][0],
                                                           json_data['t2i'][1],
                                                           json_data['t2i'][2],
                                                           json_data['t2i'][3]))
                        
    logger.info('Wrote to: %s', args.output_txt)
    logger.info('Time: %s', datetime.now() - start)