# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 11:48
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 04 列表推导式，生成器表达式.py
# @Software: PyCharm

# l1 = []
# for num in range(1,101):
#     l1.append(num)
# print(l1)
# 列表推导式：一行代码几乎搞定你需要的任何的列表。
    # 循环模式  [变量（加工后的变量） for 变量 in iterable]
# l = [i for i in range(1,101)]
# print(l)
# l2 = ['python%s期' % i for i in range(1,16)]
# print(l2)
# print([i*i for i in range(1,11)])
    # 筛选模式 [变量（加工后的变量） for 变量 in iterable if 条件]
# l3 = [i for i in range(1,31) if i % 2 == 0]
# print(l3)
# print([i for i in range(1,31) if i % 3 == 0])
# print([i**2 for i in range(1,31) if i % 3 == 0])
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
print([j for i in names for j in i if j.count('e') == 2])

# 列表推导式
# 优点：一行解决，方便。
# 缺点：容易着迷，不易排错，不能超过三次循环。
# 列表推导式不能解决所有列表的问题，所以不要太刻意用。

# 生成器表达式：将列表推导式的 []  换成() 即可。
# g = (i for i in range(100000000000))
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
#
# mcase = {'a': 10, 'b': 34}
# mcase_frequency = {mcase[k]: k for k in mcase}
# print(mcase_frequency)

# squared = {x**2 for x in [1, -1, 2]}
# print(squared)