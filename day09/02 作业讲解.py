# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 9:07
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 02 作业讲解.py
# @Software: PyCharm

# with open('a1',encoding='utf-8',mode='w') as f1:
#     f1.write('666')
#     f1.write('666')
#     f1.write('666')
#     f1.write('6668888')
#     f1.close()
#
# f = open('a1',encoding='utf-8',mode='w')
# f.write('1111')
# f.write('1111')
# f.write('1111')
# f.write('1111')
# f.write('1111')
# f.close()

#[{'name':'apple','price':10,'amount':3,'year':},
#{'name':'tesla','price':1000000,'amount':1}......]
# l1 = []
# with open('a2',encoding='utf-8',mode='r') as f1:
#     for line in f1:
#         line_list = line.strip().split()  # ['name:apple', 'price:10', 'amount:3', 'year:2012']
#         dic = {}
#         for i in line_list:
#             # print(i)  # 'name:apple'
#             key,value = i.split(':')  # [name,apple]
#             dic[key] = value
#         l1.append(dic)
# print(l1)


list3 = [
    {"name": "alex", "hobby": "抽烟"},
    {"name": "alex", "hobby": "喝酒"},
    {"name": "alex", "hobby": "烫头"},
    {"name": "alex", "hobby": "Massage"},
    {"name": "wusir", "hobby": "喊麦"},
    {"name": "wusir", "hobby": "街舞"},
    {"name": "wusir", "hobby": "唱歌"},
    {"name": "太白", "hobby": "开车"},
]
list4 = [
    {"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]},
    {"name": "wusir", "hobby_list": ["喊麦", "街舞"]},
]
# 将list3 这种数据类型转化成list4类型,你写的代码必须支持可拓展,
# 比如list3 数据在加一个这样的字典{"name": "wusir", "hobby": "溜达"},	你的list4{"name": "wusir", "hobby_list": ["喊麦", "街舞", "溜达"],
# 或者list3增加一个字典{"name": "太白", "hobby": "开车"},
# 你的list4{"name": "太白", "hobby_list": ["开车"],无论按照要求加多少数据,你的代码都可以转化.如果不支持拓展,则4分,支持拓展则8分.

# {'alex':{"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]
#     'wusir':{"name": "wusir", "hobby_list": ["喊麦", "街舞"]}
# }
# dic = {}
# for i in list3:
#     if i['name'] not in dic:
#         dic[i['name']] = {'name':i['name'],'hobby_list':[i['hobby'],]}
#     else:
#         dic[i['name']]['hobby_list'].append(i['hobby'])
# print(list(dic.values()))