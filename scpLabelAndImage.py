# -*- coding:utf8 -*-
import os
import pdb
import re
import xlwt
from openpyxl import Workbook
#pdb.set_trace()

g_NameSet = '/home1/wiwide_data/OID/person_voc/l1c.txt'
g_SrcLabelPath = '/home1/wiwide_data/OID/person_voc/l1/'
g_SrcImagePath = '/home1/wiwide_data/OID/person_voc/JPEGImages/'
g_DstLabelPath = '/home1/wiwide_data/voc/labels/'
g_DstImagePath = '/home1/wiwide_data/voc/JPEGImages'


	
if __name__=="__main__":
	Fin = open(g_NameSet,'r')
	Files = Fin.readlines()
	Fin.close()
	i = 0
	for f in Files:
		if 3>len(f):continue
		f = f.split('.')[0]
		Image = f + '.jpg'
		Label = f + '.txt'
		os.system('scp ' + g_SrcImagePath+Image + ' dbs@172.16.105.173:'+g_DstImagePath)
		os.system('scp ' + g_SrcLabelPath+Label + ' dbs@172.16.105.173:'+g_DstLabelPath)	
		os.system('echo ' + str(i) + ' >> scplog.txt')
		i = i+1