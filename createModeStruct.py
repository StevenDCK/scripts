#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy as np
import sys
import os
import os.path as osp
import google.protobuf as pb
import google.protobuf.text_format
from argparse import ArgumentParser
import caffe

import pdb
#pdb.set_trace()

g_SrcNameSet = 'ssdfls2x.prototxt'

def test(vSrcModelFileName):
	with open(vSrcModelFileName) as f:
		netStruct = caffe.proto.caffe_pb2.NetParameter()
		pb.text_format.Merge(f.read(), netStruct)
	for i, layer in enumerate(netStruct.layer):
		if layer.type == 'Convolution' and layer.bottom == ['data']:
			if layer.convolution_param.bias_term == False:
				layer.convolution_param.bias_term = True
				layer.convolution_param.bias_filler.type = 'constant'
				layer.convolution_param.bias_filler.value = 0.0
				with open(vDstModelFileName, 'w') as f:
					f.write(pb.text_format.MessageToString(netStruct))
			else:
				noMeanValue = True
			break

if __name__ == "__main__":
	test(g_SrcNameSet)