# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 14:43
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 05 运算符.py
# @Software: PyCharm
# and or not
# 优先级：（）> not > and > or
# 第一种情况，前后条件为比较运算
# print(1 < 2 or 3 > 1)
# print(1 < 2 and 3 > 4)
# print(1 < 2 and 3 > 4 or 8 < 6 and 9 > 5 or 7 > 2)
# print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)
# print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)

# 第二种情况，前后两边的条件为数值
'''
x or y if x is True,return x
'''
# print(1 or 2)
# print(1 and 2)
# print(5 or 2)
# print(5 and 2)
# print(0 or 2)
# print(-1 or 2)
'''
# 补充
# int < --- > bool
# 0 对应的bool值为False,非0 都是True.
# True     1    ,False     0

# print(bool(100))
# print(bool(-1))
# print(bool(0))
# print(int(True))
# print(int(False))
'''
# print(0 or 3 and 5 or 4)

# 变态面试题：思考
# print(1 > 2 or 3 and 4 < 6)
# print(2 or 3 and 4 < 6)

# 应用：
# 1，if while 等条件判断（数据库，Django orm Q查询）。
# 1，面试。