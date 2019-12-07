# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 12:26
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 04 元祖.py
# @Software: PyCharm
#  元组：只读列表，只允许查询，不允许增删改
# tu1 = ('alex', 100, True, [1, 2, 3], {'name':'太白'},(22, 33))
# 索引，切片，切片+步长
# print(tu1[0])
# print(tu1[:3])
# # for 循环
# for i in tu1:
#     print(i)
# index,len,count
# 应用场景： 一些非常重要的数据，不允许所有人修改的，放在元组中。
# tu1[3].append(666)
# tu1.append(666) 错的
# 元组 儿子不能改，孙子可能可以改。
# print(tu1)