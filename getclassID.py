# -*- coding:utf8 -*-
import os
import pdb
pdb.set_trace()

g_SrcNameSet = '6'
g_DstNameSet = 'exclasses'
#g_Path = '/home1/wiwide_data/train_image/person/JPEGImages/'


	
if __name__ == "__main__":
	Fin = open(g_SrcNameSet,'r')
	Files = Fin.readlines()
	Fin.close()
	Fout = open(g_DstNameSet, 'w')
	for i in range(len(Files)):
		s = Files[i][0:-1]
		if len(s)==0:continue
		id = int(s)
		if id==0 or id == 2:Fout.write(str(i)+'\n')
	Fout.close()