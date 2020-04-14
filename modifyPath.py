import pdb
import re
import sys
pdb.set_trace()

FileName = sys.argv[1]
fin = open(FileName, "r")
lines = fin.readlines()
fin.close()
fout = open(FileName, "w")

for l in lines:
	l = l.replace("/home/lzhpc/ydw", "/home1/home_lzhpc")
	fout.write(l)	
	
fout.close()
