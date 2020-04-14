# -*- coding:utf8 -*-
import os
import pdb
#pdb.set_trace()

g_NameSet = 'testPerson.txt'
g_SrcImagePath = '/home1/wiwide_data/train_image/person/JPEGImages'
g_DstImagePath = '/home1/wiwide_data/train_image/person/JPEGImages/'


	
if __name__=="__main__":
	Fin = open(g_NameSet,'r')
	Files = Fin.readlines()
	Fin.close()
	i = 0
	for f in Files:
		i = i+1		
		#if 3>len(f):continue
		f = f[0:-1]
		if os.path.exists(f):continue
		cmd = 'scp '  + ' dbs@172.16.105.172:'+f + ' ' + g_DstImagePath
		os.system(cmd)
		if 0==(i&127): os.system('echo ' + str(i) + ' >> scplogtest.txt')