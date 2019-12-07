# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 12:35
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 05 range.py
# @Software: PyCharm

# range 自定制的 数字范围的 可迭代对象类比成列表
# range(1,101)
# print(range(1,101))
# range() 一般和for 循环结合使用。
# for i in range(1,11):
#     print(i)

# for i in range(1,20,2):
#     print(i)

# for i in range(1,101,2):
#     print(i)

# for i in range(10,1,-1):
#     print(i)

l1 = ['alex', 'alex', 'taibai', 'egon', '景女神', '文周老师', '日天']
# 方法一：不好
# for i in l1:
#     print(l1.index(i))
# 方法二：
# for i in range(0,len(l1)):
#     print(i)
s1 = 'alex'
l1 = ['alex', 'alex', 'taibai', 'egon', '景女神', '文周老师', '日天']
# print('a' in s1)
# print('al' in s1)
# print('alx' in s1)
print('alex' not in l1)
# print(['alex','alex'] in l1)
