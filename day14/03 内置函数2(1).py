# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 9:23
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 03 内置函数2.py
# @Software: PyCharm

# 1.4.2和数据结构相关（24）
#
# 　　列表和元祖（2）
#
# 　　　　list：将一个可迭代对象转化成列表（如果是字典，默认将key作为列表的元素）。
#
# 　　　　tuple：将一个可迭代对象转化成元祖（如果是字典，默认将key作为元祖的元素）

# 　reversed：将一个序列翻转，并返回此翻转序列的迭代器。  *****
#

# l1 = [1,3,4,2,6]
# s1 = 'abcdefg'
# dic = {'name':'alex','age':1000,'hobby':'oldwomen'} # 不行
# print(reversed(l1))
# for i in reversed(l1):
#     print(i)
# for i in reversed(s1):
#     print(i)
# for i in reversed(dic):
#     print(i)

# 　　　　slice：构造一个切片对象，用于列表的切片。  ***
# l1 = [i for i in range(10)]
# l2 = l1[:5:2]
# l3 = [i for i in range(10,20)]
# sli_obj = slice(0,5,2)
# print(l3[sli_obj])
# l4 = ['a', 'b', 'c', 'd', 'e']
# print(l4[sli_obj])
# str：将数据转化成字符串。
#
# format:与具体数据相关，用于计算各种小数，精算等。 **
# print(format('test', '<20'))
# print(format('test', '>20'))
# print(format('test', '^20'))

# bytes：unicode ---> bytes 类型  ****
# a1 = '太白'
# # print(a1.encode('utf-8'))
# print(a1.encode('utf-8').decode())

# bytes：unicode ---> bytes 类型
# a1 = '太白'
# b1 = bytes(a1,encoding='utf-8')
# print(b1)

# a1 = -100
# b1 = -100
# print(id(a1))
# print(id(b1))

# 　bytearry：返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
    # [97,110,103,115]
# ret = bytearray('alex',encoding='utf-8')
# print(id(ret))
# print(ret)  # bytearray(b'alex')
# print(ret[0])  # 97
# ret[0] = 65
# print(ret)  # bytearray(b'Alex')
# print(id(ret))

# memoryview
# ret = memoryview(bytes('你好',encoding='utf-8'))
# print(len(ret))  # 6
# print(ret)  # <memory at 0x000001D3D6FCD048>  # [\xe4,\xbd,\xa0,\xe5,\xa5,\xbd]
# print(bytes(ret[:3]).decode('utf-8'))  # 你
# print(bytes(ret[3:]).decode('utf-8'))  # 好

# ord:输入字符找该字符编码 unicode  的位置  **
# print(ord('a'))
# print(ord('中'))
# chr:输入位置数字找出其对应的字符 unicode **
# print(chr(97))
# print(chr(20013))
# ascii:是ascii码中的返回该值，不是则返回他在unicode的位置（16进制。） **
# print(ascii('a'))
# print(ascii('中'))  # '\u4e2d'

# repr:返回一个对象的string形式（原形毕露）。  *****
# print('alex')
# print(repr("ale,x"))
# print(repr("{'alex':'sb'}"))
# repr()  json pickle序列化模块 特殊字符串，python字符串的区别
# 格式化输出 %r
# msg = 'alex 是 %r的人' % ('德高望重')
# print(msg)

#  sorted：对所有可迭代的对象进行排序操作。 *****

l1 = [2,3,5,3,1,9,8,6]
# l1.sort()
# print(l1)
# print(sorted(l1)) # 形成了一个新列表
# print(l1) # 原列表不变
#
# l2 = [(1,1000),(2,18),(4,250),(3,500)]
# print(sorted(l2))

# def func1(x):
#     return x[1]
# print(sorted(l2,key=func1,reverse=True))
#　enumerate:枚举，返回一个枚举对象。

# all：可迭代对象中，全都是True才是True  ***  多做条件判断
# l1 = [1,'',[1,3],(2,4)]
# print(all(l1))
# any：可迭代对象中，有一个True 就是True ***  多做条件判断
# print(any([1,0,'',()]))
#
# 　zip：函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。 *****
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同。
# 拉链方法  将多个iter 纵向组成一个个元组。
# l1 = [1,2,3,5,6,7]
# tu1 = ('alex','太白', 'wusir', '女神')
# dic = {'name': '日天', 'age':28, 'hobby': 'tea', 'weight':100}
# # print(zip(l1,tu1,dic))
# for i in zip(l1,tu1,dic):
#     print(i)

# 　filter：过滤· 迭代器。 *****
# l1 = [i for i in range(10)]
# def func1(x):
#     return x % 2 == 0
# print(list(filter(func1,l1)))

# map:会根据提供的函数对指定序列做映射。 循环模式
# l1 = [1,2,3,4]
# # print([i**2 for i in l1])
# def func(x): return x**2
# print(list(map(func,l1)))

# print() sum reversed
# key : min max map sorted filter zip




# 匿名函数  lambda表达式，
# 普通函数 有且只有返回值的函数才可以用匿名函数进行简化，一行函数。
# func2 = lambda x: x*2

# def func2(x):
#     return x**2

# func2 = lambda x : x**2
# print(func2(6))

# func2 = lambda x,y: x+y
# print(func2(1,2))
# 匿名函数 不单独使用，多与内置函数结合。

# l2 = [(1,1000),(2,18),(4,250),(3,500)]
# print(sorted(l2,key=lambda x:x[1]))

dic={'k1':10,'k2':100,'k3':30}
#1,利用内置函数匿名函数将dic按照值进行排序。
# print(sorted(dic,key=lambda x:dic[x]))
# print(sorted(dic.items(),key=lambda x:x[1]))
# [1,5,7,4,8]
# 利用内置函数匿名函数 计算列表的每个数的2倍。
# print(list(map(lambda x:x*2,[1,5,7,4,8])))
# [5,8,11,9,15]
# 利用内置函数匿名函数，将值大于10的留下来。
# print(list(filter(lambda x: x>10,[5,8,11,9,15])))

# func = lambda x:x if x > 2 else x * 2