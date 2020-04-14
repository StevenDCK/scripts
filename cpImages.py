# -*- coding:utf8 -*-
import os
import pdb
#pdb.set_trace()

g_NameSet = '000.txt'
g_SrcImagePath = 'JPEGImages/'
g_DstImagePath = 'trainImages000/'


	
if __name__=="__main__":
	Fin = open(g_NameSet, 'r')
	Files = Fin.readlines()
	Fin.close()
	i = 0
	cmd = 'cp '
	for f in Files:
		i = i+1		
		#if i<10752:continue
		f = f[0:-1]
		cmd +=  g_SrcImagePath+f + ' '
		if 0==(i&511): os.system('echo ' + str(i) + ' >> cplog.txt')		
		if 0==(i&127):
			cmd += g_DstImagePath
			os.system(cmd)
			cmd = 'cp '
	if 'cp ' != cmd:
		cmd += g_DstImagePath
		os.system(cmd)

