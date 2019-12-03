# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 12:29
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 05 深浅copy.py
# @Software: PyCharm

# 赋值运算
# l1 = [1,2,3]
# l2 = l1
# l1.append(666)
# print(l2)
# print(id(l1))
# print(id(l2))


# 浅copy
# l1 = [1,2,3]
# l2 = l1.copy()
# l1.append(666)
# print(l2)

# l1 = [1,2,3,[22,]]
# l2 = l1.copy()
# # l1.append(666)
# # print(l1,l2)
# l1[-1].append('taibai')
# # print(l1,l2)
# print(id(l1))
# print(id(l2))
# print(id(l1[-1]))
# print(id(l2[-1]))
# 深copy
import copy
# l1 = [1,2,3,[22,]]
# l2 = copy.deepcopy(l1)
# # print(l1,l2)
# # l1.append(666)
# l1[-1].append('太白')
# print(l2)

# 应用场景：面试会考，解释深浅copy
    # 完全独立的copy一份数据，与原数据没有关系，深copy
    # 如果一份数据（列表）第二层时，你想与原数据进行公用，浅copy。

#  面试题
# 切片属于浅copy
# l1 = [1,2,3,[22,33]]
# l2 = l1[:]
# # l1.append(666)
# l1[-1].append(666)
# print(l2)
