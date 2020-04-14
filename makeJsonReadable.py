import os
import time
import sys
import json
import pdb
#pdb.set_trace()
srcFileName = str(sys.argv[1])
dstFileName = '0'+srcFileName
with open(srcFileName, 'r') as load_f:
    load_dict = json.load(load_f)
json_fp = open(dstFileName, 'w')
json.dump(load_dict, json_fp, indent=4)
# json_str = json.dumps(json_dict)
# json_fp.write(json_str)
json_fp.close()
