# -*- coding:utf8 -*-
import os
import sys
from argparse import ArgumentParser
	
if __name__=="__main__":
	parser = ArgumentParser(description="Add mean value and variance to caffeModel.")
	parser.add_argument('--filePrefix', default="ssdlite_MV1-0.5-BN-128HEAD-PROB02-VOC512_512x512_0.5x", help="The prefix of model file.")
	args = parser.parse_args()

	srcModelFileName = args.filePrefix + ".prototxt"
	srcWeightsFileName = args.filePrefix + ".caffemodel"
	rgbWeightsFileName = args.filePrefix + "rgb.caffemodel"
	sys.path.append("/home/dbs/caffe/python")
	os.system("python rgb_bgr.py --srcModel " + srcModelFileName + " --srcWeights " + srcWeightsFileName + " --dstWeights  " + rgbWeightsFileName)

	modelMeanVarianceFileName = args.filePrefix + "MeanVariance.prototxt"
	weightMeanVarianceFileName = args.filePrefix + "MeanVariance.caffemodel"
	os.system("python addMeanVar2Model.py --srcModel " + srcModelFileName + " --srcWeights " + rgbWeightsFileName + " --dstModel " + modelMeanVarianceFileName + " --dstWeights  " + weightMeanVarianceFileName)

	sys.path.append("/opt/movidius/caffe/python")
	os.system("mvNCCompile " + modelMeanVarianceFileName + " -w " + weightMeanVarianceFileName + " -s 8 " + " -o " +  args.filePrefix)
