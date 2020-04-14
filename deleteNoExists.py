# -*- coding:utf8 -*-
import os
import pdb
#pdb.set_trace()

g_SrcFileName = '/home1/wiwide_data/train_image/oriTrainPerson.txt'
g_DstFileName = '/home1/wiwide_data/train_image/trainPerson.txt'
	
if __name__=="__main__":
	Fin = open(g_SrcFileName,'r')
	Files = Fin.readlines()
	Fin.close()
	Fout = open(g_DstFileName,'w')
	for f in Files:
		l = f[0:-1]
		if os.path.exists(l):
			Fout.write(f)
	Fout.close()