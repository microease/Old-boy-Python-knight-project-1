# # -*- coding: utf-8 -*-
# # @Time    : 2018/8/23 9:26
# # @Author  : 骑士计划
# # @Email   : customer@luffycity.com
# # @File    : 02 作业讲解.py
# # @Software: PyCharm
#
# Day14 作业及默写
# 1.整理今天所学内容，整理知识点，整理博客。
#
# 2.画好流程图。
#
# 3.都完成的做一下作业（下面题都是用内置函数或者和匿名函数结合做出）：
#
# 4.用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
# name=['oldboy','alex','wusir']
# # print([i+'_sb' for i in name])
# print(list(map(lambda x:x+'_sb',name)))


# 5.用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
# l=[{'name':'alex'},{'name':'y'}]
# # print([i['name']+'sb' for i in l])
# print(list(map(lambda x:x['name']+'sb',l)))
# 6.用filter来处理,得到股票价格大于20的股票名字
# shares={
#    	'IBM':36.6,
#    	'Lenovo':23.2,
#   	'oldboy':21.2,
#     'ocean':10.2,
# 	}
#
# 7.有下面字典，得到购买每只股票的总价格，并放在一个迭代器中。
# 结果：list一下[9110.0, 27161.0,......]
# portfolio = [
#   {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}]
#
# 8.还是上面的字典，用filter过滤出单价大于100的股票。
#
# 9.有下列三种数据类型，
l1 = [1,2,3,4,5,6]
l2 = ['oldboy','alex','wusir','太白','日天']
tu = ('**','***','****','*******')
# 写代码，最终得到的是（每个元祖第一个元素>2,第三个*至少是4个。）
# 	[(3, 'wusir', '****'), (4, '太白', '*******')]这样的数据。
# print(list(zip(l1,l2,tu)))
# zip(l1,l2,tu)
# print(list(filter(lambda x: x[0] > 2 and len(x[-1]) >= 4,zip(l1,l2,tu))))
#
#
# 10.有如下数据类型：
l1 = [ {'sales_volumn': 0},
     		{'sales_volumn': 108},
     		{'sales_volumn': 337},
     		{'sales_volumn': 475},
     		{'sales_volumn': 396},
     		{'sales_volumn': 172},
     		{'sales_volumn': 9},
     		{'sales_volumn': 58},
     		{'sales_volumn': 272},
     		{'sales_volumn': 456},
     		{'sales_volumn': 440},
     		{'sales_volumn': 239}]

# 将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。
# print(sorted(l1,key=lambda x:x['sales_volumn']))
# 11. 求结果
# func = lambda :x
# v = [lambda :x for x in range(10)]
# # 只要这样写，在内存中x 已经定格在9值,
# # [func1,func2,func3.....func10]
# print(v)
# # print(v[0])
# print(v[0]())
#
# 12. 求结果
# v = (lambda :x for x in range(10))
# print(v)
# print(v[0])
# print(v[0]())
# print(next(v))
# print(next(v)())
#
#
# 生成器：close()

# def func():
#     for i in range(6):
#         yield i
# g = func()
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
#
# try:
#     print(g.close())
# except StopIteration:
#     print(g)
# print(list(g))

# g.close()
# # print(g.__next__())
# print(g.__next__())
