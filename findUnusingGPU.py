#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import time
import requests
import json
import os
import  pdb
import socket
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


def getMessage():
    #pdb.set_trace()
    os.system("ps -ef | grep train_net.py > .gpu.log")
    fin = open(".gpu.log", 'r')
    lines = fin.readlines()
    fin.close()
    msg = ""
    if len(lines)<42:
        msg = "There are idle gpus,  on serverce of " + str(socket.gethostbyname(socket.getfqdn(socket.gethostname())))
    return msg

if __name__ == '__main__':
    wx = WeChat()
    num = 3
    while True:
        msg =getMessage()
        if len(msg)>0:
            wx.send_data(msg)
            num -= 1
            if 0==num: exit(0)
        time.sleep(5)