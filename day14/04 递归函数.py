# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 12:16
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 04 递归函数.py
# @Software: PyCharm

# 人理解函数，神理解递归。

# def func():
#     print(666)
#     func()
#
# func()
# RecursionError: maximum recursion depth exceeded while calling a Python object

# 默认递归深度：998
import sys
# sys.setrecursionlimit(100000)
n = 1
def func(x):
    print(x)
    x += 1
    func(x)
func(n)

'''
alex  比 wusir 大两岁 n = 4
wusir 比日天 大两岁  n= 3
日天 比太白 大两岁  n = 2
太白 24岁 n = 1

'''
'''
def age(n):
    if n == 1:
        return 24
    else:
        return age(n-1) + 2
        
def age(4):
    if n == 1:
        return 24
    else:
        return age(n-1) + 2    
age(4) = 24 + 2 + 2 + 2
def age(3):
    if n == 1:
        return 24
    else:
        return age(2) + 2
def age(2):
    if n == 1:
        return 24
    else:
        return age(n-1) + 2
def age(1):
    if n == 1:
        return 24
    else:
        return age(n-1) + 2
'''
# print(age(4))