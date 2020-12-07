#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_classic.py 
@time: 2020/12/04 
"""
import json
import datetime

import requests


#todo: 1、与底层具体的实现框架代码耦合严重，比如公司切换了协议
#todo: 2、代码冗余，需要封装
#todo: 3、无法清晰的描述业务
#todo: 4、无法使用jsonpath表达更灵活的查找

def test_tag_list():
    corpid="wwa52a42ed3e961e9e"
    corpsecret="hd7lLu2RyUuapwJyR9Uf07kGsCBX6egNT9AnmsmfQ_8"
    r=requests.get(
        "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        params={"corpid":corpid,"corpsecret":corpsecret}
    )
    token=r.json()['access_token']



    tag_name="tag_new_"+str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
    r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
                    params={"access_token":token},
                    json={
                        "id":"etZyjlEQAAw4j09GsfEKzaXAMbAlAjfQ",
                        "name":tag_name,
                    }
                    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0



    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={"access_token": token},
        json={"tag_id": []}

    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    tags = [
        tag
        for group in r.json()['tag_group'] if group['group_name'] == "job_new"
        for tag in group["tag"] if tag["name"] == tag_name]
    print(tag_name)
    print(tags)
    assert tags != []



