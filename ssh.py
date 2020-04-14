#coding:utf-8
import getpass
import os
import time
import sys
import datetime
import pdb
#pdb.set_trace()
for ip in range(120, 255):
	os.system("ssh nvidia@172.16.105."+str(ip)+' &')