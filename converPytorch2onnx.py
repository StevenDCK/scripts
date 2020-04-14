# -*- coding:utf-8 -*-
import os
import sys
import torch
import cv2
import numpy as np

_classes = ('__background__',  'face')
modelWidthHeight = 112
PIXEL_MEANS = np.array([[[103.52, 116.28, 123.675]]])#bgr103.52, 116.28, 123.675 #rgb123.675, 116.28, 103.52
STD = np.array([[[57.375, 57.12, 58.395]]]) #BGR [57.375, 57.12, 58.395] rgb 57.375, 57.12, 58.395


def sumabs(vArray):
    a = np.abs(vArray)
    return  np.sum(a)

def preprocess():
    #img = cv2.imread("4faces.jpg")
    #im = cv2.resize(img, (modelWidthHeight, modelWidthHeight))
    #cv2.imwrite('4faces2.jpg', im)
#    im = cv2.imread('/home/dbs/face.jpg')
    im = cv2.imread('t1.png')
    im = im.astype(np.float32, copy=True)
    im = cv2.resize(im, (modelWidthHeight, modelWidthHeight))
    im -= PIXEL_MEANS
    im /= STD
    im = im.transpose(2, 0, 1)
    im = im.reshape((1,) + im.shape)
    print ("input sumabs:", sumabs(im))
    return im

def weight_filler(src, dst):
    updated_dict = dst.copy()
    match_layers = []
    mismatch_layers = []
    for dst_k in dst:
        # if 'blur1' in dst_k or 'bn_1' in dst_k:
        #     print()
        if dst_k in src:
            src_k = dst_k
            if src[src_k].shape == dst[dst_k].shape:
                match_layers.append(dst_k)
                updated_dict[dst_k] = src[src_k]
            else:
                mismatch_layers.append(dst_k)
        elif dst_k.replace('module.', '') in src:
            src_k = dst_k.replace('module.', '')
            if src[src_k].shape == dst[dst_k].shape:
                match_layers.append(dst_k)
                updated_dict[dst_k] = src[src_k]
            else:
                mismatch_layers.append(dst_k)
        elif 'module.' + dst_k in src:
            src_k = 'module.' + dst_k
            if src[src_k].shape == dst[dst_k].shape:
                match_layers.append(dst_k)
                updated_dict[dst_k] = src[src_k]
            else:
                mismatch_layers.append(dst_k)
        elif 'Conv_Body.' + dst_k in src:
            src_k = 'Conv_Body.' + dst_k
            if src[src_k].shape == dst[dst_k].shape:
                match_layers.append(dst_k)
                updated_dict[dst_k] = src[src_k]
            else:
                mismatch_layers.append(dst_k)
        elif dst_k.replace('_tmp_', '') in src:  # for sync bn
            src_k = dst_k.replace('_tmp_', '')
            if src[src_k].shape == dst[dst_k].shape:
                match_layers.append(dst_k)
                updated_dict[dst_k] = src[src_k]
            else:
                mismatch_layers.append(dst_k)
        elif dst_k.replace('_tmp_', '').replace('module.', '') in src:  # for sync bn
            src_k = dst_k.replace('_tmp_', '').replace('module.', '')
            if src[src_k].shape == dst[dst_k].shape:
                match_layers.append(dst_k)
                updated_dict[dst_k] = src[src_k]
            else:
                mismatch_layers.append(dst_k)
        elif 'module.' + dst_k.replace('_tmp_', '') in src:  # for sync bn
            src_k = 'module.' + dst_k.replace('_tmp_', '')
            if src[src_k].shape == dst[dst_k].shape:
                match_layers.append(dst_k)
                updated_dict[dst_k] = src[src_k]
            else:
                mismatch_layers.append(dst_k)
        else:
            mismatch_layers.append(dst_k)

    return updated_dict, match_layers, mismatch_layers

def weight_filler1(src, dst):
    updated_dict = dst.copy()
    match_layers = []
    mismatch_layers = []
    for dst_k in dst:
        # if 'blur1' in dst_k or 'bn_1' in dst_k:
        #     print()
        if dst_k in src:
            src_k = dst_k
            if src[src_k].shape == dst[dst_k].shape:
                match_layers.append(dst_k)
                updated_dict[dst_k] = src[src_k]
            else:
                mismatch_layers.append(dst_k)
        elif dst_k.replace('module.', '') in src:
            src_k = dst_k.replace('module.', '')
            if src[src_k].shape == dst[dst_k].shape:
                match_layers.append(dst_k)
                updated_dict[dst_k] = src[src_k]
            else:
                mismatch_layers.append(dst_k)
        elif 'module.' + dst_k in src:
            src_k = 'module.' + dst_k
            if src[src_k].shape == dst[dst_k].shape:
                match_layers.append(dst_k)
                updated_dict[dst_k] = src[src_k]
            else:
                mismatch_layers.append(dst_k)
        elif 'Conv_Body.' + dst_k in src:
            src_k = 'Conv_Body.' + dst_k
            if src[src_k].shape == dst[dst_k].shape:
                match_layers.append(dst_k)
                updated_dict[dst_k] = src[src_k]
            else:
                mismatch_layers.append(dst_k)
        elif dst_k.replace('_tmp_', '') in src:  # for sync bn
            src_k = dst_k.replace('_tmp_', '')
            if src[src_k].shape == dst[dst_k].shape:
                match_layers.append(dst_k)
                updated_dict[dst_k] = src[src_k]
            else:
                mismatch_layers.append(dst_k)
        elif dst_k.replace('_tmp_', '').replace('module.', '') in src:  # for sync bn
            src_k = dst_k.replace('_tmp_', '').replace('module.', '')
            if src[src_k].shape == dst[dst_k].shape:
                match_layers.append(dst_k)
                updated_dict[dst_k] = src[src_k]
            else:
                mismatch_layers.append(dst_k)
        elif 'module.' + dst_k.replace('_tmp_', '') in src:  # for sync bn
            src_k = 'module.' + dst_k.replace('_tmp_', '')
            if src[src_k].shape == dst[dst_k].shape:
                match_layers.append(dst_k)
                updated_dict[dst_k] = src[src_k]
            else:
                mismatch_layers.append(dst_k)
        else:
            mismatch_layers.append(dst_k)

    return updated_dict, match_layers, mismatch_layers


def weight_filler0(src, dst):
    updated_dict = dst.copy()
    match_layers = []
    mismatch_layers = []
    diff_names = ['', 'module.', 'module.Conv_Body.', '_tmp_']
    for dst_k in dst:
        is_match = False
        for diff_name in diff_names:
            if dst_k.replace(diff_name, '') in src:
                src_k = dst_k.replace(diff_name, '')
                if src[src_k].shape == dst[dst_k].shape:
                    match_layers.append(dst_k)
                    updated_dict[dst_k] = src[src_k]
                    is_match = True
                else:
                    mismatch_layers.append(dst_k)

            elif diff_name + dst_k in src:
                src_k = diff_name + dst_k
                if src[src_k].shape == dst[dst_k].shape:
                    match_layers.append(dst_k)
                    updated_dict[dst_k] = src[src_k]
                    is_match = True
                else:
                    mismatch_layers.append(dst_k)
        if '.num_batches_tracked' in dst_k:
            is_match = True
            print('ignore ', dst_k)
        if not is_match:
            print(dst_k)
            mismatch_layers.append(dst_k)

    return updated_dict, match_layers, mismatch_layers

import onnx
from  onnx import helper
from onnx import numpy_helper
#from IR_SE_FaceNet import *
from vertify import MobileFaceNet_DEX_c3
from MobileFaceNetVerifyAgeGender import MobileFaceNetVerifyAgeGender
modelName = "res50.pth"
#modelFileName = 'MobileFaceNetVerifyAgeGender.pth'
modelFileName = 'gch.pth' #'model_best._a.pth'

from onnx.shape_inference import infer_shapes
from onnx.optimizer import optimize

def runPytorch(img):
    torchModel = MobileFaceNet_DEX_c3() #MobileFaceNet_DEX_c3() # MobileFaceNetVerifyAgeGender() #IR_SE_FaceNet() #
    model_dict = torchModel.state_dict()
    torchWeights = torch.load(modelFileName, map_location=lambda storage, loc: storage)
    updated_dict, match_layers, mismatch_layers = weight_filler(torchWeights, model_dict)
    print("The mismatch layers %s", mismatch_layers)
    model_dict.update(updated_dict)
    torchModel.load_state_dict(model_dict)
    torchModel.eval().cpu()
    #img = img[0]
    #imgs = np.array([img, img,img, img], dtype=np.float32)
    y = torchModel.forward(torch.from_numpy(img).cpu())
    print(y.abs().sum())
    onxFileName  = "nameAgeGenderFaceBlur.onnx"
    dummy_input = torch.randn(4, 3, modelWidthHeight, modelWidthHeight)
    torch.onnx.export(torchModel.cpu(), dummy_input.cpu(), onxFileName, verbose=True)
    torch.onnx.in
    om = onnx.load(onxFileName)
    om = infer_shapes(om)
    om = optimize(om)
    onnx.save(om, onxFileName)
    a = om.graph
    #import pdb
    #pdb.set_trace()
    helper.printable_graph(a)
    v = a.value_info

'''
    a = onnx.load('ageGenderWithShape.onnx')
    g = a.graph
    print(helper.printable_graph(g))
    onnx.checker.check_model(a)
    onnx.helper.strip_doc_string(a)
    model = infer_shapes(a)
    g = model.graph
    model = optimize(model)
    g = model.graph
    onnx.checker.check_model(model)
    #onnx.save(model, 'ageGenderWithShape.onnx')

    g = model.graph

'''



import pdb
#pdb.set_trace()
if __name__ == '__main__':
    img = preprocess()
    runPytorch(img)