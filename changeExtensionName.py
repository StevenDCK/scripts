# -*- coding:utf8 -*-
import os
import pdb
#pdb.set_trace()

g_Path = 'src/'


	
if __name__ == "__main__":
	os.system('ls ' + g_Path +'*.c >tt')
	Fin = open('tt','r')
	Files = Fin.readlines()
	Fin.close()
	for i in range(len(Files)):
		f = g_Path + Files[i][0:-1]
		os.system('mv ' + f + ' ' + f +'pp')
