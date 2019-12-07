# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 12:04
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 04 集合.py
# @Software: PyCharm

# set1 = {'alex', [1,2], 1,2,3}
# set1 = {'alex', 'wusir'}
# set2 = set({'alex', 'wusir'})
# print(set2)

# 面试必考：list去重  *****
# l1 = [1,1,2,3,4,4,3,2,1,5,5]
# set1 = set(l1)
# l2 = list(set1)
# print(l2)

#
set1 = {'alex','wusir','ritian','egon','barry'}
# 增
# set1.add('女神')
# print(set1)

# set1.update('abc')
# print(set1)

# 删
# set1.remove('alex')
# print(set1)
# set1.pop()
# print(set1)
# set1.clear()
# print(set1)

# del set1
# print(set1)

# 关系测试

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

# 交集
# print(set1 & set2)
# print(set1.intersection(set2))

# 并集
# print(set1 | set2)
# print(set1.union(set2))

# 反交集

# print(set1 ^ set2)
# print(set1.symmetric_difference(set2))

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
# 差集
# print(set1 - set2)
# print(set1.difference(set2))

# 子集
set1 = {1,2,3}
set2 = {1,2,3,4,5,6}
# print(set1 < set2)  # True
# print(set1.issubset(set2))

# 超集
# print(set2 > set1)
# print(set2.issuperset(set1))

set1 = {1,2,3}
set3 = frozenset(set1)
print(set3)  # 不可变的数据类型。  ***