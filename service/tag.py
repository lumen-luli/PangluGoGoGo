# -*- coding:utf-8 _*-
""" 
@author:lupang 
@file: tag.py 
@time: 2020/12/07 
"""
import datetime
import json

import requests


class Tag:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = "wwa52a42ed3e961e9e"
        corpsecret = "hd7lLu2RyUuapwJyR9Uf07kGsCBX6egNT9AnmsmfQ_8"
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={"corpid": corpid, "corpsecret": corpsecret}
        )
        token = r.json()['access_token']
        # po里面通常不加断言，如果确定读取失败不通过，可以加
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        return token

    def add(self):
        pass

    def list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={"access_token": self.token},
            json={"tag_id": []}
        )

        return r

    def update(self,id,tag_name):
        #tag_name = "tag_new_" + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            params={"access_token": self.token},
            json={
                  "id": id,
                  "name": tag_name,
            }
        )
        return r

    def delete(self):
        pass
