import os
import time
import sys
import json
import pdb
#pdb.set_trace()
srcFileName = str(sys.argv[1])
sumPos = 0
sumNeg = 0
numPos = 0
numNeg = 0
maxRatio = 0
with open(srcFileName, 'r') as load_f:
    load_dict = json.load(load_f)
    anns = load_dict['annotations']
    for ann in anns:
        clsId = ann['category_id']
        if clsId == 1:
            bbox = ann['bbox']
            ratio = float(bbox[2])/bbox[3]
            if ratio>=1 :
                sumPos += ratio
                numPos += 1
            else:
                ratio = 1/ratio
                sumNeg += ratio
                numNeg +=1
            if ratio>maxRatio:
                maxRatio = ratio
print("all: ", numNeg+numPos, (sumNeg+sumPos)/(numNeg+numPos), maxRatio)
print("w>h: ", numPos, sumPos/numPos)
print("w<h: ", numNeg, sumNeg/numNeg)

