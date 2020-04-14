import os
import time
import sys
import json
import pdb
pdb.set_trace()
srcFileName = str(sys.argv[1])
dstImageNum = int(sys.argv[2])
dstFileName = 'sub'+srcFileName
with open(srcFileName, 'r') as load_f:
    load_dict = json.load(load_f)
    image_id = load_dict['images'][dstImageNum]['id']
    load_dict['images'] = load_dict['images'][0:dstImageNum]
    for i in range(len(load_dict['annotations'])):
        if image_id==load_dict['annotations'][i]["image_id"]:
            break
    load_dict['annotations'] = load_dict['annotations'][0:i]
json_fp = open(dstFileName, 'w')
json.dump(load_dict, json_fp, indent=4)
# json_str = json.dumps(json_dict)
# json_fp.write(json_str)
json_fp.close()
