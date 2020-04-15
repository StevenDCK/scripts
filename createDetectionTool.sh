#!/bin/bash
cd convertProtobufBinary2txt
python3 create.py --pro postPara3DKeyPoints.proto --dat C3DPara
cp postPara3DKeyPoints.pb.* ..
cp postPara3DKeyPoints_pb2.py ../../../..
