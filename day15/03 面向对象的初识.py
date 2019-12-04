# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 11:56
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 03 面向对象的初识.py
# @Software: PyCharm


s1 = 'fkdsjdsjfksdalfksld'
# count = 0
# for i in s1:
#     count += 1
# print(count)


# def mylen(argv):
#     count = 0
#     for i in argv:
#         count += 1
#     return count
# mylen(s1)

# 结构上理解：面向对象：两部分
class A:
    name = 'alex' #  静态属性，静态变量，静态字段。

    def func1(self):  # 函数，动态属性，方法。
        pass

# 函数vs面向对象


def register(argv):
    pass

def login(argv):
    pass
def shoppingcar(argv):
    pass


class Shopping_Car:
    def __init__(self):  # 特殊方法
        pass

    def register(self):
        pass

    def login(self):
        pass
    def shoppingcar(self):
        pass

# 1，函数封装一个功能，而面向对象封装多个相关的功能。
# 2，面向对象抽象，它是一种思想，站在上帝的角度去理解他。
# 3，程序可扩展，对象都是一个个独立的。耦合性，差异性。


# 类，对象。
# 类：具有相同属性或者功能的一类实物。
#对象：对象是类的具体体现。


