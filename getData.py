from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import datetime
import xlwt
import pdb
import os

g_StartTime = "2018-07-16 07:04:50"
g_StopTime  = "2018-07-16 20:46:00"
g_1MacAddress = "00:1F:7A:40:80:20"
#g_1MacAddress = "00:1F:7A:40:7F:30"
#g_2MacAddress = "00:1F:7A:40:73:E0"
g_2MacAddress = "00:1F:7A:40:74:D0"
g_WorkDirctory='h:\\'


def updateValue(vDriver, vID, vValue):
	vDriver.find_element_by_id(vID).send_keys(Keys.CONTROL,'a') 
	vDriver.find_element_by_id(vID).send_keys(Keys.CONTROL,'x') 
	vDriver.find_element_by_id(vID).send_keys(vValue)

def calculateHours():
	Now = datetime.datetime.now()
	StartTime =  datetime.datetime.strptime(g_StartTime, '%Y-%m-%d %H:%M:%S')
	TimeSpan = Now - StartTime
	return (TimeSpan.days*24+TimeSpan.seconds/3600 + 1)
	
def getApData(vDriver, vMacAddress):
	updateValue(vDriver, "devmac", vMacAddress)
	WorkMode = driver.find_element_by_id("devmodeselectid")
	Select(WorkMode).select_by_value('2')
	Hours = calculateHours()
	updateValue(driver, "latesthour", Hours)
	updateValue(driver, "showcount", 100*Hours)
	driver.find_element_by_id("btnsearch").click()
	InOutTime = driver.find_elements_by_tag_name("td");
	InTimeSet = InOutTime[2].text.split('\n')
	OutTimeSt = InOutTime[3].text.split('\n')
	return InTimeSet, OutTimeSt
	
	
def save2txt(vMacAddress, vTimeSet, vFileName):
	Fout = open(vFileName, 'w')
	Fout.write(vMacAddress+'\n')
	for Time in vTimeSet:
		if Time >= g_StartTime and Time <= g_StopTime :
			Fout.write(Time+'\n')
	Fout.close()
	
def getFilePrefix():
	StopTime = g_StopTime.split(' ')[0].split('-')
	MonthDay = StopTime[1]+StopTime[2]
	return g_WorkDirctory+'data\\'+MonthDay
	
def txt2excel(vTxtFileName, vExcelTable):
	Fin = open(vTxtFileName,'r')
	Lines = Fin.readlines()
	Fin.close()
	for i in range(len(Lines)):
		t1t2 = Lines[i].split(',')
		if len(t1t2) == 2:
			t1 = t1t2[0].replace(',', '')
			vExcelTable.write(i,0, t1)
			vExcelTable.write(i,1,t1t2[1])


#pdb.set_trace()	
driver =webdriver.Chrome()
driver.get("http://54.223.138.145/statistics")
FilePrefix = getFilePrefix()
In,Out = getApData(driver, g_1MacAddress)
save2txt(g_1MacAddress, In, FilePrefix+"In.txt")
save2txt(g_1MacAddress, Out, FilePrefix+"Out.txt")

In,Out = getApData(driver, g_2MacAddress)
save2txt(g_2MacAddress, In, FilePrefix+"In1.txt")
save2txt(g_2MacAddress, Out, FilePrefix+"Out1.txt")

os.system(g_WorkDirctory+'correspond.lnk ' + FilePrefix+"In.txt")
os.system(g_WorkDirctory+'correspond.lnk ' + FilePrefix+"Out.txt")


Excel = xlwt.Workbook(encoding = 'ascii')
TIn = Excel.add_sheet('In')
TOut= Excel.add_sheet('Out')
txt2excel(FilePrefix+'In-corresponded.txt', TIn)
txt2excel(FilePrefix+'Out-corresponded.txt', TOut)
Excel.save(FilePrefix+'InOut-corresponded.xls')

#driver.quit()



