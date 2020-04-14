# -*- coding:utf8 -*-
import os
BootFilePath = '/H/uwork/MV-CDK/CDK2_17.07.02_ma2x5x/mdk/projects/Ipipe2/apps/GuzziSpi_mv182_OV5658_ma2150/output/'
BootFileName = 'GuzziSpi_mv182_OV5658_ma2150.mvcmd'
os.system('cd '+BootFilePath)
#重命名
Fin = open(BootFilePath+'../Compiletime.txt', 'r')
Compiletime = Fin.readline()
Compiletime = Compiletime.strip()
Fin.close()
ShortName = 'boot-'+Compiletime+'.mvcmd'
RealBootFileName = BootFilePath+ ShortName
os.system('cp '+ BootFilePath+BootFileName + ' ' + RealBootFileName)
#计算md5
os.system('md5sum '+ RealBootFileName +' > md5.txt')
#生成dbsversion
Fin = open('md5.txt', 'r')
Md5Infor = Fin.readline()
Md5 = Md5Infor.split()[0]
Fin.close()
Fout = open('dbsversion', 'w')
Fout.write('bootname ' + ShortName+'\n')
Fout.write('bootmd5 ' + Md5)
Fout.close()
#上传boot 和 dbsversion
os.system('scp  ' + RealBootFileName+  ' bjrd01@52.83.112.192:/home/prod/deploys/wiupdate/wios/W1242/camera/DP')
os.system('scp  dbsversion' +  ' bjrd01@52.83.112.192:/home/prod/deploys/wiupdate/wios/W1242/camera/DP')

print 'OK! The boot filename is: ' + RealBootFileName
print '''\n\ncurl upgrade.wiwide.com/wios/W1242/video_fw_upgrade-DP-manual-new.sh -o /tmp/video_fw_upgrade-DP-manual-new.sh
chmod 777 /tmp/video_fw_upgrade-DP-manual-new.sh
/tmp/video_fw_upgrade-DP-manual-new.sh\n\n
'''
print '''
/home/prod/deploys/wiupdate/wios/W1242/camera/DP\n\n
'''
os.system('ssh bjrd01@52.83.112.192')