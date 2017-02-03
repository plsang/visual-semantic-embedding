"""
Convert dependency to vectors for dep matching
"""

from __future__ import print_function
import logging
from datetime import datetime
import argparse
import h5py, json
import numpy as np
import scipy.sparse
from sklearn.preprocessing import MultiLabelBinarizer

logger = logging.getLogger(__name__)
                
if __name__ == '__main__':
    start = datetime.now()

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s: %(message)s')

    argparser = argparse.ArgumentParser(description = "Convert dependency to vectors for dep matching")
    argparser.add_argument("input_json", type=str, help="Json file contains splits provided by Karpathy http://cs.stanford.edu/people/karpathy/deepimagesent/")
    argparser.add_argument("h5_file", type=str, help="vocab file")
    argparser.add_argument("jsonl_file", type=str, help="jsonl file")
    argparser.add_argument("output_feat", type=str, help="Feature in vse format")
    argparser.add_argument("--split", type=str, default='test', help="split name")
    argparser.add_argument('--target_id', type=str, dest='target_id', default='text_id', help='text_id')
    argparser.add_argument('--target_concept', type=str, dest='target_concept', default='coarse_lemmas', help='Name (attribute in the input JSONL file) of target concepts')
    args = argparser.parse_args()
    
    logger.info(args)
    logger.info('Loading file: %s', args.input_json)
    infos = json.load(open(args.input_json))
    
    split = args.split
    if split == 'dev':
        split = 'val'
        
    sentids_dict = {}
    image_ids = []
    for info in infos['images']:
        if info['split'] == split:
            image_id = str(info['cocoid'])
            image_ids.append(image_id)
            sentids_dict[image_id] = info['sentids'][:5]
    
    logger.info('Load vocabulary file: %s', args.h5_file)
    h5 = h5py.File(args.h5_file)
    vocab_list = [w for w in h5['columns']]
    h5.close()
    
    vocab = {v:i for i,v in enumerate(vocab_list)}
    
    logger.info('Load input file: %s', args.jsonl_file)
    with open(args.jsonl_file) as f:
        target_data = [json.loads(line) for line in f]
    
    data_dict = {}
    for l in target_data:
        key = str(l[args.target_id])
        concepts = [json.dumps(c) for c in l[args.target_concept]]
        vec = [vocab[c] for c in concepts if c in vocab]
        data_dict[key] = vec
    
    logger.info('Converting features')
    out_matrix = []
    for image_id in image_ids:
        sentids = sentids_dict[image_id]
        for sentid in sentids:
            out_matrix.append(data_dict[str(sentid)])
    
    binarizer = MultiLabelBinarizer(classes=range(len(vocab)))
    out = binarizer.fit_transform(out_matrix)
    
    #logger.info('Apply unit normalization')
    #l2norm = np.linalg.norm(out, axis=1)
    #out = out / l2norm[:, None]
        
    logger.info('Saving feature file: %s', args.output_feat)
    np.save(args.output_feat, out)
        
    logger.info('done')
    logger.info('Time: %s', datetime.now() - start)