# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 12:16
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 6.property内置函数.py
# @Software: PyCharm

# property
# property
# property是一个装饰器函数
# 所有的装饰器函数都怎么用？ 在函数、方法、类的上面一行直接@装饰器的名字
# 装饰器的分类：
    # 装饰函数
    # 装饰方法 ： property
    # 装饰类

# class Student:
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age
#     @property   # 将一个方法伪装成一个属性
#     def name(self):
#         return self.__name
# zhuge = Student('诸葛',20)
# print(zhuge.name)

# from math import pi
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     @property
#     def area(self):
#         return self.r ** 2 * pi
#     @property
#     def perimeter(self):
#         return 2 * self.r * pi
#
# c1 = Circle(10)
# print(c1.area)
# print(c1.perimeter)
# c1.r = 5
# print(c1.area)
# print(c1.perimeter)

# 1.把我讲的例子抄一遍
# 2.把应该改成属性的这些方法 加上property装饰器
# 3.https://www.cnblogs.com/Eva-J/articles/9235899.html


