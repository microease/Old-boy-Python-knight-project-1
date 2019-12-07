# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 10:22
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 03 基础数据类型的补充.py
# @Software: PyCharm
# print('q       '.isspace())

# 元组
# 如果元组中只有一个数据，且没有逗号，则该 '元组' 与里面的数据的数据类型相同。
# tu1 = (1,)
# tu2 = ('alex')
# tu3 = ([1,2,3],)
# print(tu1,type(tu1))
# print(tu2,type(tu2))
# print(tu3,type(tu3))

# 列表
# 列表与列表可以相加
# l1 = [1,2,3]
# l2 = ['alex','wusir']
# l3 = l1 + l2
# print(l3)

#
# l1 = [11, 22, 33, 44, 55, 66, 77, 88]
# 将列表中索引为奇数的元素，全部删除
# 方法一：切片+步长删除
# del l1[1::2]
# # print(l1)
l1 = [11, 22, 33, 44, 55, 66, 77, 88]
# for i in range(len(l1)):
#     print(l1)
#     print(i)
#     if i % 2 == 1:
#         l1.pop(i)
#     print(l1)
#     print(i)
# print(l1)

# 在循环一个列表时，如果对列表中的某些元素进行删除，
# 那么此元素后面的所有元素就会向前进一位，他们的索引就会发生变化。


# 方法二：
# l2 = []
#
# for i in range(len(l1)):
#     if i % 2 == 0:
#         l2.append(l1[i])
# print(l2)
# l1 = l2
# print(l1)
# l1 = [11, 22, 33, 44, 55, 66, 77, 88]
# # 方法三：倒着删除
# for index in range(len(l1)-1, -1, -1):
#     if index % 2 == 1:
#         l1.pop(index)
# print(l1)
# 在循环一个列表时，最好不要对此列表进行改变大小（增删）的操作。


# 字典

# fromkeys()
# dic1 = dict.fromkeys([1,2,3],'alex')
# print(dic1)

# 面试题：创建字典的方式
#1，
# dic = {'name':'alex'}
#2
# dic = dict({'name':'alex'})
# print(dic)
#3, fromkeys()

# 陷阱：
# dic1 = dict.fromkeys([1,2,3],[])
# print(dic1)
# # dic1[1].append('alex')
# print(dic1)
# print(id(dic1[1]))
# print(id(dic1[2]))
# print(id(dic1[3]))

#
dic = {'key1': 'value1','key2': 'value2', 'k3':'v3', 'name': 'alex'}
# 将 dic的键中含有k元素的所有键值对删除。
# for key in dic:
#     if 'k' in key:
#         dic.pop(key)
# dictionary changed size during iteration： 在循环一个字典时，不能改变字典的大小。
# l1 = []
# for key in dic:
#     if 'k' in key:
#         l1.append(key)
# # print(l1)
# for key in l1:
#     dic.pop(key)
# print(dic)

# 数据类型的转换。
'''
int str bool 三者转换
str <---> bytes
str <---> list
dict.keys() dict.values() dict.items()  list()
tuple <---> list
dict ---> list
'''

# str ---> list
# s1 = 'alex wusir taibai'
# l1 = s1.split()
# print(l1)
# list  ---> str  此list中的元素全部是str类型
# l1 = ['alex', 'wusir', 'taibai', 100]
# # s2 = ' '.join(l1)
# # print(s2)

# tuple <---> list
# l1 = [1,2,3]
# tu1 = tuple(l1)
# print(tu1)

# tu2 = (0,2,3)
# l1 = list(tu2)
# print(l1)

# dic1 = {'name': 'alex', 'age': 1000}
# l1 = list(dic1)
# print(l1)
# 有问题
# l2 = ['name', 'age']
# dic2 = dict(l2)
# print(dic2)

# 0 "  [] () {} set() ---> bool False