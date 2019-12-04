# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 10:25
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 03 函数名的应用.py
# @Software: PyCharm
def func():
    print(666)


# 1 ,函数名就是函数的内存地址。
# print(func)

# 2, 函数名可以作为变量。
# a = 2
# b = a
# c = b
# print(c)\

# def func1():
#     print(666)
# f1 = func1
# f2 = f1
# f2()

# 3,函数名可以作为函数的参数。

# def func1():
#     print(666)
#
# def func2(x):
#     print(x)  # <function func1 at 0x0000026C3D983BF8>
#     x()
#
# # a = '太白'
# # func2(a)
# print(func1)  # <function func1 at 0x0000026C3D983BF8>

# def func():
#     print(666)
#
#
# def func1():
#     func()
#
#
# def func2(x):
#     x()  # func1()
#
# func2(func1)

# 函数名可以当做函数的返回值。

# def wraaper():
#     def inner():
#         print('inner   ')
#     return inner
# ret = wraaper()  # inner
# ret() # inner()

# def func2():
#     print('in func2')
#
# def func3(x):  # x = func2
#     print('in func3')
#     return x  # func2
#
# f1 = func3(func2)  # func2
# f1()

# 函数名可以作为容器类类型的元素。

# a = 6
# b = 4
# c = 5
# l1 = [a,b,c]
# print(l1)

# def func1():
#     print('in func1')
#
# def func2():
#     print('in func2')
#
# def func3():
#     print('in func3')
#
# def func4():
#     print('in func4')
# l1 = [func1,func2,func3,func4]
# for i in l1:
#     i()

# 向上面的函数名这种，第一类对象。


# globals() locals()
# globals() # 返回全局变量的一个字典。
# locals()  返回 当前位置 的局部变量的字典。

# def func1():
#     a = 2
#     b = 3
#     # print(globals())
#     # print(locals())
#     def inner():
#         c = 5
#         d = 6
#         print(globals())
#         print(locals())
#     inner()
# # print(globals())
# # print(locals())
# func1()


