from __future__ import print_function
from xml.etree import ElementTree as ET
import sys
import numpy as np
import cv2
import time
import os.path

g_SrcImagesFileName = '/home1/wiwide_data/supermarketImages_person.txt'
g_LabelClassFileName = '/home4/dbs/mycfg/personClassLabel.txt'
g_DetectionsPath = '/home1/wiwide_data/txtDetections4supermarketimages/'
g_DstXMLsPath  = '/home1/wiwide_data/xmlDetections4supermarketimages/'

g_Templet = '''
<annotation>
	<folder>JPEGImages</folder>
	<filename>pic_Z4RYDR8G_1518019046_1524.jpg</filename>
	<path>mypath</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>1024</width>
		<height>512</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>person_s</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>141</xmin>
			<ymin>79</ymin>
			<xmax>230</xmax>
			<ymax>152</ymax>
		</bndbox>
	</object>
</annotation>
'''

g_LabelClassSet = []
g_TempXmlFileName = 'templet.xml'
def _readLines(vTxtFileName):
	Fin = open(vTxtFileName, 'r')            
	Lines = Fin.readlines()  
	Fin.close()
	return Lines


def convert2Array(vStr):
	vStr = vStr.strip()
	FloatTxts = vStr.split()
	FloatSet = []
	for Txt in FloatTxts:
		Txt = Txt.strip(',')
		FloatSet.append(float(Txt))
	return FloatSet

def _getClassName(vClassIndex, vXmlObj):	
	vXmlObj.find('name').text = g_LabelClassSet[vClassIndex]

def _updateXmlSizeElement(voXmlSize, vHeightWidthChanel):
	voXmlSize.find('width').text = str(vHeightWidthChanel[1])
	voXmlSize.find('height').text = str(vHeightWidthChanel[0])
	voXmlSize.find('depth').text = str(vHeightWidthChanel[2])
	
def _getRealSize(vHeightWidth, vLocation, voBndbox):
	xRatio = float(vHeightWidth[1])
	yRatio = float(vHeightWidth[0])	
	HalfWidth = vLocation[2] * xRatio / 2
	HalfHeght = vLocation[3] * yRatio / 2
	vLocation[0] *= xRatio
	Left = int(0.5+max(0, vLocation[0] - HalfWidth))
	Rigt = int(0.5+min(xRatio-1, vLocation[0] + HalfWidth))
	vLocation[1] *= yRatio
	Top  = int(0.5+max(0, vLocation[1]-HalfHeght))
	Bot  = int(0.5+min(yRatio-1, vLocation[1]+HalfHeght))
	voBndbox.find('xmin').text = str(Left)
	voBndbox.find('ymin').text = str(Top)
	voBndbox.find('xmax').text = str(Rigt)
	voBndbox.find('ymax').text = str(Bot)

def _convertTxt2Xml(vSrcImageFileName, vDetectionFileName, vDstXmlFileName):
	SrcImage = cv2.imread(vSrcImageFileName)
	HeightWidthChanel=SrcImage.shape
	XMLTree = ET.parse(g_TempXmlFileName)
	Annotation = XMLTree.getroot()
	Annotation.find('filename').text = os.path.basename(vSrcImageFileName)
	_updateXmlSizeElement(Annotation.find('size'), HeightWidthChanel)	
	ObjectTemplet = Annotation.find('object')
	Annotation.remove(ObjectTemplet)
	TxtDetections = _readLines(vDetectionFileName)
	for TD in TxtDetections:
		Detection = convert2Array(TD)
		if 0 < len(Detection):
			_getClassName(int(Detection[0]), ObjectTemplet)
			_getRealSize(HeightWidthChanel[0:2], Detection[1:5], ObjectTemplet.find('bndbox'))
			Annotation.append(ObjectTemplet)
	XMLTree.write(vDstXmlFileName)
	
def main():
	import pdb
	#pdb.set_trace()	
	Fout = open(g_TempXmlFileName, 'w')
	Fout.write(g_Templet)
	Fout.close()
	ImageNames = _readLines(g_SrcImagesFileName)
	i = 0
	ClassLabelSet = _readLines(g_LabelClassFileName)
	for ClassLabel in ClassLabelSet:
		ClassLabel = ClassLabel.strip()
		if 3 < len(ClassLabel):
			Name = ClassLabel.split(',')[1]
			g_LabelClassSet.append(Name)
	for FileName in ImageNames:
		#FileName = ImageNames[697]
		if 0==i%10:
			if i>0:print ('\b\b\b\b\b\b')
			print (str(i), end='')
		FileName = FileName.strip()
		if FileName != "":
			SrcImage = FileName 
			FileName = os.path.basename(FileName)
			ShortName,ExtName = os.path.splitext(FileName)
			FileName = ShortName+".txt"
			DetectionFileName = g_DetectionsPath+FileName
			DstXmlFileName = g_DstXMLsPath + ShortName+'.xml'
			_convertTxt2Xml(SrcImage, DetectionFileName, DstXmlFileName)
		i = i + 1
	
if __name__ == "__main__":
    sys.exit(main())
	