#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_tag.py
@time: 2020/12/07 
"""
import datetime
import json

import pytest
import requests
from jsonpath import jsonpath

from service.tag import Tag



class  TestTag:
    def __init__(self):
        self.tag = Tag()

    @pytest.mark.parametrize("tag_id,tag_name",[
        ["etZyjlEQAAw4j09GsfEKzaXAMbAlAjfQ", "tag_new_"],
        ["etZyjlEQAAw4j09GsfEKzaXAMbAlAjfQ", "tagz中文"],
        ["etZyjlEQAAw4j09GsfEKzaXAMbAlAjfQ", "tag---[中文]"]
    ])
    def test_tag_list(self,tag_id,tag_name):
        #group_name="job_new"
        tag_name=tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
        tag_id=tag_id

        r=self.tag.list()
        r=self.tag.update(id=tag_id,tag_name=tag_name)

        r=self.tag.list()
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        # tags = [
        #     tag
        #     for group in r.json()['tag_group'] if group['group_name'] == group_name
        #     for tag in group["tag"] if tag["name"] == tag_name]
        # print(tag_name)
        # print(tags)
        # assert tags != []

        #使用jsonpath获取tagname
        assert  jsonpath(r.json(),f"$..[?(@.name={tag_name})]")[0]['name']==tag_name

    def test_tag_list_fail(self):
        pass
