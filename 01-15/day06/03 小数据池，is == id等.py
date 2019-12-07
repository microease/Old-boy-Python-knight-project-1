# -*- coding: utf-8 -*-
# @Time    : 2018/8/9 10:40
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 03 小数据池，is == id等.py
# @Software: PyCharm

# 一 代码块。
# if True:
#     print(333)
#     print(666)
#
# # while 1:
# #     a = 1
# #     b = 2
# #     print(a+b)
#
# for i in '12324354':
#     print(i)

# 虽然上面的缩进的内容都叫代码块，但是他不是python中严格定义的代码块。
#python中真正意义的代码块是什么？
# 一个模块，一个函数，一个类，一个文件等都是一个代码块。
# def func():
#     print(333)
# class A:
#     name = 'alex'

# 交互模式下，每一行是一个代码块。
# >>> i1 = 1000  可以理解为这一行在一个文件中。
# >>> i2 = 1000  可以理解为这一行在另一个文件中。

# 二，id is ==
# name = 'alex'  # 赋值
# print('alex' == 'alex')  # 数值相同
# name = 'alex123'
# name1 = 'alex123'
# print(id(name),id(name1))  #  2370269674608 2370269674608
# 在内存中id都是唯一的，如果两个变量指向的值的id相同，就证明他们在内存中是同一个。
#  is 判断的是两个变量的id值是否相同。
# 如果is是True, == 一定是True。

# 三 小数据池（缓存机制，驻留机制）

# 小数据池的应用的数据类型： 整数，字符串，bool值

# 小数据池，python对内存做的一个优化：
# 他将 -5 ~256 的整数，以及一定规则的字符串，提前在内存中创建了池，容器，
# 容器里固定的放了这些数。
# 为什么这么做？？？
# 1，节省内存。
# 2，提高性能与效率。
# i1 = 100
# i2 = 100

# 一定规则的字符串？


# s1 = 'alex@'
# s2 = 'alex@'
# print(s1 is s2)


# 代码块：
    #python在同一个代码块中的变量，初始化对象的命令时，它会将变量与值的对应关系放到一个字典中，
    # 如果下面的代码在遇到初始化对象的命令，他会先从字典中寻找，如果存在相同的值，他会复用，指向的都是同一个内存地址。
    # dic = {'name': alex@的内存地址，}
    # python对于不同的代码块：初始化对象的命令时，他会从小数据池中寻找。
name = 'alex@'
# name1 = 'alex@'  #  name1 = name

# 同一个代码块
# i1 = 1000
# i2 = 1000
# print(id(i1),id(i2))

# def func():
#     i1 = 1000
#     print(id(i1))
#
#
# def func1():
#     i2 = 1000
#     print(id(i2))
#
# func1()
# func()






