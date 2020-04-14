#coding:utf-8
import getpass
import os
import time
import sys
import datetime
import time

while 1:
	with open("/sys/devices/gpu.0/load", 'r') as gpuFile:
		fileData = gpuFile.read()
	# The GPU load is stored as a percentage * 10, e.g 256 = 25.6%
	usage = int(fileData) / 10
	print (usage)
	time.sleep(0.2)