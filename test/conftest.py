#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: conftest.py 
@time: 2020/12/01 
"""
import pytest
#存储公共的fixture，名字不能改
#不需要导入

@pytest.fixture
def con_db():
    print("链接数据库")
    return "con success"