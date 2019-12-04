# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 10:32
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 03 函数.py
# @Software: PyCharm

s = 'fjkdsfljsdklfjskdfdsfsdafsd'
# count = 0
# for i in s:
#     count += 1
# print(count)

# l = [1, 2, 3, 4]
# # count = 0
# # for i in l:
# #     count += 1
# # print(count)
#
# # def 关键字 函数名：
# def my_len():
#     #函数体
#     l = [1, 2, 3, 4]
#     count = 0
#     for i in l:
#         count += 1
#     print(count)
#
# my_len()  # 执行函数 函数名 ()
# 函数的优点：
# 减少代码的重复率。
# 增强代码的阅读性。

# 函数到底是什么？ 函数最主要的目的：封装一个功能。


#
# s = 'fjkdsfljsdklfjskdfdsfsdafsd'
# print(len(s))

# def my_len():
#     #函数体
#     s = 'fjkdsfljsdklfjskdfdsfsdafsd'
#     count = 0
#     for i in s:
#         count += 1
#     print(count)
# # print(my_len())

# 函数的返回值 return
# 1,函数中如果遇到retrun,则直接结束函数。
# 2，给函数的执行者返回值。
    # return                    None
    # return 单个值            原封不动的返回
    # return 多个值            一个元组，所有的返回值作为元组的每一个元素
# def func1():
#     print(111)
#     print(222)
#     return
#     print(333)
# print(func1())  # 整体是函数的执行者。

# def func1():
#     a = 1
#     b = 2
#     c = a + b
#     d = 'alex'
#     e = [1,2,3]
#     return c,d,e
# ret = func1()
# print(ret,type(ret))  # 整体是函数的执行者。
# 工作中，函数中尽量不要出现print
# def my_len():
#     #函数体
#     s = 'fjkdsfljsdklfjskdfdsfsdafsd'
#     count = 0
#     for i in s:
#         count += 1
#     return count
# print(my_len())

# 函数的传参：
    #实参
        # 位置参数  按照顺序，一一对应
        # 关键字参数  可以不按照顺序，但是必须一一对应
        # 混合参数   关键字参数一定要在位置参数后面
    #形参
        # 位置参数  按照顺序，一一对应
        # 默认参数

# l1 = [1,2,3]
# s = 'fjkdsfljsdklfjskdfdsfsdafsd'
# def my_len(argv):  # 形式参数，形参
#     #函数体
#     count = 0
#     for i in argv:
#         count += 1
#     return count
# # print(my_len(l1)) # 函数的执行者（实参） 实际的参数
# print(my_len(s)) # 函数的执行者（实参） 实际的参数
# print(len(s))

# 实参
    # 位置参数  按照顺序，一一对应

#
# def func1(x,y):
#     print(x,y)
#
# func1(1,2)
# 2个函数： 1个函数 求和； 2个函数 将大的数给我返回

# def sum1(x,y):
#     return x+y
#
# a = 3
# b = 6
# print(sum1(a,b))
# def compare(x,y):
#     # if x > y:
#     #     return x
#     # else:
#     #     return y
#     #
#     # ret = x if x > y else y
#     return x if x > y else y
# print(compare(1001,100))

#三元运算：只针对于简单的if else 这样的结构，才可以使用。

# 关键字传参 可以不按照顺序，但是必须一一对应

# def func1(x,y):
#     return x+y
# print(func1(y=100,x=99))

# 混合传参： 关键字参数一定要在位置参数后面

# def func1(a,y,n,x,n):
#     return x+y
#
# name = 'alex'
# print(func1(100,200,name,y=100,x=99))

# 形参角度
    # 位置参数 按照顺序，一一对应
    # 默认参数：给其传值，将原默认参数覆盖掉，不传值，不报错，使用默认值
        # 应用场景：不经常改变的参数，但是一直在用。
# def func(x,y,z):
#     print(x,y,z)
# func(1,2,3)

# def func1(x,y,a=666):
#     print(x,y,a)
# func1(1,2)
# func1(1,2,333)
def namelist(n1,s1='男'):
    with open('namelist',encoding='utf-8',mode='a') as f1:
        f1.write('{}|{}\n'.format(n1,s1))

while 1:
    name,sex = input('请输入姓名，性别：以 ,隔开').strip().replace('，',',').split(',')
    if name.upper() == 'Q':break
    if sex.strip():
        namelist(name,sex)
    else:
        namelist(name)

# 默认参数的陷阱
# 默认参数若是可变的数据类型，他始终使用的是一个。
# def func1(x,l1=[]):
#     l1.append(x)
#     return l1
# ret = func1(1)
# print(ret,id(ret))
# ret1 = func1(100)
# print(ret1,id(ret1))
