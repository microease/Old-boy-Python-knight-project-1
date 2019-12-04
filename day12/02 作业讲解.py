# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 9:27
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 02 作业讲解.py
# @Software: PyCharm

'''
11,写函数，传入一个参数n，返回n的阶乘
例如:cal(7)  计算7*6*5*4*3*2*1
# 7*6*5*4*3*2*1

# 7+6+...+1
# def sum1(n):
#     s = 0
#     for i in range(n,0,-1):
#         s = s + i
#     return s
# print(sum1(8))

# def sum1(n):
#     s = 1
#     for i in range(n,0,-1):
#         s = s * i
#     return s
# print(sum1(8))
12写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组（升级题）
例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]

'''

# [(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]

# def poker(argv):
#     l1 = []
#     for num in range(1,14):
#         for i in argv:
#             l1.append((i,num))
#     return l1
# print(poker(['黑桃','红心', '草花', '方块']))
def calc(a,b,c,d=1,e=2):
    return a+b+c+d+e
# 请分别写出下列标号代码的输出结果，如果出错请写出Error。

# print(calc(1,2,3,4,5))  # 15
# print(calc(1,2))  # 报错 位置参数一一对应
# print(calc(e=4,c=5,a=2,b=3)) # 15
# print(calc(1,2,3))  # 9
# print(calc(1,2,3,e=4))  # 11
# print(calc(1,2,3,d=5,4))  # 15
# def extendList(val,list=[]):
#     list.append(val)
#     return list
# list1 = extendList(10)  # [10,]  list
# list2 = extendList(123,[]) # [123.]
# list3 = extendList('a')  # [10,'a']  list
#
# print('list1=%s'%list1)  # [10,'a']
# print('list2=%s'%list2) # [123.]
# print('list3=%s'%list3)  # [10,'a']  list


# def extendList(val,list=[]):
#     list.append(val)
#     return list
# list1 = extendList(10)
# print('list1=%s'%list1)  # [10,]
# list2 = extendList(123,[])
# print('list2=%s'%list2)  # [123,]
# list3 = extendList('a')
# print('list3=%s'%list3) # ['a']  [10,'a']


