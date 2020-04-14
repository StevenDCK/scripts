# -*- coding:utf8 -*-
import ctypes
import cv2
import math
import numpy as np

import os
import pdb
#pdb.set_trace()


ll = ctypes.cdll.LoadLibrary
lib = ll("cpppython.so")
lib.test.restype = ctypes.c_float
frame = cv2.imread('~/test.jpg')
frame_data = np.asarray(frame, dtype=np.uint8)
res = np.asarray([1, 2, 3], dtype=np.float32)
pframe_data = frame_data.ctypes.data_as(ctypes.c_char_p)
rData = res.ctypes.data_as(ctypes.c_void_p)

print(res)
print(frame_data.sum(), frame_data.sum(0))
value = lib.test(frame.shape[0], frame.shape[1], pframe_data, rData)
print ("lib.test:\n", value)
print(res)


