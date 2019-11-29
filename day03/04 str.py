# -*- coding: utf-8 -*-
# @Time    : 2018/8/6 11:08
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 04 str.py
# @Software: PyCharmf


# 对字符串的下面这两部分操作：形成的都是一个新的字符串，与原来的字符串没有关系。
# 第一部分：索引切片步长。
# 按照索引取值,取出来的都是一个字符，形成的字符串。
# s1 = 'python1期骑士计划'
# s2 = s1[0]
# # print(s2,type(s2))
# s3 = s1[2]
# print(s3)
# s4 = s1[4]
# s5 = s1[-1]
# # print(s4)
# print(s5)
# print(s1[-2])
# 按切片取值,顾头不顾腚
# s5 = s1[0:6]
# s51 = s1[:6]
# # print(s5,s51)
# # print(s1[1:7])
# s6 = s1[6:-1]
# s61 = s1[6:]
# s62 = s1[6:-2]
# print(s6,s61,s62)

# 按照切片+步长
# s7 = s1[:5:2]
# print(s7)
# s8 = s1[1::2]
# print(s8)
# 如果想倒叙取值，加一个反向步长(负号)。
# s9 = s1[-1:-5:-1]
# s10 = s1[-1:-6:-2]
# print(s9,s10)






# 第二部分：字符串的常用方法。
name = 'oldBoy'
# capitalize() 首字母大写  ***
# print(name.capitalize())

# center 字符串居中前后填充自定义的字符  **
# print(name.center(20,'*'))

# upper：全大写 lower  *****
# print(name.upper())
# print(name)
# print(name.lower())
# 应用举例：
# username = input('请输入用户名：')
# code = 'ADfer'.upper()
# your_code = input('请输入验证码:').upper()
# print(code, your_code)
# # if username == 'alex' and (your_code == 'ADFER' or ..or....
# if username == 'alex' and your_code == code:
#     print('账号密码及验证码输入正确')

# startswith  endswith  *****
# print(name.startswith('o'))
# print(name.startswith('ol'))
# print(name.startswith('B',3))
# print(name.startswith('B',3))
# print(name.startswith('ld', 1, 5))
# print(name.startswith('oldBOy'))
# print(name.endswith('o'))

# swapcase 大小写翻转 **
# print(name.swapcase())
# s1 = 'alex wusir*taibai6nvshen'
#
# # title 非字母隔开的每个部分的首字母大写  **
# print(s1.title())

# find  通过元素找索引,找到第一个就返回，没有此元素则返回-1  *****
# index 通过元素找索引,找到第一个就返回，没有此元素则报错 *****
# print(name.find('B'))
# print(name.find('ld'))
# print(name.find('o'))
# print(name.find('d',1,-1))
# print(name.index('q'))

# name = '\t    oldboy\n'
# print(name)
# strip 默认去除字符串前后的空格，换行符，制表符  *****
# name1 = '*alex**'
# name2 = 'weralexwqwe'
# print(name.strip())
# print(name1.strip('*'))
# print(name2.strip('erw'))  # 可以指定字符
# lstrip() rstrip()  课下练习
# 举例：
# username = input('请输入用户名：').strip()  # 'alex '
# if username == 'alex':
#     print('登陆成功...')


# split  # 将字符串分割成列表（str---> list）
# s1 = 'alex wusir taibai'
# l1 = s1.split() # 默认按照空格分隔
# print(l1)
# s2 = 'alex，wusir，taibai'
# print(s2.split('，'))
# s3 = ',alex,wusir,taibai'
# print(s3.split(','))
# s4 = ' alex wusir taibai'
# print(s4.split(' '))
# s5 = 'alexlwle'
# print(s5.split('l',1)) # 可设置分割次数
# 课下自己练习：
# print(s5.rsplit())

# str1 = 'alex'
# # join 自定制连接符，将可迭代对象中的元素连接起来 *****
# s2 = '*'.join(str1)
# s2 = '_'.join(str1)
# print(s2)

# str2 = 'alex 是创始人,alex很nb，alex ....'
# # replace  *****
# # s3 = str2.replace('alex','SB')
# s3 = str2.replace('alex','SB',1)  # 替换次数可设置
# print(s3)


# 格式化输出：format
# s1 = '我叫{},今年{}，性别{}'
# 三种方式
# 第一种
# s2 = '我叫{},今年{}，性别{}'.format('太白','28','男')
# print(s2)
# 第二种
# s3 = '我叫{0},今年{1}，性别{2}，我依然叫{0}'.format('太白', '28', '男')
# print(s3)

# 第三种
# s4 = '我叫{name},今年{age}，性别{sex}'.format(age='28', name='太白', sex='男')
# print(s4)


# is 系列
# name = 'taibai'
# name1 = 'a123'
# print(name.isalnum())  # 数字或字母组成
# print(name1.isdigit())  # 判断全部是由整数组成
# print(name.isalpha())  # 全部由字母组成

# 公共方法
# name = 'alexaaa'
# # print(name.count('a'))  # 有切片
# print(len(name))

s1 = 'fdjsafjsdkla'
# while 循环
#
f
d













