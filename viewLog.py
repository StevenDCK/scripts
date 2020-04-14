from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import datetime
import xlwt
import pdb
import os

g_Hours = 4
g_1MacAddress = "00:1F:7A:40:73:E0"

def updateValue(vDriver, vID, vValue):
	vDriver.find_element_by_id(vID).send_keys(Keys.CONTROL,'a') 
	vDriver.find_element_by_id(vID).send_keys(Keys.CONTROL,'x') 
	vDriver.find_element_by_id(vID).send_keys(vValue)

	
def getApData(vDriver, vMacAddress, vFlag):
	if vFlag == 0 : updateValue(vDriver, "devmac", vMacAddress)
	WorkMode = vDriver.find_element_by_id("devmodeselectid")
	if vFlag == 0 : Select(WorkMode).select_by_value('2')
	Hours = g_Hours
	if vFlag == 0 : updateValue(vDriver, "latesthour", Hours)
	if vFlag == 0 : updateValue(vDriver, "showcount", 100*Hours)
	vDriver.find_element_by_id("btnsearch").click()
	InOutTime = vDriver.find_elements_by_tag_name("td");
	InTimeSet = InOutTime[2].text.split('\n')
	OutTimeSt = InOutTime[3].text.split('\n')
	print 'In:'+str(len(InTimeSet)), 'out:'+str(len(OutTimeSt))
	

#pdb.set_trace()	
driver =webdriver.Chrome()
driver.get("http://54.223.138.145/statistics")
getApData(driver, g_1MacAddress, 0)
while True:	
	yn = raw_input("Try again(y/n)?:")
	if 'n' == yn:
		break
	getApData(driver, g_1MacAddress, 1)
#driver.quit()



