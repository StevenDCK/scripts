# -*- coding:utf8 -*-

from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import email.MIMEMultipart# import MIMEMultipart
import email.MIMEText# import MIMEText
import email.MIMEBase# import MIMEBase
import email.MIMEImage# import MIMEImage
import mimetypes
import os.path 
from time import sleep
import datetime
import xlwt
import pdb
import os

g_StartTime = "2018-08-13 09:24:50"
g_StopTime  = "2018-08-13 17:46:00"
g_1MacAddress = "00:1F:7A:40:7F:30"
g_2MacAddress = "00:1F:7A:40:76:10"
#g_1MacAddress = "00:1F:7A:40:7F:30"
#g_2MacAddress = "00:1F:7A:40:73:E0"


#yu.zou@wiwide.com,steven.wang@wiwide.com, steven.yan@wiwide.com
g_Receviers = "yu.zou@wiwide.com,eco.deng@wiwide.com"
g_WorkDirctory='h:/tools/'
#g_WorkDirctory='/home1/tools/'


def getDataFromWeb(vMac, vHours, vShowcount):
	URL='http://54.223.138.145/statistics'
	Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36','Referer':'http://54.223.138.145/statistics'			}
	param={'devmac':vMac,	'devmode':'2',	'latesthour':vHours,	'showcount':vShowcount,	'faceonly':'1',	'byfaceid':'0'}	
	Page=requests.post(URL,data=param,headers=Headers,timeout=10)
	if Page.status_code==200:
		return Page.text
	else:
		raise Exception(Page.status_code)


def save2txt(vMacAddress, vTimeSet, vFileName):
	Fout = open(vFileName, 'w')
	Fout.write(vMacAddress+'\n')
	for Time in vTimeSet:
		Time = Time.strip()
		if 2<len(Time) and Time >= g_StartTime and Time <= g_StopTime :
			Fout.write(Time+'\n')
	Fout.close()		
		
def generateFile(vMac, vHours, vFilePrefix, vFilePostfix):
	res = getDataFromWeb(vMac, vHours, vHours*100)
	html=BeautifulSoup(res, 'lxml')
	tds=html.find_all('td')
	save2txt(vMac, tds[2].text.split('\n'), vFilePrefix+'In'+vFilePostfix)
	save2txt(vMac, tds[3].text.split('\n'), vFilePrefix+'Out'+vFilePostfix)


def attachFile(vFileName, vMsgBox):
	ctype,encoding = mimetypes.guess_type(vFileName)
	if ctype is None or encoding is not None:
		ctype='application/octet-stream'
	maintype,subtype = ctype.split('/',1)
	file_msg=email.MIMEImage.MIMEImage(open(vFileName,'rb').read(),subtype)
	basename = os.path.basename(vFileName)
	file_msg.add_header('Content-Disposition','attachment', filename = basename)
	vMsgBox.attach(file_msg)

	
def sendEmail(vReceviers, vTxtMsg, vFileNames):
	main_msg = email.MIMEMultipart.MIMEMultipart()
	text_msg = email.MIMEText.MIMEText("This email was sended by script.为使邮件不被识别为垃圾邮件，请在邮件的中的以上选项选择“是我订阅的”\n为了营造绿色健康的邮箱环境，我们想了解一下，这是否您订阅的邮件？    是我订阅的   不是我订阅的   我不确定   自动归档", _charset="utf-8")
	main_msg.attach(text_msg)
	for File in vFileNames.split(','):
		attachFile(File, main_msg)
	server = smtplib.SMTP('smtp.163.com')
	server.login('m13008198539@163.com', 'wwdbs100')
	main_msg['From'] = "m13008198539@163.com"
	main_msg['To'] = vReceviers
	main_msg['Subject'] = vTxtMsg
	main_msg['Date'] = email.Utils.formatdate( )
	fullText = main_msg.as_string( )
	server.sendmail('m13008198539@163.com', vReceviers.split(','), fullText)	

def txt2excel(vTxtFileName, vExcelTable):
	Fin = open(vTxtFileName,'r')
	Lines = Fin.readlines()
	Fin.close()
	i = 1
	NumLeftBlank = 0
	NumRigtBlank = 0
	for l in Lines:
		t1t2 = l.split(',')
		if len(t1t2) == 2:
			t0 = t1t2[0].replace(',', '')
			t1 = t1t2[1]
			vExcelTable.write(i,0, t0)
			vExcelTable.write(i,1, t1)
			i = i+1
			t0 = t0.strip()
			t1 = t1.strip()
			if len(t0) < 2: NumLeftBlank = NumLeftBlank +1
			if len(t1) < 2: NumRigtBlank = NumRigtBlank + 1
	vExcelTable.write(0,0, 'Blanks: '+str(NumLeftBlank))
	vExcelTable.write(0,1, 'Blanks: '+str(NumRigtBlank))

def calculateHours():
	Now = datetime.datetime.now()
	StartTime =  datetime.datetime.strptime(g_StartTime, '%Y-%m-%d %H:%M:%S')
	TimeSpan = Now - StartTime
	return (TimeSpan.days*24+TimeSpan.seconds/3600 + 1)
			
def getFilePrefix():
	StopTime = g_StopTime.split(' ')[0].split('-')
	MonthDayHour = StopTime[1]+StopTime[2]+g_StopTime.split(' ')[1].split(':')[0]
	return g_WorkDirctory+'results/'+MonthDayHour
	

if __name__=='__main__':
	import pdb
	pdb.set_trace()
	Hours = calculateHours()
	FilePrefix = getFilePrefix()	
	generateFile(g_1MacAddress, Hours, FilePrefix, '.txt')
	generateFile(g_2MacAddress, Hours, FilePrefix, '1.txt')
	
	os.system(g_WorkDirctory+'correspond.lnk ' + FilePrefix+"In.txt")
	os.system(g_WorkDirctory+'correspond.lnk ' + FilePrefix+"Out.txt")
	
	Excel = xlwt.Workbook(encoding = 'ascii')
	TIn = Excel.add_sheet('In')
	TOut= Excel.add_sheet('Out')
	txt2excel(FilePrefix+'In-corresponded.txt', TIn)
	txt2excel(FilePrefix+'Out-corresponded.txt', TOut)
	Excel.save(FilePrefix+'InOut-corresponded.xls')
	print ('The result files ware saved in path of ' + g_WorkDirctory+'results/')
	FileSet = FilePrefix+'In-corresponded.txt,'+FilePrefix+'Out-corresponded.txt,' + FilePrefix+'InOut-corresponded.xls'
	Subject = g_StartTime + '  --->  '+ g_StopTime +',   devMacAddresss:  ' + g_1MacAddress+'  vs  ' + g_2MacAddress
	#sendEmail(g_Receviers, Subject, FileSet)
	print 'The email was sended successfully.'