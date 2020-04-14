# -*- coding:utf8 -*-
import os
import pdb
import re
import xlwt
from openpyxl import Workbook
#pdb.set_trace()

	
if __name__=="__main__":
	Fin = open('/home1/wiwide_data/OID/person_voc/tt.txt','r')
	Files = Fin.readlines()
	Fin.close()
	Fout = open('/home1/wiwide_data/OID/person_voc/personAll.txt','w')
	for f in Files:
		Fout.write(f)
		Fout.writelines(open('/home1/wiwide_data/OID/person_voc/l1/'+f.strip(),'r').readlines())
	Fout.close()