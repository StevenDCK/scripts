from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import datetime
import xlwt
import pdb
import os

g_StartTime = "2018-07-12 12:04:50"
g_StopTime  = "2018-07-12 18:46:00"
g_1MacAddress = "00:1F:7A:40:80:20"
#g_1MacAddress = "00:1F:7A:40:7F:30"
#g_2MacAddress = "00:1F:7A:40:73:E0"
g_2MacAddress = "00:1F:7A:40:74:D0"
g_WorkDirctory='h:\\'

g_Driver = webdriver.Chrome()

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
	
def startChome():
	g_Driver.get("http://fang.vanke.com")
	g_Driver.find_element_by_id('Telphone').send_keys('13008198539')
	g_Driver.find_element_by_id('Password').send_keys('123456')

#pdb.set_trace()	

def mainPage():
	g_Driver.get("http://fang.vanke.com/ActivityTarget/Index/17269?site=0")
	Fin = open("candidates.txt","r") 
	lines = Fin.readlines()
	Fin.close()
	for l in lines:
		l = l.strip()
		if 2<len(l):
			updateValue(g_Driver, 'Num', l)
			#g_Driver.find_element_by_id('Num').send_keys(l)
			g_Driver.find_element_by_id('btn_search').click()
			Option = input("n:")
			if 0 == Option:
				break
			
	
	
startChome()	
for i in range(1000):
	Option = input('Choice: \n1:Start Chrome. \n2:main     \n')
	if 1 == Option:
		startChome()
	elif 2==Option:
		mainPage()



#driver.quit()



