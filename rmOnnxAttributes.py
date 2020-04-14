import os
import time
import sys
import onnx
from  onnx import helper
import pdb
#pdb.set_trace()
onnxFileName = str(sys.argv[1])
a = onnx.load(onnxFileName)
g = a.graph
for  n in g.node:
    if n.op_type == "BatchNormalization":
        n.attribute.remove(n.attribute[-1])
onnx.save(a, '0'+onnxFileName)