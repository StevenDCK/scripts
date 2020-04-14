import os
import time
import sys
import onnx
from  onnx import helper
import pdb
#pdb.set_trace()
onnxFileName = str(sys.argv[1])
batchSize = int(sys.argv[2])
from onnx.shape_inference import infer_shapes
from onnx.optimizer import optimize
om = onnx.load(onnxFileName)
om.graph.input[0].type.tensor_type.shape.dim[0].dim_value = batchSize
v = om.graph.value_info
'''
while len(v)>0:
    v.pop()
for o in om.graph.output:
    o.type.tensor_type.shape.dim[0].dim_value=batchSize
om = infer_shapes(om)
om = optimize(om)
'''
onnx.save(om, onnxFileName)