# # -*- coding: utf-8 -*-
# # @Time    : 2018/8/21 9:30
# # @Author  : 骑士计划
# # @Email   : customer@luffycity.com
# # @File    : 02 作业讲解.py
# # @Software: PyCharm
#
#
# Day12作业默写
# 1，整理今天的博客，写课上代码，整理流程图。
# 2，用列表推导式做下列小题
# (1)	过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# (2)	求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的 元祖 列表
# l1 = [(),(),....]
# print([(2*x,2*x+1) for x in range(0,3)])
# print([(x,y) for x in range(0,6) if x % 2 == 0 for y in range(0,6) if y % 2 == 1])
# print([(x,y) for x in range(0,5,2)for y in range(1,6,2)])
# (3)	求M中3,6,9组成的列表M = [[1,2,3],[4,5,6],[7,8,9]]
# M = [[1,2,3],[4,5,6],[7,8,9]]
# print([x[-1] for x in M])
# print([[x-2,x-1,x] for x in [3,6,9]])

# (4)	求出50以内能被3整除的数的平方，并放入到一个列表中。
# (5)	构建一个列表：
# ['python1期', 'python2期', 'python3期', 'python4期', 'python6期', 'python7期', 'python8期', 'python9期', 'python10期']
# (6)	构建一个列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# (7)	构建一个列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# (8)	有一个列表l1 = ['alex', 'WuSir', '老男孩', '太白']
# 将其构造成这种列表['alex0', 'WuSir1', '老男孩2', '太白3']
# (9)有以下数据类型：
x = {
    'name':'alex',
    'Values':[{'timestamp':1517991992.94,
         'values':100,},
        {'timestamp': 1517992000.94,
        'values': 200,},
        {'timestamp': 1517992014.94,
         'values': 300,},
        {'timestamp': 1517992744.94,
         'values': 350},
        {'timestamp': 1517992800.94,
         'values': 280}
		],}
# 将上面的数据通过列表推导式转换成下面的类型：
# [[1517991992.94, 100], [1517992000.94, 200], [1517992014.94, 300], [1517992744.94, 350], [1517992800.94, 280]]
# print([[i['timestamp'],i['values']] for i in x['Values']])


# 3，求结果：
# v = [i % 2 for i in range(10)]
# print(v)
#
#
# 4，求结果:
# v = (i % 2 for i in range(10))
# print(v)
#
# 5，求结果：
#
# def func1():
#     for i in range(5):
#         print(i)
# print(i)
#
#
#
