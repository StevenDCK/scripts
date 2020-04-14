# -*- coding:utf-8 -*-
import os
import sys
import cv2
import numpy as np
from mxnet.contrib import onnx as onnx_mxnet

def convert2onnx(vDstModelPrefix, vEpoch):
    sym = '%s-symbol.json' % vDstModelPrefix
    params = '%s-%04d.params' % (vDstModelPrefix, vEpoch)
    input_shape = (1, 3, 960, 960)
    onnxFileName = params[0:-6] + "onnx"

    # pdb.set_trace()
    converted_model_path = onnx_mxnet.export_model(sym, params, [input_shape], np.float32, onnxFileName)
    from onnx.shape_inference import infer_shapes
    from onnx.optimizer import optimize
    om = onnx.load(onnxFileName)
    om = infer_shapes(om)
    om = optimize(om)
    onnx.save(om, onnxFileName)


import pdb
#pdb.set_trace()
if __name__ == '__main__':
    convert2onnx("/home/dbs/insightface/RetinaFace/model/mobilenet_0_25", 0)