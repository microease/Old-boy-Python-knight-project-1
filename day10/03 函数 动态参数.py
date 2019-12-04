# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 10:09
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 03 函数 动态参数.py
# @Software: PyCharm
# 你的函数，为了拓展，对于传入的实参数量不固定，万能参数，动态参数，*args, **kwargs

# def sum1(*args,**kwargs):  # 在函数的定义时，在 *位置参数，聚合。
#                    # *args 将所有的实参的位置参数聚合到一个元组，并将这个元组赋值给args
#     print(args)
#     print(kwargs)
# sum1(1,2,3,4,name='alex',age=1000)
# def sum1(*args,**kwargs):
#     count = 0
#     for i in args:
#         count = count + i
#     return count
# print(sum1(10,10,20,30,100))

# * 的魔性用法
# 在函数的定义时，在 *位置参数，**位置参数聚合。
# 在函数的调用(执行)时，在 *位置参数，**位置参数打散。
# l1 = [1,2,3]
# l2 = [111,22,33,'alex']
# #
# def func1(*args):
#     print(args)
#     return args[0] + args[1]
# print(func1(l1,l2))

# def func1(*args,**kwargs):
#     # print(args)
#     print(kwargs)
# func1(*l1,*l2)
# func1(*(1,2,3),*('alex','sb'))
# func1(*'alex',*'sb')
# func1(1,2,3,'alex','sb')
#
# func1(**{'name':'alex'},**{'age':1000})  # func1(name='alex',age=1000})

# 形参的顺序
# 位置参数，默认参数，*args,**kwargs

# 位置参数，默认参数
# def func(a,b,sex='男'):
#     # print(a)
#     print(sex)
# func(100,200,)
# 位置参数，*args, 默认参数
# def func(a,b,*args,sex='男',):
#     # print(a)
#     print(a,b)
#     print(sex)
#     print(args)
# func(100,200,1,2,34,5,6)

# 位置参数，*args, 默认参数 **kwargs
def func(a, b, *args, sex='男', **kwargs, ):
    print(a, b)
    print(sex)
    print(args)
    print(kwargs)


func(100, 200, 1, 2, 34, 5, 6, sex='nv', name='alex', age=1000)
