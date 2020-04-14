# -*- coding:utf8 -*-
import os
import pdb
pdb.set_trace()

g_SrcNameSet = '/home1/wiwide_data/train_image/tf'
g_DstNameSet = '/home1/wiwide_data/train_image/trainPerson_filtered.txt'
g_Path = '/home1/wiwide_data/train_image/person/JPEGImages/'


	
if __name__ == "__main__":
	Fin = open(g_SrcNameSet,'r')
	Files = Fin.readlines()
	Fin.close()
	Fout = open(g_DstNameSet, 'w')
	for i in range(len(Files)):
		f = Files[i]
		f = g_Path + f
		Fout.write(f)
	Fout.close()