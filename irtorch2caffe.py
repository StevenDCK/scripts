import numpy as np
import sys
import torch
import collections
import google.protobuf as pb
_pytorch_model = 'res50.pth'
caffePrototxtFileName = 'r50se.prototxt'
_caffe_save_model = 'r50se.caffemodel'
torchNet = torch.load(_pytorch_model, map_location=lambda storage, loc: storage)

res_dict = collections.OrderedDict()
for layer_name, data in torchNet.items():
   res_dict[layer_name] = data.cpu().numpy()
   #print(layer_name.encode('utf-8'), res_dict[layer_name].shape)

import caffe
#import pdb
#pdb.set_trace()
caffe.set_mode_cpu()

g_convIndex = -3
netCaffe = caffe.Net(caffePrototxtFileName, caffe.TEST)
caffeLayerNames = netCaffe._layer_names

def _getBlob(vTorchName):
    postFix = vTorchName.split('.')[-1]
    dstLayerName = vTorchName[0: len(vTorchName)-len(postFix)-1]
    if postFix.startswith('running'): dstLayerName += ".bn"
    if 'bias' == postFix or 'running_var' == postFix:
        dstIndex = 1
    else:dstIndex= 0
    return dstLayerName, dstIndex

layerIndex = 1
for srcName, srcData in torchNet.items():
    dstLayerName, dstIndex = _getBlob(srcName)
    dstBlob = torchNet[srcName] #.reshape(dstShape)
    netCaffe.params[dstLayerName][dstIndex].data[...] = dstBlob
    if srcName.endswith('running_var'):
        netCaffe.params[dstLayerName][2].data[...] = np.array([1.]).astype(np.float32)
    print(str(layerIndex)+" : " +srcName + " --> " + dstLayerName)
    #if 63==layerIndex: break
    layerIndex += 1
#for i in range(24):
    #netCaffe.params['body.'+str(i) + '.res_layer.5.fc3'][0].data[...] = 1.0
netCaffe.save(_caffe_save_model)
print('finish torch-->caffe!')


def modifyLayerName(vSrcModelFileName):
    with open(vSrcModelFileName) as f:
        netStruct = caffe.proto.caffe_pb2.NetParameter()
        pb.text_format.Merge(f.read(), netStruct)
    for i, layer in enumerate(netStruct.layer):
        if layer.type == 'Prelu' :
            layer.name += '_prelu'
    with open(vSrcModelFileName, 'w') as f:
        f.write(pb.text_format.MessageToString(netStruct))