#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_param.py 
@time: 2020/11/30 
"""
import pytest


#参数化：笛卡尔积
@pytest.mark.parametrize('a',[1,2,3])
@pytest.mark.parametrize('b',[4,5,6])
@pytest.mark.parametrize('c',[7,8,9])
def test_parm(a,b,c):
    print(a,b,c)



#数据驱动：测试数据的数据驱动、测试步骤的数据驱动