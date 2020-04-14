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
var = g.input[-1]
if not var.name.startswith("var__"):
    tmp = g.input[-1]
    mean = g.input.add()
    var = g.input.add()
    mean.CopyFrom(tmp)
    var.CopyFrom(tmp)
else: mean = g.input[-2]

mean.name = "mean__"+ str(sys.argv[2]) #separator is ','
var.name = "var__"+str(sys.argv[3]) #separator is ','

onnx.save(a, onnxFileName)
