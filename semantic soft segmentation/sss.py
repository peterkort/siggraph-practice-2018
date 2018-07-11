# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 12:10:20 2018

@author: Peter
"""

import numpy as np

def get_test_image(i = 0):
    import PIL
    if i == 1:
        file_name = "test images/IMGP0061.JPG"
    else:
        file_name = "test images/IMGP0014.JPG"
    img = PIL.Image.open(file_name)
    arr = np.asarray(img, dtype=np.uint8)
    return arr

import caffe
caffe.set_device(0)
caffe.set_mode_gpu()
prototxt_filename = 'deep lab v2 resnet/test.prototxt'
caffemodel_filename = 'deep lab v2 resnet/train_iter_20000.caffemodel'

def do_the_caffe_thing(img):
    net = caffe.Net("deep lab v2 resnet/test.prototxt", "deep lab v2 resnet/train_iter_20000.caffemodel", caffe.TEST)

