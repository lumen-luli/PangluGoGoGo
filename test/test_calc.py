#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_calc.py
@time: 2020/11/26 
"""
import pytest
import yaml


#解析测试数据
def get_data():
    with open("./datas/calc.yaml",encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print(add_ids,add_datas)
    return [add_datas,add_ids]

#解析测试步骤
def steps(calc,a,b,exp):
    with open("./datas/steps.yaml",encoding='utf-8') as f:
        steps = yaml.safe_load(f)

        for step in steps:
            if "add" == step:
                result = calc.add(a,b)
            elif "add1" == step:
                result = calc.add(a, b)
            assert exp==result


class TestCalc:
    def setup_class(self):
        print("begin")
        self.calc = TestCalc()

    def teardown_class(self):
        print("end")

    @pytest.mark.parametrize('a,b,expect',
        get_data()[0],ids=get_data()[1]
    ,)
    def test_answer(self,a,b,expect):
        ret=a+b
        assert ret==expect


    def add(self,a,b):
        ret = a+b
        return ret

    def test_steps(self):
        a=1
        b=1
        exp=2
        steps(self.calc,a,b,exp)
        # assert 2== self.calc.add(1,1)


    def teardown_function(self):
        print("资源销毁")

