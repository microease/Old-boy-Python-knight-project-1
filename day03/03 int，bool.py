# -*- coding: utf-8 -*-
# @Time    : 2018/8/6 10:39
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 03 int，bool.py
# @Software: PyCharm

# int
i = 4
# print(i.bit_length()) # 查询十进制转化成二进制占用的最小位数  *
'''
十进制         二进制
1              0000 0001
2              0000 0010
3              0000 0011
4              0000 0100
....
'''

# bool
# 数据类型之间的转化。 *****
# int ---> str   str(int)   int(str)
# int ----> bool : 非零及True,零即为False，    True  ---> 1  False  ----> 0
# bool <---> str:
# print(bool('alex'))
# print(bool('alexsb'))
# str ---> bool 空字符串 bool False ,非空即True
# s1 = ' '
# print(bool(s1))
# name = input(">>>")
# if name:
#     print('666')
# else:
#     print('无内容')

# bool ---> str
# print(str(True),type(str(True)))