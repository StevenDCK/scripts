# -*- coding:utf8 -*-
import os
import pdb
#pdb.set_trace()

g_SrcFileName = '/home4/dbs/tt'
g_DstFileName = '/home4/dbs/tt0size'
g_FilePath = '/home4/dbs/trainImages/'
	
if __name__=="__main__":
	Fin = open(g_SrcFileName,'r')
	Files = Fin.readlines()
	Fin.close()
	Fout = open(g_DstFileName,'w')
	for f in Files:
		#l = f.replace('JPEGImages', 'labels')
		l = g_FilePath+f[0:-1]
		if os.path.getsize(l) == 0:		
			Fout.write(f)
	Fout.close()