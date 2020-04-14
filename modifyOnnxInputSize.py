import os
import time
import sys
import onnx
from  onnx import helper
import pdb
##
onnxFileName = str(sys.argv[1])
from onnx.shape_inference import infer_shapes
from onnx.optimizer import optimize
om = onnx.load(onnxFileName)
om.graph.input[0].type.tensor_type.shape.dim[0].dim_value = 1
om.graph.input[0].type.tensor_type.shape.dim[1].dim_value =3
om.graph.input[0].type.tensor_type.shape.dim[2].dim_value = 540
om.graph.input[0].type.tensor_type.shape.dim[3].dim_value = 960
v = om.graph.value_info
while len(v)>0:
    v.pop()


#pdb.set_trace()
ots = om.graph.output
h = 17
for i in range(3)://this need do by yourself.
    ots[i*4+0].type.tensor_type.shape.dim[2].dim_value=h
    ots[i*4+1].type.tensor_type.shape.dim[2].dim_value=h
    ots[i*4+2].type.tensor_type.shape.dim[2].dim_value=h
    ots[i*4+3].type.tensor_type.shape.dim[2].dim_value=h
    h *= 2

om = infer_shapes(om)
om = optimize(om)
onnx.save(om, onnxFileName)