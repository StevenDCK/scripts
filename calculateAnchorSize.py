import os

Fin = open('anchors.txt','r')
Line = Fin.readline()
Fin.close()

data = Line.split(',')
NOSet=[]
for d in data:
	NOSet.append(float(d))

Scales = [8,16,32]
for iAnchor in range(3):
	for iNO in range(6):
		NOSet[iAnchor*6+iNO] *= Scales[iAnchor] 
	
SizeSet = []
for NO in NOSet:
	SizeSet.append(int(0.5+NO))
	

Fout = open('AnchorResult.txt','w')
for Size in SizeSet:
	Fout.write(str(Size)+', ')

Fout.close()