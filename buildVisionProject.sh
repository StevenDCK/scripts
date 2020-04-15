#!/bin/bash
echo "cloning......"
git clone -b tensorRT git@172.16.105.143:WAR/VisionProject.git #-q
cd VisionProject 

cd framework/tensorrt_framework/cppCommon
mkdir lib 
mkdir build 
cd build 
cmake ../src/Common/ 
make -j2

cd ../../tensorrtFrmame/
mkdir build 
cd build 
cmake .. 
make -j2 

echo "fh_tracking buiding......"
cd ../../../../source/modules/fh_tracking/
sh gcc.sh
echo "Finished!"
cd ../../..

