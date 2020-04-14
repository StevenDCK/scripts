# -*- coding:utf8 -*-
import os
import pdb
#pdb.set_trace()

def getIndex(vName):
    for i in range(len(vName)):
        if vName[i] == '(' or vName[i]=='（':
            return i
    return 0


def getName(vName):
    i = getIndex(vName)
    return vName[0:i]
    

srcDir = 'wiwide_nature/'
dstDir = 'wiwide3/'
for root, dirs, files in os.walk(srcDir):
		for i in range(len(files):
			filename, extension= os.path.splitext(files[i])
			newName = getName(filename)+'_'+srcDir[:-1]+extension
			os.system("cp " + srcDir+"'"+files[i-1] + "' "+ dstDir+newName)