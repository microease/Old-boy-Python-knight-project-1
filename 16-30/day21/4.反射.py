# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 10:03
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 4.反射.py
# @Software: PyCharm

# 反射
# 3w 1h
# what 是什么
    # 反射 使用字符串数据类型的变量名来获取这个变量的值
# a = 1
# b = 2
# name = 'alex'

# why 为什么 三个场景
    # input
        # 用户输入的如果是a，那么就打印1，如果输入的是b就打印2，如果输入的是name，就打印alex
    # 文件
        # 从文件中读出的字符串，想转换成变量的名字
    # 网络
        # 将网络传输的字符串转换成变量的名字
# where 在哪儿用
# how 怎么用

# 反射 ******
# hasattr *****
# getattr ******

# 反射类中的变量 : 静态属性,类方法，静态方法
# class Foo:
#     School = 'oldboy'
#     Country = 'China'
#     language = 'Chiness'
#
#     @classmethod
#     def class_method(cls):
#         print(cls.School)
#     @staticmethod
#     def static_method():
#         print('in staticmethod')
#
#     def wahaha(self):
#         print('wahaha')
# print(Foo.School)
# print(Foo.Country)
# print(Foo.language)
# 判断实现
# if inp == 'School':print(Foo.School)
# elif inp == 'Country':print(Foo.Country)
# elif inp == 'language':print(Foo.language)

# 反射实现
# while True:
#     inp = input('>>>')
#     print(getattr(Foo,inp))

# 解析getattr方法
# getattr(变量名：命名空间，字符串：属于一个命名空间内的变量名)
# getattr(Foo,'School')  # Foo.School
# print(Foo.class_method)
# print(getattr(Foo,'class_method'))
# getattr(Foo,'class_method')()    # Foo.class_method()
# getattr(Foo,'static_method')()   # Foo.static_method()
# getattr(Foo,'wahaha')(1)  # Foo.wahaha(1)
# print(hasattr(Foo,'wahaha'))
# print(hasattr(Foo,'shuangwaiwai'))

# 反射实现
# while True:
#     inp = input('>>>')
#     if hasattr(Foo,inp):
#         print(getattr(Foo,inp))

# 反射对象中的变量
# 对象属性
# 普通方法
# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def eating(self):
#         print('%s is eating'%self.name)
# alex = Foo('alex_sb',83)
# print(getattr(alex,'name'))
# print(getattr(alex,'age'))
# getattr(alex,'eating')()

# 反射模块中的变量
import os # os就是一个模块
# os.rename('D:\骑士计划PYTHON1期\day21\__init__.py','D:\骑士计划PYTHON1期\day21\__init__.py.bak')
# getattr(os,'rename')('D:\骑士计划PYTHON1期\day21\__init__.py.bak','D:\骑士计划PYTHON1期\day21\__init__.py')

# 反射本文件中的变量  分析过程
# a = 1
# b = 2
# name = 'alex'
# def qqxing():
#     print('qqxing')

# cls.xxx
# obj.xxx
# os.xxx

# import sys
# print(sys.modules['__main__'])  # 本文件的命名空间
# print(sys.modules['__main__'].a)
# print([__name__]) # 变量，内置的变量

# 反射本文件中的变量  结论
# a = 1
# b = 2
# name = 'alex'
# def qqxing():
#     print('qqxing')
# class Foo:pass
#
# import sys
# print(sys.modules[__name__])     # 反射本文件中的变量 固定的使用这个命名空间
# print(getattr(sys.modules[__name__],'a'))
# print(getattr(sys.modules[__name__],'b'))
# print(getattr(sys.modules[__name__],'name'))
# getattr(sys.modules[__name__],'qqxing')()
# print(getattr(sys.modules[__name__],'Foo'))
# obj = getattr(sys.modules[__name__],'Foo')()
# print(obj)

# setattr
# delattr
# class Foo:
#     Country = 'China'
#
# def func():
#     print('qqxing')
#Foo.School = 'OLDBOY'
# setattr(Foo,'School','OLDOBY')  # 接受三个参数 命名空间 ‘变量名’ 变量值
# print(Foo.__dict__)
# print(getattr(Foo,'School'))
# print(Foo.School)

# setattr(Foo,'func',func)  # 一般没人往空间中添加函数
# print(Foo.__dict__)
# print(Foo.func)

# delattr
# del Foo.Country
# print(Foo.__dict__)
# delattr(Foo,'Country')
# print(Foo.__dict__)

# hasattr
# getattr
# setattr
# delattr

# 反射类中的变量
# 反射对象中的变量
# 反射模块中的变量
# 反射本文件中的变量

# 用反射的场景
# input
# 网络
# 文件






