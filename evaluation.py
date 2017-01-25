"""
Evaluation code for multimodal-ranking
"""
import numpy

from datasets import load_dataset
from tools import encode_sentences, encode_images, load_model

import logging
from datetime import datetime
import argparse

logger = logging.getLogger(__name__)

def evalrank(model, data, feat, split='dev'):
    """
    Evaluate a trained model on either dev or test
    data options: f8k, f30k, coco
    """
    print 'Loading dataset'
    if split == 'dev':
        X = load_dataset(data, feat, load_train=False)[1]
    else:
        X = load_dataset(data, feat, load_train=False)[2]

    print 'Computing results...'
    ls = encode_sentences(model, X[0])
    lim = encode_images(model, X[1])

    (r1, r5, r10, medr) = i2t(lim, ls)
    print "Image to text: %.1f, %.1f, %.1f, %.1f" % (r1, r5, r10, medr)
    (r1i, r5i, r10i, medri) = t2i(lim, ls)
    print "Text to image: %.1f, %.1f, %.1f, %.1f" % (r1i, r5i, r10i, medri)

def i2t(images, captions, npts=None):
    """
    Images->Text (Image Annotation)
    Images: (5N, K) matrix of images
    Captions: (5N, K) matrix of captions
    """
    if npts == None:
        npts = images.shape[0] / 5
    index_list = []

    ranks = numpy.zeros(npts)
    for index in range(npts):

        # Get query image
        im = images[5 * index].reshape(1, images.shape[1])

        # Compute scores
        d = numpy.dot(im, captions.T).flatten()
        inds = numpy.argsort(d)[::-1]
        index_list.append(inds[0])

        # Score
        rank = 1e20
        for i in range(5*index, 5*index + 5, 1):
            tmp = numpy.where(inds == i)[0][0]
            if tmp < rank:
                rank = tmp
        ranks[index] = rank

    # Compute metrics
    r1 = 100.0 * len(numpy.where(ranks < 1)[0]) / len(ranks)
    r5 = 100.0 * len(numpy.where(ranks < 5)[0]) / len(ranks)
    r10 = 100.0 * len(numpy.where(ranks < 10)[0]) / len(ranks)
    medr = numpy.floor(numpy.median(ranks)) + 1
    return (r1, r5, r10, medr)

def t2i(images, captions, npts=None):
    """
    Text->Images (Image Search)
    Images: (5N, K) matrix of images
    Captions: (5N, K) matrix of captions
    """
    if npts == None:
        npts = images.shape[0] / 5
    ims = numpy.array([images[i] for i in range(0, len(images), 5)])

    ranks = numpy.zeros(5 * npts)
    for index in range(npts):

        # Get query captions
        queries = captions[5*index : 5*index + 5]

        # Compute scores
        d = numpy.dot(queries, ims.T)
        inds = numpy.zeros(d.shape)
        for i in range(len(inds)):
            inds[i] = numpy.argsort(d[i])[::-1]
            ranks[5 * index + i] = numpy.where(inds[i] == index)[0][0]

    # Compute metrics
    r1 = 100.0 * len(numpy.where(ranks < 1)[0]) / len(ranks)
    r5 = 100.0 * len(numpy.where(ranks < 5)[0]) / len(ranks)
    r10 = 100.0 * len(numpy.where(ranks < 10)[0]) / len(ranks)
    medr = numpy.floor(numpy.median(ranks)) + 1
    return (r1, r5, r10, medr)

if __name__ == '__main__':
    start = datetime.now()

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s: %(message)s')
    argparser = argparse.ArgumentParser(description = "Convert format in clcv project to format of the visual semantic embedding project")
    argparser.add_argument("dataset", type=str, default='coco', help="Type of features")
    argparser.add_argument("feat", type=str, default='coco', help="Type of features")
    argparser.add_argument("model", type=str, default='data/models/coco.npz', help="Path to the model")
    argparser.add_argument("split", type=str, default='dev', help="Path to the model")
    args = argparser.parse_args()
    logger.info(args)
    
    model = load_model(path_to_model=args.model)
    evalrank(model, args.dataset, args.feat, split=args.split)
    
    logger.info('done')
    logger.info('Time: %s', datetime.now() - start)
    