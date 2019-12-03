# -*- coding: utf-8 -*-
# @Time    : 2018/8/9 12:01
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 04 编码.py
# @Software: PyCharm

# b1 = b'alex'
# b2 = b1.upper()
# s1 = 'alex'
# print(b1, type(b1))
# print(b2, type(b2))
# print(s1, type(s1))

# s1 = '太白'
# b1 = s1.encode('utf-8')
# b2 = s1.encode('gbk')
# print(b1)  # b'\xe5\xa4\xaa\xe7\x99\xbd'
# print(b2)

# str --- > bytes encode 编码
# s1 = 'alex'
# s2 = '太白'
# b1 = s1.encode('utf-8')
# print(b1)
# b2 = s2.encode('gbk')
# print(b2)

# bytes ---> str decode 解码
b1 = b'\xcc\xab\xb0\xd7'  # gbk 的bytes
s2 = b1.decode('gbk')
print(s2)