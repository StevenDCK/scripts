from __future__ import print_function
import sys
#import numpy as np
import cv2
import time
import os.path

g_SrcImagesFileName = '/home1/wiwide_data/train_image/nameSet.txt'
g_SrcImagePath = '/home4/dbs/Images4Detections/'
g_SrcImagesFileName = 'D:/test/a.txt'
g_SrcImagePath = 'D:/test/'

def _readLines(vTxtFileName):
	Fin = open(vTxtFileName, 'r')            
	Lines = Fin.readlines()  
	Fin.close()
	return Lines


	
def main():
	import pdb
	#pdb.set_trace()	
	ImageNames = _readLines(g_SrcImagesFileName)
	i = 0
	cv2.namedWindow("Image") 	
	for FileName in ImageNames:
		FileName = FileName.strip()
		if FileName != "":
			ShortName,ExtName = os.path.splitext(FileName)
			SrcImage = g_SrcImagePath + ShortName + '.jpg'
			img = cv2.imread(SrcImage)   
			cv2.imshow("Image", img)   
			key = cv2.waitKey(0)  		
		i = i + 1
	cv2.destroyAllWindows()
	
	
if __name__ == "__main__":
    sys.exit(main())
