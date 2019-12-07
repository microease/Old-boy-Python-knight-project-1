# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 11:55
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 04 字典的嵌套.py
# @Software: PyCharm

dic = {'name_list': ['王双', 'alex', '孙飞', 'taibai'],
       1: {'name': 'taibai', 'age': 18, 'sex': '男'},
       (1, 2): [100, {'ip': '192.168.1.1', 'port': 3306}]
       }
# 1,给 name_list对应的列表追加一个值: 司徒大人.
# print(dic['name_list'])
# dic['name_list'].append('司徒大人')
# print(dic)

# 2,将name_list对应的alex 变成全部大写.
# dic['name_list'][1] = 'ALEX'
# dic['name_list'][1] = dic['name_list'][1].upper()
# print(dic)
# 3, 将1对应的字典添加一个键值对: weight : 75
# print(dic[1])
# dic[1]['weight'] = 75
# print(dic)
# 4,将1 对应的字典的name键对应的名字taibai 换成alex
# dic[1]['name'] = 'alex'
# print(dic)
# 5,将 {'ip': '192.168.1.1', 'port': 3306} 此字典的port键值对删除.
dic[(1,2)][1].pop('port')
print(dic)