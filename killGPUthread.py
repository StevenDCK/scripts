#coding:utf-8
import getpass
import os
import time
import sys
import datetime
import pdb
#pdb.set_trace()
processKey = str(sys.argv[1])
logFileName = os.environ['HOME'] + "/gpuTemp.txt"
os.system("ps -ef | grep " + processKey + " > " + logFileName)
Fin =open(logFileName)
lins = Fin.readlines()
for line in lins:
	if 'grep' not in line:
		infor = line.split()
		pid = int(infor[1])
		os.system("kill -9 "+str(pid))