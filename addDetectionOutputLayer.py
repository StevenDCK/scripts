import os
import time
import sys
import onnx
from  onnx import helper
import pdb
#pdb.set_trace()
onnxFileName = str(sys.argv[1])
dstFileName = "ssd"+onnxFileName
a = onnx.load(onnxFileName)
g = a.graph
//nodes
src = g.node.pop()
anchor = src.input[0]
loc = src.input[1]
dst = g.node.add()
detectionLayerName = src.output[0]
dst.CopyFrom(src)
dst.op_type = "DetectionOutput"
confLayerOutputName = g.node[-3].output[0]
for i in range(len(dst.input)): dst.input.pop()
dst.input.append(loc)
dst.input.append(confLayerOutputName)
dst.input.append(anchor)

//outputs
src = g.output[-1]
for i in range(len(g.output)): g.output.pop()
dst = g.output.add()
dst.CopyFrom(src)
dst.name = detectionLayerName

dims = dst.type.tensor_type.shape.dim
for i in range(len(dims)-3): dims.pop()
dims[1].dim_value = 100
dims[2].dim_value = 7

onnx.save(m, dstFileName)

print(helper.printable_graph(g))
print("Finish!")