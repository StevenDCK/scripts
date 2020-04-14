# -*- coding:utf8 -*-
import os
import pdb
#pdb.set_trace()

file_dir = '/home/nvidia/maxjpgs/'
maxJpgs = '/home/nvidia/maxjpgs'
for root, dirs, files in os.walk(file_dir):
		for i in range(1, len(files)):
			if files[i-1][0:3] != files[i][0:3] or i+1 == len(files):
				os.system("cp " + file_dir+"'"+files[i-1] + "' "+ maxJpgs)