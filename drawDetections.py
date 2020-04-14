from __future__ import print_function
import sys
import numpy as np
import cv2
import time
import os.path

g_SrcImagesFileName = '/home1/wiwide_data/train_image/nameSet.txt'
g_SrcImagePath = '/home1/wiwide_data/train_image/JPEGImages/'
g_DetectionsPath = '/home1/wiwide_data/train_image/labels/'
g_DstImagesPath  = '/home4/dbs/Images4Detections/'

g_RightColor = (0, 255, 0)

def _readLines(vTxtFileName):
	Fin = open(vTxtFileName, 'r')            
	Lines = Fin.readlines()  
	Fin.close()
	return Lines

def drawBox(vImage, vLocation):
	BoxColor = g_RightColor		
	SrcWidth = vImage.shape[1]
	SrcHeght = vImage.shape[0]
	xRatio = float(SrcWidth)
	yRatio = float(SrcHeght)
	
	HalfWidth = vLocation[2] * xRatio / 2
	HalfHeght = vLocation[3] * yRatio / 2
	vLocation[0] *= xRatio
	Left = int(0.5+max(0, vLocation[0] - HalfWidth))
	Rigt = int(0.5+min(SrcWidth-1, vLocation[0] + HalfWidth))
	vLocation[1] *= yRatio
	Top  = int(0.5+max(0, vLocation[1]-HalfHeght))
	Bot  = int(0.5+min(SrcHeght-1, vLocation[1]+HalfHeght))
	
	box_thickness = 2	
	cv2.rectangle(vImage, (Left, Top), (Rigt, Bot), BoxColor, box_thickness)

def convert2Array(vStr):
	vStr = vStr.strip()
	FloatTxts = vStr.split()
	FloatSet = []
	for Txt in FloatTxts:
		Txt = Txt.strip(',')
		FloatSet.append(float(Txt))
	return FloatSet
	
def drawDetections(vSrcImageFileName, vDetectionFileName, vDstImageFileName):
	SrcImage = cv2.imread(vSrcImageFileName)	
	TxtDetections = _readLines(vDetectionFileName)
	for TD in TxtDetections:
		Detection = convert2Array(TD)
		if 0 < len(Detection):
			drawBox(SrcImage, Detection[1:])
	cv2.imwrite(vDstImageFileName, SrcImage)
	
def main():
	import pdb
	pdb.set_trace()	
	ImageNames = _readLines(g_SrcImagesFileName)
	i = 0
	for FileName in ImageNames:
		if 0==i%10:
			if i>0:print ('\b\b\b\b\b\b')
			print (str(i), end='')
		FileName = FileName.strip()
		if FileName != "":
			ShortName,ExtName = os.path.splitext(FileName)
			SrcImage = g_SrcImagePath + ShortName + '.jpg'
			DetectionFileName = g_DetectionsPath + ShortName + '.txt'
			DstImageFileName = g_DstImagesPath + ShortName + '.jpg'
			drawDetections(SrcImage, DetectionFileName, DstImageFileName)	
		i = i + 1
	
if __name__ == "__main__":
    sys.exit(main())
