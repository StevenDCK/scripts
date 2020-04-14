#!/bin/bash
echo "bgr --> rgb "
export PYTHONPATH=/home/dbs/caffe/python
filePrefix=$1
python rgb_bgr.py --modelFilePrefix $filePrefix
echo "addMeanVar2Model"
python addMeanVar2Model.py  --modelFilePrefix $filePrefix
export PYTHONPATH=/opt/movidius/caffe/python
echo "caffe --> movidius"
mvNCCompile "${filePrefix}MeanVariance.prototxt" -w "${filePrefix}_MeanVariance.caffemodel" -s 8 -o $filePrefix
echo "generate model of $filePrefix"
