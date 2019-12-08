# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 11:15
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 5.封装.py
# @Software: PyCharm

# 广义上的封装
# class 类名:
#     def 方法1(self):pass
# 是为了只有这个类的对象才能使用定义在类中的方法

# 狭义上的封装
# 把一个名字藏在类中
# class Goods:
#     __discount = 0    # 私有的静态变量
#     print(__discount)
# print(Goods.__discount)  # 在类的外部不能引用私有的静态变量
# 类中的静态变量和方法名在程序加载的过程中就已经执行完了，不需要等待调用
# 在这个类加载完成之前，Goods这个名字还没有出现在内存空间中
# 私有的静态属性可以在类的内部使用，用来隐藏某个变量的值

# class Goods:
#     __discount = 0    # 私有的静态变量
#     # 变形 ： _类名__私有变量
#
# print(Goods.__dict__)
# print(Goods._Goods__discount)  # 编程规范的角度上出发 我们不能在类的外部使用私有的变量

# class Srudent:
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age
#     def name(self):
#         return self.__name
# zhuge = Srudent('诸葛',20)
# print(zhuge.name())
# print(zhuge.age)
# zhuge.age = 'aaaa'
# print(zhuge.age)

# class Goods:
#     __discount = 0.7    # 私有的静态变量
#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
#
#     def price(self):
#         return self.__price * Goods.__discount
#
#     def change_price(self,new_price):
#         if type(new_price) is int:
#             self.__price = new_price
#         else:
#             print('本次价格修改不成功')
#
# apple = Goods('APPLE',5)
# print(apple.price())
# apple.change_price('aaaa')
# print(apple.price())
#
# class User:
#     def __init__(self,username,password):
#         self.usr = username
#         self.__pwd = password
#         self.pwd = self.__getpwd()
#
#     def __getpwd(self):
#         return hash(self.__pwd)
#
# obj = User('alex','alex3714')
# print(obj.usr,obj.pwd)
# 类中的私有成员：
    # 私有的静态属性
    # 私有的对象属性
    # 私有的方法

# 我为什么要定义一个私有变量呢：
    # 我不想让你看到这个值
    # 我不想让你修改这个值
    # 我想让你在修改这个值得时候有一些限制
    # 有些方法或者属性不希望被子类继承

# 私有变量能不能在外部被定义？？？
# class A :
#     __country = 'China'  # 在类的内部会发生变形
#     print(__country)      # '_A__country'
# print(A.__dict__)
# A.__Language = 'Chinese'
# print(A.__dict__)

# 私有变量能不能被继承？？？
# class A:
#     __country = 'China'
#     def __init__(self,name):
#         self.__name = name  # '_A__name'
#
# class B(A):
#     # print(__country)
#     # NameError: name '_B__country' is not defined
#     def get_name(self):
#         return self.__name  # '_B__name'
#
# b = B('alex')
# print(b.__dict__)

# 广义上的封装 把属性函数都放到类里
# 狭义上的封装 定义私有成员

# 类中的私有成员：
    # 私有的静态属性
    # 私有的对象属性
    # 私有的方法

# 我为什么要定义一个私有变量呢：
    # 我不想让你看到这个值
    # 我不想让你修改这个值
    # 我想让你在修改这个值得时候有一些限制 ： 保证了数据的安全
    # 有些方法或者属性不希望被子类继承