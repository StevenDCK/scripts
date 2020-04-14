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
print(helper.printable_graph(g))