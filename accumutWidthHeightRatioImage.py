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
    images = load_dict['"images"']
    for img in images:
        width = img["width"]
        height = img['height']
        ratio = float(width)/height
        sumPos += ratio
        numPos += 1

        if ratio>maxRatio:
            maxRatio = ratio
print("all: ", numNeg+numPos, (sumNeg+sumPos)/(numNeg+numPos), maxRatio)
#print("w>h: ", numPos, sumPos/numPos)
#print("w<h: ", numNeg, sumNeg/numNeg)

