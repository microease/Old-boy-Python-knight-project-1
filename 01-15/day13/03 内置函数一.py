# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 10:28
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 03 内置函数一.py
# @Software: PyCharm

'''
len()
range()
min()
max()
input()
print()
id()
type()
int()
list()
str()
set()
next()
tuple()
iter()
bool()
dict()
globals()
dir()
enmurate()
locals()
open()
send()
'''
# 作用域相关  ******
# globals() :返回一个字典：包含全部的全局变量。
# locals() ： 返回一个字典：包含的是当前作用域 所有的变量。
# b = 2
# def func1():
#     a = 1
#     print(locals())
#     print(globals())
# func1()
# 1.2其他相关  不建议使用 ***
# 1.2.1 字符串类型代码的执行 eval，exec，complie
# eval: 执行字符串类型的代码，并返回最终结果
# s1 = '1+2+3'
# # print(s1)
# # s2 = "{'name':'alex'}"
# # print(eval(s1),type(eval(s1)))
# # print(eval(s2),type(eval(s2)))
# # exec 执行字符串类型的代码，不返回结果  代码流
# s3 = '''for i in range(3):
#     print(i)
# '''
# # print(exec(s1))
# exec(s3)

# complie 了解

# #
# 1.2.2 输入输出相关 input，print  *****
#
# 　　input:函数接受一个标准输入数据，返回为 string 类型。
#
# 　　print:打印输出。
# print('666')
# print(1,2,3,4)
# print(*[1,2,3])
# def func1(*args,**kwargs):  # 函数的定义：*聚合。
    # print(*args)   # (*(1,2,3,4))函数的执行： * 打散  print(1,2,3,4)
    # print(**kwargs) # print(name='alex',age=1000)
    # print(kwargs)
# func1(1,2,3,4,name='alex',age=1000)
# print(1,2,3,sep='|')  # sep 打印多个内容是分隔符默认是空格
# print(1,end=' ')  # end：默认换行
# print(222)
# f = open('t1',encoding='utf-8',mode='w')
# print(666,'777','888',file=f)

# 1.2.3内存相关 hash id ***
#
# 　　hash：获取一个对象（可哈希对象：int，str，Bool，tuple）的哈希值。
#     id:获取该对象的内存地址。

# hash()
# 字典：会将你的所有的key 在内存中转化成id
# dic = {'name':'alex','kfdshjfhdskjfhsd': '123'}
# print(hash('name'))
# print(hash('name1'))
# print(hash('fdsmkfghsdlksld'))
# print(hash(1))
# print(hash(100))
# print(hash(100000000000))
# print(hash([1,2,3]))
# 1.2.3文件操作相关
#
# 　　open：函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。 *****
#
# 1.2.4模块相关__import__　 ***
#
# 　　__import__：函数用于动态加载类和函数 。

# 1.2.5帮助
#
# 　　help：函数用于查看函数或模块用途的详细说明。 **
# name = 'alex'
# print(help(str))

# 1.2.6调用相关
#
# 　　callable：函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；
# 但如果返回False，调用对象ojbect绝对不会成功。  ***
# name = 'alex'
#
# def func1():
#     pass
# print(callable(name))  # False
# print(callable(func1))  # True # 可以被调用
#
# 1.2.7查看内置属性  ***
#
# 　　dir：函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
# 如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
# name = 'alex'
# print(dir(name))

# range：函数可创建一个整数对象，一般用在 for 循环中。
#  python2x: range(3) ---> [0,1,2] 列表
#            xrange(3) ---> 迭代器。
#  python3x: range(3) ---> range(0,3) 可迭代对象

# 　　next：内部实际使用了__next__方法，返回迭代器的下一个项目。
# 　　iter：函数用来生成迭代器（讲一个可迭代对象，生成迭代器）。

# 1.4 .1
# 数字相关（14）

# 　　数据类型（4）：

# 　　　　bool ：用于将给定参数转换为布尔类型，如果没有参数，返回False。 ***
# print(bool(1 < 2 and 3 > 4 or 5 < 6 and 9 > 2 or 3 > 1))
# print(bool('fdsjkfl'))
# 　　int：函数用于将一个字符串或数字转换为整型。***
# print(int('123'))
# print(int(3.74)) # 取整 不是四舍五入
# print(int('0101',base=2))  # 将2进制的 0100 转化成十进制。结果为 4
# 　　float：函数用于将整数和字符串转换成浮点数。 ***
# print(type(3.14))
# 　　　complex：函数用于创建一个值为real + imag * j的复数或者转化一个字符串或数为复数。
# 如果第一个参数为字符串，则不需要指定第二个参数。。

#  进制转换（3）：
#
# 　　　　bin：将十进制转换成二进制并返回。
# print(bin(100))  # 0b1100100
# # 　　　　oct：将十进制转化成八进制字符串并返回。
# # print(oct(7))  # 0o7
# # print(oct(8))  # 0o10
# # print(oct(9))  # 0o10
# # 　　　　hex：将十进制转化成十六进制字符串并返回。
# print(hex(10)) # 0xa
# print(hex(15)) # 0xf
# print(hex(17)) # 0xf
# 数学运算（7）：
#
# 　　　　abs：函数返回数字的绝对值。 ****
# print(abs(-100))
# #
# # 　　　　divmod：计算除数与被除数的结果，返回一个包含商和余数的元组(a // b, a % b)。 ****
# print(divmod(12,7))  # (1, 5) (商，余数)
# # 分页。
#     # 103 条数据，你每页显示12 条数据，你最终显示多少页。
# print(divmod(103,12))
# 　　　　round：保留浮点数的小数位数，默认保留整数,四舍五入。  ***
# print(round(3.141592653,4))
#
# 　　　　pow：求x**y次幂。（三个参数为x**y的结果对z取余） **
# print(pow(2,5))
# print(pow(2,5,12))
# 　　　　sum：对可迭代对象进行求和计算（可设置初始值）。 *****
#sum(iterable,start_num)
# print(sum([1,2,3,4,100,101]))
# print(sum([1,2,3,4,100,101],100))
# print(sum([int(i) for i in [1,'2',3,'4','100',101]]))

# 　　　　min：返回可迭代对象的最小值（可加key，key为函数名，通过函数的规则，返回最小值）。 *****
# print(min([1,-2,3,4,100,101]))
# print(min([1,-2,3,4,100,101]))
# print(min([1,-2,3,4,100,101],key=abs))
# [('alex',1000),('太白',18),('wusir',500)]
# 求出年龄最小的那个元组
# ls = [('alex',1000),('太白',18),('wusir',500)]
# min1 = min([i[1] for i in ls])
# for i in ls:
#     if i[1]==min1:
#         print(i)
# def func(x):
#     return x[1]  # 1000  18  500
# print(min([('alex',1000),('太白',18),('wusir',500)],key=func))
# # 1,他会将iterable的每一个元素当做函数的参数传进去。
# 2，他会按照返回值去比较大小。
# 3,返回的是 遍历的元素 x.

# dic = {'a':3,'b':2,'c':1}
# def func1(x):
#     return dic[x]
# print(min(dic,key=func1))
# def func2(x):
#     return x[1]
# print(min(dic.items(),key=func2))

# 　　　　max：返回可迭代对象的最大值（可加key，key为函数名，通过函数的规则，返回最大值）。 *****
# print(max([1,2,3,100]))
