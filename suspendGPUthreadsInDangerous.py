#coding:utf-8
import getpass
import os
import time
import sys
import datetime

g_TimeSleep = 2
g_TemperatureThresh = 80
g_LogFileName = '/home1/tools/results/gpuThreads.txt'
g_SuspendTime = 90

def calculateThreshBaseonTime():
	Hour = datetime.datetime.now().hour
	g_TemperatureThresh = 79
	if Hour<=8 or Hour>=22 :
		g_TemperatureThresh = 82
	return g_TemperatureThresh
	
def getTemperatureSet():
	Fin = open('GpuInfor.txt', 'r')
	Lines = Fin.readlines()
	Fin.close()
	TemperatureSet = []
	Max = 0
	for i in range(len(Lines)):
		data = Lines[i].split()
		if 10<len(data):
			Temp = int(data[2][:-1])
			TemperatureSet.append(Temp)
			if Temp>Max: Max = Temp
		else: break			
	return TemperatureSet, Max

def getMyGpuThreads():
	Fin = open('GpuInfor.txt', 'r')
	Lines = Fin.readlines()
	Fin.close()
	GPUPIDs = []
	for l in Lines:
		data = l.split()
		if 7 ==len(data):
			GPUPIDs.append([int(data[1]), data[2],data[4]])
	return GPUPIDs
	

def killThreadIfEmergency(vGpuPIDs, vTemperatures, vFout):
	PidSet = [g_SuspendTime]
	for GpuPID in vGpuPIDs:
		GPU = GpuPID[0]
		if vTemperatures[GPU] > g_TemperatureThresh:
			PID = str(GpuPID[1])
			PName = GpuPID[2]
			os.system('kill -stop '+PID)
			vFout.write(str(datetime.datetime.now())+'\n')
			vFout.write(PName+'(pid:' + PID + ') has been suspend with GPU ' + str(GPU) + ' bing ' +str(vTemperatures[GPU]) +'C. \n')
			PidSet.append(int(PID))
	if 1 < len(PidSet):
		vFout.write('\n')
	return PidSet

def awakeThreads(vPidCache, vSleepTime, vFout):
	PidCache = []
	for PidSet in vPidCache:
		PidSet[0] -= vSleepTime
		if PidSet[0] <= 0:
			for Pid in PidSet[1:]:
				os.system('kill -cont '+str(Pid))
				vFout.write('Thread('+str(Pid)+') has been awaken.\n')
		else: PidCache.append(PidSet)
	if len(PidCache) < len(vPidCache):
		vFout.write('\n')
	return PidCache

if __name__=="__main__":
	import pdb
	#pdb.set_trace()
	FOut = open(g_LogFileName, 'a')
	FOut.write('GPU threads killer with time step = ' + str(g_TimeSleep) + ' and temperatureThresh = ' + str(g_TemperatureThresh) + '.\n')
	FOut.close()
	PidCache = []
	while 1:	
		#g_TemperatureThresh = calculateThreshBaseonTime()
		os.system('nvidia-smi | grep MiB > GpuInfor.txt')
		TemperatureSet,Max = getTemperatureSet()
		GpuPidSet = getMyGpuThreads()
		if Max > g_TemperatureThresh: 
			FOut = open(g_LogFileName, 'a')
			PidSet = killThreadIfEmergency(GpuPidSet, TemperatureSet, FOut)
			FOut.close()
			PidCache.append(PidSet)
		g_TimeSleep = int(1 + max(0, g_TemperatureThresh-Max) * 0.5)
		time.sleep(g_TimeSleep)	
		if 0 < len(PidCache):
			FOut = open(g_LogFileName, 'a')
			PidCache = awakeThreads(PidCache, g_TimeSleep, FOut)
			FOut.close()
	
#ps -ef |grep python  