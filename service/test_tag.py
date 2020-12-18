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
    def setup(self):
        self.tag = Tag()

    @pytest.mark.parametrize("tag_id,tag_name",[
        ["etZyjlEQAAw4j09GsfEKzaXAMbAlAjfQ", "tag_new_"],
        ["etZyjlEQAAC7pkbn8p84WJmJaXD6lfjQ", "tag2_"],
        ["etZyjlEQAA6ktxPqiuaJwqHp_8d0ReJw", "tag3_"]
    ])
    def test_tag_list(self,tag_id,tag_name):
        #group_name="job_new"
        tag_name=tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
        tag_id=tag_id

        r=self.tag.list()
        #print(json.dumps(r.json(), indent=2))
        r=self.tag.update(id=tag_id,tag_name=tag_name)
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == "ok"
        #print(json.dumps(r.json(), indent=2))

        r=self.tag.list()
        print(json.dumps(r.json(), indent=2))
        #print(json.dumps(r.json(), indent=2))
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
        #print(jsonpath(r.json(),f"$..[?(@.name={tag_name})]")[0]['name'])
        #assert  jsonpath(r.json(),"$..[?(@.name={tag_name})]")[0]['name']==tag_name
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name

    def test_tag_list_fail(self):
        pass

    @pytest.mark.parametrize("tag_name",
                             ["tag5", "tag6"])
    def test_add_tag(self,tag_name):
        #tag_name="tag4_"
        group_id = "etZyjlEQAAw4j09GsfEKzaXAMbAlAjfQ"
        print(group_id,tag_name)
        r = self.tag.add(tag_name=tag_name, group_id=group_id)
        print(json.dumps(r.json(), indent=2))
        print("end")
        assert r.json()['errcode'] == 0
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name



    def test_del_tag(self):
        r=self.tag.list()
        print(json.dumps(r.json(), indent=2))
        tag_id="etZyjlEQAA6ktxPqiuaJwqHp_8d0ReJw"
        r=self.tag.delete_tag(tag_id)
        assert r.json()['errcode'] == 0
        r = self.tag.list()
        print(json.dumps(r.json(), indent=2))
