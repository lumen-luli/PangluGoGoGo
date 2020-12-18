#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test_fixture.py 
@time: 2020/12/01 
"""
#pytest test_fixture.py --setup-show -vs 回溯fixture执行过程
#pytest --collect-only 只收集用例
#pytest --junitxml=./result.xml 生成执行结果文件


import pytest

#fixture参数
#autouse=True，会把fixture应用到每一个上面，没写也会用。默认False。自动执行顺序，方法名字排序前的先执行
#scope 默认是function级别，（class，module，package，session
@pytest.fixture
def login():
    print("login")
    #yield相当于return
    yield ["tom","123456"]
    #生成器，在fixture方法里加了yield，它后面的操作相当于tear down，前面的操作相当于 setup
    print("login out")


# @pytest.fixture
# def con_db():
#     print("链接数据库")

#通过装饰器方法传入fixture,这样无法打印login返回值
@pytest.mark.usefixtures("login")
def test_case1():
    print(login)
    print("case1")


def test_case2():
    print("case2")

#如果测试用例里面需要用到fixture返回值，fixture名字需要以参数的形式传到方法里，可以打印出login返回值
#允许传入多个fixture，执行顺序按参数顺序
def test_case3(login,con_db):
    print(login)
    print(con_db)
    print("case3")