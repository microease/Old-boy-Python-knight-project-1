# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 15:31
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 7.试题讲解.py
# @Software: PyCharm

# def outer():
#     name = 'alex'
#     print(name)
#     def inner():
#         # name = 'wupeiqi'
#         print(name)
#     print(inner.__closure__)  # inner是一个闭包
#
# outer()

# 闭包 ： 装饰器
    #     做缓存
# from urllib.request import urlopen
#
#
# # 爬虫 ： 网页有很多数据，把网页上的数据爬下来
# def get_url(url):
#     ret = urlopen(url)
#     content = ret.read().decode('utf-8')
#     def get():return content
#     return get
#
# get = get_url('http://www.cnblogs.com/Eva-J/p/7277026.html')
# get()

# print(type((3)))
# print(type((3,)))

# 'abdaadf'
# dic = {}
# for i in 'abdaadf':
#     if i in dic:
#         dic[i] +=1
#     else:
#         dic[i] = 1
# res = []
# for k in dic:
#     res.append('%s:%s'%(k,dic[k]))
# print('|'.join(res))


# dic = {}
# for i in 'abdaadf':
#     dic[i] = dic[i] +1 if i in dic else 1
# print('|'.join(['%s:%s'%(k,dic[k]) for k in dic]))

# str1 = 'abdaadf'
# print(''.join(['%s:%s|'%(i,str1.count(i)) for i in set(str1)])[:-1])

# for
dicta = {"a":1,"b":2,"c":3,"d":4,"f":"hello"}  # a b c d f
dictb = {"b":3,"d":5,"e":7,"m":9,"k":"world"}
# for
# for k in dicta:
#     if k in dictb:
#         dicta[k] += dictb[k]
# # for
# for k in dictb:
#     if k not in dicta:
#         dicta[k] = dictb[k]
# print(dicta)

# for k in dicta:
#     if k in dictb:
#         dicta[k] += dictb[k]
#         dictb.pop(k)
# dicta.update(dictb)
# print(dicta)

# def func1(a,b):
#     for i in b:
#         if i in a:
#             a[i] += b[i]
#         else:
#             a[i] = b[i]
#     return a
# dicta = {"a":1,"b":2,"c":3,"d":4,"f":"hello"}
# dictb = {"b":3,"d":5,"e":7,"m":9,"k":"world"}
# print(func1(dicta,dictb))

# x = {'a':1,'b':2,'c':3,'d':4,'f':'ew'}
# y = {'a':1,'b':2,'c':3,'e':4,'f':'wefew'}
#
# def func(a,b):
#     dic = dict.fromkeys(a.keys() | b.keys())
#     d =  {i: a[i]+b[i] if a.get(i) and b.get(i) else a[i] if a.get(i) else b[i]   for i in dic}
#     print(d)
# func(x,y)

# 16、写函数，完成给一个列表去重的功能。（不能使用set集合）（8分）
# lst = [1,2,3,4,5,1,2,3,4]
# new_lst = []
# for i in new_lst:
#     if i not in new_lst:
#         new_lst.append(i)



