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
outLayer = g.node.add()
outLayer.CopyFrom(g.node[-2])
outputBlobName = "fcosDetectionOut"

inputs = []
while len(g.output)>1:
    o = g.output.pop()
    inputs.append(o.name)
inputs.append(g.output[0].name)
g.output[0].name = outputBlobName

while len(outLayer.input)>0:
    outLayer.input.pop()

while len(inputs)>0:
    outLayer.input.append(inputs.pop())

while len(outLayer.output)>1:
    outLayer.output.pop()
outLayer.output[0] = outputBlobName
outLayer.op_type = outputBlobName
dims = g.output[0].type.tensor_type.shape.dim
while len(dims)>3: dims.pop()
dims[1].dim_value = 100
dims[2].dim_value = 7
onnx.save(a, '0'+onnxFileName)
