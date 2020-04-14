#!/bin/bash
cd /home/dbs/pet
CUDA_VISIBLE_DEVICES=1,2,3,4,5,6,7 python3 tools/ssd/test_net.py --cfg cfgs/ssd/mscoco_humanparts/mobilenet_v1/ssd_MV1-0.25-64HEAD-FL_540x960_s2x_RetinaFace.yaml

