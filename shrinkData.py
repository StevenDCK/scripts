# -*- coding:utf8 -*-
import os
import pdb
#pdb.set_trace()

g_SrcData = '/home/dbs/f/widerface/WIDER_val0.txt'
g_DstData = '/home/dbs/f/widerface/WIDER_val.txt'


	
if __name__ == "__main__":
	Fin = open(g_SrcData,'r')
	Files = Fin.readlines()
	Fin.close()
	Fout = open(g_DstData, 'w')
	for i in range(len(Files)):
		if 0 != i%6: continue
		f = Files[i]
		Fout.write(f)
	Fout.close()