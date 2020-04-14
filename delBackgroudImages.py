import os
import time
import sys
import json
import pdb

srcFileName = str(sys.argv[1])
dstFileName = 'full'+srcFileName
with open(srcFileName, 'r') as load_f:
    load_dict = json.load(load_f)
    pdb.set_trace()
    srcImages = load_dict['images'][::-1]
    dstImages = []
    srcAnnons = load_dict['annotations'][::-1]
    dstAnnons = []
    while len(srcImages)>0 and len(srcAnnons)>0:
        imgId = srcImages[-1]['id']
        annId = srcAnnons[-1]["image_id"]
        if annId<imgId:
            srcAnnons.pop()
        else:
            img = srcImages.pop()
            if annId == imgId:
                dstImages.append(img)
                while len(srcAnnons)>0 and srcAnnons[-1]["image_id"]==imgId:
                    ann = srcAnnons.pop()
                    dstAnnons.append(ann)

    load_dict['annotations'] = dstAnnons
    load_dict['images'] = dstImages

json_fp = open(dstFileName, 'w')
json.dump(load_dict, json_fp, indent=4)
# json_str = json.dumps(json_dict)
# json_fp.write(json_str)
json_fp.close()
