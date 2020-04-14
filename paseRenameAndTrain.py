#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import time
import requests
import json
import os
import  pdb
class WeChat:
    def __init__(self):
        self.CORPID = 'ww66ee240fa200c293'  #企业ID，在管理后台获取https://work.weixin.qq.com/login
        self.CORPSECRET = '5rCJYNOG37bbbp86wagd-eblknI9BawKjCIRXsEAYlM'#自建应用的Secret，每个自建应用里都有单独的secret
        self.AGENTID = '1000003'  #应用ID，在后台应用中获取
        self.TOUSER = "DengBoSheng"  # 接收者用户名,多个用户用|分割  Effy|

    def _get_access_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        values = {'corpid': self.CORPID,
                  'corpsecret': self.CORPSECRET,
                  }
        req = requests.post(url, params=values)
        data = json.loads(req.text)
        return data["access_token"]

    def get_access_token(self):
        try:
            with open('.access_token.conf', 'r') as f:
                t, access_token = f.read().split()
        except:
            with open('.access_token.conf', 'w') as f:
                access_token = self._get_access_token()
                cur_time = time.time()
                f.write('\t'.join([str(cur_time), access_token]))
                return access_token
        else:
            cur_time = time.time()
            if 0 < cur_time - float(t) < 7260:
                return access_token
            else:
                with open('.access_token.conf', 'w') as f:
                    access_token = self._get_access_token()
                    f.write('\t'.join([str(cur_time), access_token]))
                    return access_token

    def send_data(self, message):
        #pdb.set_trace()
        send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.get_access_token()
        send_values = {
            "touser": self.TOUSER,
            "msgtype": "text",
            "agentid": self.AGENTID,
            "text": {
                "content": message
                },
            "safe": "0"
            }
        send_msges=(bytes(json.dumps(send_values), 'utf-8'))
        respone = requests.post(send_url, send_msges)
        respone = respone.json()   #当返回的数据是json串的时候直接用.json即可将respone转换成字典
        return respone["errmsg"]

g_mtime = 1574321263.1668758
g_latstUpateTime = datetime.datetime(2017,1,1)
def getMessage():
    #pdb.set_trace()
    global g_mtime
    global g_latstUpateTime
    os.system("cd mailBox &&  git pull")
    cmdFileName = "mailBox/cmd.txt"
    mtime = os.path.getmtime(cmdFileName)
    msg = ""
    if mtime>g_mtime:
        g_mtime = mtime
        fin = open(cmdFileName, 'r')
        cmd = fin.readline().strip()
        fin.close()
        os.system(cmd + " >.tmp.txt")
        fin = open('.tmp.txt', 'r')
        lines = fin.readlines()
        fin.close()
        for line in lines:
            msg += line
        msg = msg.strip()
        g_latstUpateTime = datetime.datetime.now()
    else:
        thisTime = datetime.datetime.now()
        timeSpan = (thisTime-g_latstUpateTime).total_seconds()
        if timeSpan>60*10: time.sleep(6)
        else: time.sleep(1)
    return msg

if __name__ == '__main__':
    wx = WeChat()
    time.sleep(3000)
    os.system("kill -9 2191 2190 2189 2194 2197 2198 2199 2200")
    os.system("kill -9 2191 2190 2189 2194 2197 2198 2199 2200")
    os.system("python3 tools/ssd/test_net.py --cfg cfgs/ssd/mscoco_humanparts/mobilenet_v1/ssd_MV1-0.25-64HEAD-FL_540x960_s2x_RetinaFace.yaml 2>&1 | tee  logs/evalHF80wh02NsyBN.txt")
    wx.send_data("evaluation finish! Start training!")
    os.system("mv /home/dbs/pet/ckpts/ssd/mscoco_humanparts/mobilenet_v1/ssd_MV1-0.25-64HEAD-FL_540x960_s2x_HF-SCRATCH/model_latest.pth /home/dbs/pet/ckpts/ssd/mscoco_humanparts/mobilenet_v1/ssd_MV1-0.25-64HEAD-FL_540x960_s2x_HF-SCRATCH/model_latest.pth_nsybn")
    os.system("CUDA_VISIBLE_DEVICES=2,1,0,3,4,5,6,7 python3 -m torch.distributed.launch --nproc_per_node=8 --master_addr 127.0.0.2 --master_port 29587  tools/ssd/train_net.py --cfg cfgs/ssd/mscoco_humanparts/mobilenet_v1/ssd_MV1-0.25-64HEAD-FL_540x960_s2x_RetinaFace.yaml 2>&1 | tee logs/trainHFretinaSsdsycnBN.txt")
    wx.send_data("sync bn training finish!")
    os.system("python3 tools/ssd/test_net.py --cfg cfgs/ssd/mscoco_humanparts/mobilenet_v1/ssd_MV1-0.25-64HEAD-FL_540x960_s2x_RetinaFace.yaml 2>&1 | tee  logs/evalHF80whSyBN.txt")
    wx.send_data("sync bn evaluation finish!")