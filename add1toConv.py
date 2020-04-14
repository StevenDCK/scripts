# -*- coding:utf8 -*-
import os
import pdb
#pdb.set_trace()

g_SrcNameSet = 'ssdfls2x.prototxt'
g_DstNameSet = 'ssdfls2x.prototxt1'

def _add1(s):
	i = s.find('conv')
	if 0 > i : return  s
	i += len('conv')
	i0 = s[i]
	if not i0.isdigit(): return s
	i0 = int(i0)
	i1 = s[i+1]
	post = s[i+1:]
	if i1.isdigit():
		i0 = int(s[i:i+2])
		post = s[i + 2:]
	i0 += 1
	return s[0:i] + str(i0) + post

if __name__ == "__main__":
	Fin = open(g_SrcNameSet,'r')
	srcs = Fin.readlines()
	Fin.close()
	Fout = open(g_DstNameSet, 'w')
	for i in range(len(srcs)):
		s = _add1(srcs[i])
		Fout.write(s)
	Fout.close()