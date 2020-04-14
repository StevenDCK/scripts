# -*- coding:utf8 -*-
import os
import sys
import pdb
#pdb.set_trace()
#import getpass
#author = getpass.getuser()
if __name__ == "__main__":
	if sys.argv < 4 :
		print ('repaceString input parameter too few')
	else:
		src = str(sys.argv[1])
		dst = str(sys.argv[2])
		fileName = str(sys.argv[3])
		os.system("sed -i 's/"+src + "/"+dst+"/g' " + fileName)