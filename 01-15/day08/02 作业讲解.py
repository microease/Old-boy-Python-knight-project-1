# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 9:08
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 02 作业讲解.py
# @Software: PyCharm

# dic = dict.fromkeys([1,2,3],[])
# print(dic)
# print(id(dic[1]))
# print(id(dic[2]))
# print(id(dic[3]))

# dic = dict.fromkeys('1234','alex')
# dic['1'] = 'egon'
# print(dic)    结果# {'1': 'egon', '2': 'alex', '3': 'alex', '4': 'alex'}


# dic = dict.fromkeys('1234',[])
# dic['1'] = 'egon'
# print(dic)      结果# {'1': 'egon', '2': [], '3': [], '4': []}


# dic = dict.fromkeys('1234',[])
# dic['2'].append('msr')
# print(dic)      结果 #{'1': ['msr'], '2': ['msr'], '3': ['msr'], '4': ['msr']}

# l1 = [1, 2, 3,['taibai',]]
# l2 = l1.copy()
# print(l1 is l2)  # 内存中两个列表不是一个。
# print(id(l1[1]))
# print(id(l2[1]))
# print(id(l1[-1]))
# print(id(l2[-1]))
# import copy
# l1 = [1, 2, 3,['taibai',]]
# l2 = copy.deepcopy(l1)
# print(id(l1))
# print(id(l2))
# print(id(l1[-1]))
# print(id(l2[-1]))
import copy
# d1 = {'name':"alex"}
# d2 = copy.deepcopy(d1)
# print(id(d2),id(d1))

# d1 = 'alex'
# d2 = copy.deepcopy(d1)
# print(id(d2),id(d1))

#
# 4，电影投票.程序先给出⼀个⽬前正在上映的电影列表.由⽤户给每⼀个电影投票.最终
# 将该⽤户投票信息公布出来 。（此题明天可以继续做）
# 要求：
# 1，用户输入序号，进行投票。比如输入序号
# 1，给金瓶梅投票1。
# 2，每次投票成功，显示给哪部电影投票成功。
# 3，退出投票程序后，要显示最终每个电影的投票数。
# 结果: {'⾦瓶梅': 99, '解救吴先⽣': 80, '美国往事': 6, '⻄⻄⾥的美丽传说': 23}
# lst = ['⾦瓶梅', '解救吾先⽣', '美国往事', '⻄⻄⾥的美丽传说']
# dic = {'⾦瓶梅': 0, '解救吾先⽣': 0, '美国往事': 0, '⻄⻄⾥的美丽传说': 0}
#
# while 1:
#     for index,name in enumerate(lst,1):
#         print('投票序号：%s,投票电影：%s' %(index,name))
#     num = input('请输入你投票的电影序号：(Q或者q退出)').strip()
#     if num.isdigit():
#         if 0 < int(num) <= len(lst):
#             dic[lst[int(num)-1]] += 1
#             print('感谢您，为%s投票'%lst[int(num)-1])
#         else:
#             print('没有此序号。。。。')
#     elif num.upper() == 'Q': break
#     else:
#         print('请输入数字')
# print("'⾦瓶梅': %(⾦瓶梅)s, '解救吾先⽣': %(解救吾先⽣)s, '美国往事': %(美国往事)s\
# , '⻄⻄⾥的美丽传说': %(⻄⻄⾥的美丽传说)s" %dic)


lst = ['周⽼⼆', '周星星', '麻花藤', '周扒⽪']
for i in lst[:]:
    if '周' == i.strip()[0]:
        lst.remove(i)
print(lst)
