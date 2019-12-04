# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 11:54
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 05 迭代器.py
# @Software: PyCharm

# 可迭代对象
# for i in 'abc':
#     print(i)
# for i in 123:
#     print(i)  # 'int' object is not iterable

# 对象内部含有__iter__方法就是可迭代对象.
# 可迭代对象满足可迭代协议。

# 可迭代对象：str list dict,tuple,set,range()
s1 = 'strs'
# print(dir(s1))

# 判断一个对象是否是可迭代对象：
# 第一个方法
# dic = {'name':'alex'}
# print('__iter__' in dir(s1))
# print('__iter__' in dir(dic))
#第二种方法
from collections import Iterable
from collections import Iterator

# print(isinstance('alex',Iterable))  # True
# print(isinstance('alex',Iterator))  # True

# print(isinstance('alex',str))

# 迭代器？

# 对象内部含有__iter__方法且含有__next__方法就是迭代器.

# f = open('register', encoding='utf-8')
# print('__iter__' in dir(f))
# print('__next__' in dir(f))
# print('__iter__' in dir(dict))
# print('__next__' in dir(dict))


# 可迭代对象vs迭代器
# 可迭代对象不能取值，迭代器是可以取值的。
# 可迭代对象 --->(转化成)迭代器
# lis = [1, 2, 3]  # 可迭代对象
# # ite1 = lis.__iter__()  # 迭代器  <list_iterator object at 0x0000027A183BFFD0>
# ite1 = iter(lis)  # 迭代器  <list_iterator object at 0x0000027A183BFFD0>
# print(ite1)

# 迭代器如何取值？  next一次，取一个值
# print(ite1.__next__())
# print(ite1.__next__())
# print(ite1.__next__())
# print(ite1.__next__())

# 1, 可迭代对象不能取值，迭代器是可以取值的。
# 2, 迭代器非常节省内存。
# 3,迭代器每次只会取一个值。
# 4,，迭代器单向的，一条路走到头。

s1 = 'kfdsjl'
# for i in s1:
#     print(i)

# 1,将可迭代对象转化成迭代器。
# 2，调用__next__方法取值。
# 3，利用异常处理停止报错。
# iter1 = s1.__iter__()
#
# while 1:
#     try:
#         print(iter1.__next__())
#     except StopIteration:
#         break

# l1 = [i for i in range(100)]
# print(l1)
# ret =( i for i in range(1000000))
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())