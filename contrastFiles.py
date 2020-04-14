# -*- coding:utf8 -*-
import os
import pdb
#pdb.set_trace()

g_0path = '/home1/wiwide_data/0txtDetections4supermarketimages/'
g_1path = '/home1/wiwide_data/txtDetections4supermarketimages/'
g_namesFile = '/home1/wiwide_data/persons.txt'
g_DstNameSet='error.txt'
	
if __name__ == "__main__":
	Fin = open(g_namesFile,'r')
	Files = Fin.readlines()
	Fin.close()
	Fout = open(g_DstNameSet, 'w')
	for i in range(len(Files)):
		if 0==i%100:print i
		f = Files[i][0:-1]
		f0= g_0path+f
		f1= g_1path+f
		F0in=open(f0, 'r')
		F1in=open(f1,'r')
		l0s=F0in.readlines()
		l1s=F1in.readlines()
		num = 0
		for k in range(len(l0s)):
			if len(l0s[k].strip())==0 : continue
			if l0s[k] != l1s[k]:
				print f
				print l0s[k]
				print l1s[k]
				num += 1
		if len(l1s)>len(l0s):
			print f
			print len(l1s),f1
			print len(l0s),f0
			num += 1
		if num>0:Fout.write(f+'\n')
	Fout.close()