#!/bin/bash
protoc --python_out=. -I=. caffe.proto
protoc --python_out=. -I=. caffe_upsample.proto




