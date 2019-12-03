# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 16:41
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : day08 作业讲解.py
# @Software: PyCharm
# import os
# # with open('a1',encoding='utf-8',) as f1,\
# #     open('a1.bak',encoding='utf-8',mode='w') as f2:
# #     for line in f1:
# #         if line.strip() == '我说的都是真的。哈哈':
# #             n_line = '你们就信吧\n' + line
# #             f2.write(n_line)
# #         else:
# #             f2.write(line)
# # os.remove('a1')
# # os.rename('a1.bak','a1')



# [{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......]
# l1 = []
#
# with open('a', encoding='utf-8') as f1:
#     for line in f1:
#         if line.strip():
#             line_list = line.strip().split()  # [apple,10,3,2018]
#             print(line_list)
#             dic = {'name':line_list[0],'price':line_list[1],'amount':line_list[2],'year':line_list[3]}
#             l1.append(dic)
# print(l1)
name_list = ['name','price','amount','year', '备注']
l1 = []
with open('a', encoding='utf-8') as f1:
    for line in f1:
        if line.strip():
            line_list = line.strip().split()  # [apple,10,3,2017]
            dic = {}
            for index in range(len(name_list)):
                dic[name_list[index]] = line_list[index]
            l1.append(dic)
print(l1)

