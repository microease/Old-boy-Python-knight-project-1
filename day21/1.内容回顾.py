# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 8:36
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 1.内容回顾.py
# @Software: PyCharm

# class A:
#     @property
#     def func(self):pass # 这个方法的返回值就是print(a.func）结果
#
# a = A()
# print(a.func)

# class A:
#     @property
#     def func(self):
#         return self.name # 这个方法的返回值就是print(a.func）结果
#
#     @func.setter
#     def func(self,new): # 修改操作
#         self.name = new
#
# a = A()
# print(a.func)
# a.func = 123

# class A:
#     @property
#     def func(self):pass # 这个方法的返回值就是print(a.func）结果
#
#     @func.deleter
#     def func(self):     # 删除一个property属性的时候会执行被deleter装饰的方法
#         del self.name
# del A().func   #

# 在类的命名空间中有什么？？
# 静态属性
# 方法
# 类方法
# 静态方法
# property方法

#classmethod
# 在类中定义一个类方法 、是一个装饰器
# 什么时候用？
    # 如果你的整个方法中都没有用到对象命名空间中的名字，且你用到了类的命名空间中的名字（普通方法和property方法除外）
# 类方法的默认参数 ： cls 值得是调用这个方法的类
# 类方法的调用方式 ： 通过类名调用,本质是方法

# staticmethod
# 将一个普通的函数放到类中来就给这个函数加上一个@staticmethod装饰器
# 这个函数就不需要传默认的参数：self，cls
# 静态方法的调用方式 ： 通过类名调用，本质还是函数
# class Foo:
#     @classmethod
#     def class_method(cls):pass
#
#     @staticmethod
#     def static_method():pass
#
# from types import MethodType,FunctionType
# obj = Foo()
# print(isinstance(Foo.class_method,MethodType))
# print(isinstance(Foo.static_method,FunctionType))
# print(obj.static_method)


# isinstance 判断对象和类之间的关系
# 判断这个对象是否是这个类、这个类的子类的对象

# issubclass 判断类和类之间的关系
# 判断一个类是否是另一个类的子类
