import os
import time
import sys
import onnx
from  onnx import helper
import pdb
#pdb.set_trace()
onnxFileName = str(sys.argv[1])
from onnx.shape_inference import infer_shapes
from onnx.optimizer import optimize
om = onnx.load(onnxFileName)
v = om.graph.value_info
while len(v)>0:
    v.pop()
onnx.save(om, onnxFileName)