"""
Dataset loading
"""
import numpy

#-----------------------------------------------------------------------------#
# Specify dataset(s) location here
#-----------------------------------------------------------------------------#
path_to_data = 'data/'
#-----------------------------------------------------------------------------#

def load_dataset(name='coco', feat='coco', load_train=True):
    """
    Load captions and image features
    Possible options: f8k, f30k, coco
    """
    loc = path_to_data + name + '/'
    
    # Captions
    train_caps, dev_caps, test_caps = [],[],[]
    if load_train:
        with open(loc+name+'_train_captions.txt', 'rb') as f:
            for line in f:
                train_caps.append(line.strip())
    else:
        train_caps = None
    with open(loc+name+'_dev_captions.txt', 'rb') as f:
        for line in f:
            dev_caps.append(line.strip())
    with open(loc+name+'_test_captions.txt', 'rb') as f:
        for line in f:
            test_caps.append(line.strip())
            
    # Image features
    if load_train:
        train_ims = numpy.load(loc+feat+'_train_ims.npy')
    else:
        train_ims = None
    dev_ims = numpy.load(loc+feat+'_dev_ims.npy')
    test_ims = numpy.load(loc+feat+'_test_ims.npy')
    
    # select only top 1K
    dev_ims = dev_ims[:5000]
    dev_caps = dev_caps[:5000]
    test_ims = test_ims[:5000]
    test_caps = test_caps[:5000]
    
    return (train_caps, train_ims), (dev_caps, dev_ims), (test_caps, test_ims)

