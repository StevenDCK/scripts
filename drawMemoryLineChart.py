import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import os
import sys
import numpy as np

pid = '3219'
logFileName = "mem3219.txt"
memUseSet = []
import pdb
#pdb.set_trace()
with open(logFileName, 'r') as lines:
    for line in lines:
        items = line.split()
        if len(items)!=14:continue
        if items[1]!=pid:continue
        memUse = items[10]
        if not memUse.replace(".",'').isdigit():continue
        memUse = float(memUse)
        if memUse<10 or memUse>50:continue
        memUseSet.append(memUse)


plt.ylim(15.5, 25.5)
plt.xlabel('time')
plt.ylabel('memory utize')

# plt.plot(train_acc)
plt.plot(memUseSet, color='blue')

#plt.legend(['{}-train-error'.format(arch), '{}-val-error'.format(arch)])
plt.grid(True)

plt.savefig("mem.jpg", dpi=150)
