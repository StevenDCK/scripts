#coding:utf-8
import os
import time
import sys
import datetime
import pdb
#pdb.set_trace()
g_rootPath = str(sys.argv[1])
g_dstPath = str(sys.argv[2])

def getTogether(vRootPath):
    for rootPath,subPaths,files in os.walk(vRootPath):
        for f in files:
            os.system('mv '+rootPath+'/' + f + " " + g_dstPath)
        for s in subPaths:
            getTogether(rootPath+'/'+s)

getTogether(g_rootPath)