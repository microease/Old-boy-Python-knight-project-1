# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 11:11
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 04 闭包.py
# @Software: PyCharm

# 内层函数对外层函数的变量（非全局变量）的引用，并返回 这样就形成了闭包。

# def wraaper():
#     name = 'alex'
#     def inner():
#         print(name)
#     print(inner.__closure__)
#     inner()
#     return inner
# wraaper()
# name = 'alex'
# def wraaper():
#     def inner():
#         print(name)
#     print(inner.__closure__)  # None
#     inner()
#     return inner
# wraaper()


# name = 'alex'
# def wraaper(n):
#     n = 'alex'
#     def inner():
#         print(n)
#     print(inner.__closure__)  # cell at 0x000002AD93BF76D8:
#     inner()
#     return inner
# wraaper(name)


'''
闭包作用：
    当程序执行时，遇到了函数执行，他会在内存中开辟一个空间，局部名称空间，
    如果这个函数内部形成了闭包，
    那么他就不会随着函数的结束而消失。
'''

from urllib.request import urlopen

def index():
    url = "http://www.xiaohua100.cn/index.html"
    def get():
        return urlopen(url).read()
    return get

xiaohua = index()  # get
content = xiaohua()  # get()
content = xiaohua()  # get()
content = xiaohua()  # get()
content = xiaohua()  # get()
content = xiaohua()  # get()
content = xiaohua()  # get()
content = xiaohua()  # get()
content = xiaohua()  # get()
print(content.decode('utf-8'))
