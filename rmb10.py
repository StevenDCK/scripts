import pdb
import re
pdb.set_trace()
value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')

InputFileName = "mb1138.txt"
OutputFileName= "mb11380.txt"
fin = open(InputFileName, "r")
lines = fin.readlines()
fin.close()
fout = open(OutputFileName,"w")
i = 0
nold=-1
for line in lines:
	data = line.split()
	if len(data)>2 and value.match(data[2]) and float(data[2])<20 and float(data[2])>1:
		NFlag = data[0].split(':')
		if len(NFlag)>1 and NFlag[0].isdigit():
			Num = int(NFlag[0])
			if nold<Num:
				nold = Num
				fout.write(line)
	else:
		print i,line
	i = i+1
fout.close()
