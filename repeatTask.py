#coding:utf-8
import time
import sys
import os

g_CMD = 'nohup /home/dbs/darknetwwd/darknet/darknet detector train /home4/dbs/mycfg/voc.data  /home4/dbs/mycfg/yolov3_voc_person_train.cfg -gpus 2,3,4,5,6,7 /home4/dbs/MODELvoc/yolov3_voc_person_train.backup -savestep 1000 2>> /home4/dbs/logfile/train/yolo3voc.txt'
g_CMD = 'nohup /home/dbs/darknetwwd/darknet/darknet detector train /home4/dbs/mycfg/person.data  /home4/dbs/mycfg/y3person_train.cfg -gpus 1,2,3,4,5,6,7 /home4/dbs/person_model/y3person_train.backup -savestep 5000 2>> /home4/dbs/logfile/train/y3person.txt '
g_PauseTime = 120

if __name__=="__main__":
	time.sleep(800)	
	os.system(' python deleteNoExists.py')
	os.system(g_CMD)
	time.sleep(g_PauseTime)	
