# -*- coding:utf8 -*-
import os
import pdb
pdb.set_trace()

g_NameSet = 'trainPerson.txt'
g_SrcImagePath = '/home4/dbs/Images4DetectionsResized/'
g_DstImagePath = 'images/'


	
if __name__=="__main__":
	Fin = open(g_NameSet,'r')
	Files = Fin.readlines()
	Fin.close()
	i = 0
	for f in Files:
		i = i+1	
		if i<77120:continue
		Image = os.path.split(f)[1]
		#if 3>len(f):continue
		Image = Image[0:-1]
		if os.path.exists(g_DstImagePath+Image):continue
		cmd = 'scp '  + ' dbs@172.16.105.172:'+g_SrcImagePath+Image + ' ' + g_DstImagePath
		os.system(cmd)
		if 0==(i&127): os.system('echo ' + str(i) + ' >> scplog.txt')