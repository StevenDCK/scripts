import time
import sys
import numpy as np


for i in range(1):
    fileName = 'testPostDetection_'+str(i) +".npz"
    ds = np.load(fileName)
    for k in range(len(ds.items())):
        src = ds['arr_'+str(k)]
        for i in range(len(src)):
            src[i,3] /= 1280
            src[i,4] /= 720
            src[i,5] /= 1280
            src[i,6] /= 720
        #ds['arr_' + str(k)] = src
    np.savez(fileName+1, ds)
