# -*- coding:utf8 -*-
import os
import pdb
#pdb.set_trace()

g_SrcFileName = '/home4/dbs/testvoc.txt'
g_DstFileName = '/home4/dbs/testvoc1.txt'
	
if __name__=="__main__":
	Fin = open(g_SrcFileName,'r')
	Files = Fin.readlines()
	Fin.close()
	Fout = open(g_DstFileName,'w')
	for f in Files:
		l = f.replace('JPEGImages', 'labels')
		l = l[0:-4]+'txt'
		if os.path.getsize(l) > 0:		
			Fout.write(f)
	Fout.close()