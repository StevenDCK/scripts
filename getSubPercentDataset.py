import os
import time
import sys
import json
import pdb
pdb.set_trace()
srcFileName = str(sys.argv[1])
indexDistance = int(sys.argv[2])
dstFileName = 'sub'+srcFileName
with open(srcFileName, 'r') as load_f:
    load_dict = json.load(load_f)
    srcImgs = load_dict['images']
    dstImgs = []
    srcAnns = load_dict['annotations']
    dstAnns = []
    srcAnns.reverse()
    for i in range(0, len(srcImgs), indexDistance):
        sImg = srcImgs[i]
        imgId = sImg['id']
        dstImgs.append(sImg)
        while len(srcAnns)>0 and srcAnns[-1]["image_id"] <= imgId:
            back = srcAnns.pop()
            if back["image_id"] == imgId: dstAnns.append(back)

    load_dict['images'] = dstImgs
    load_dict['annotations'] = dstAnns
json_fp = open(dstFileName, 'w')
json.dump(load_dict, json_fp, indent=4)
# json_str = json.dumps(json_dict)
# json_fp.write(json_str)
json_fp.close()
