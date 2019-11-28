# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 11:57
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 04 格式化输出.py
# @Software: PyCharm

#
# name = input('请输入姓名：')
# age = int(input('请输入年龄：'))
# sex = input('请输入性别：')
# % 占位符  s 数据类型为字符串 d 数字
# 第一种方式：
# msg = '你的名字是%s，你的年龄%d,你的性别%s' % (name,age,sex)
# print(msg)

# 第二种方式
# msg = '你的名字是%(name1)s，你的年龄%(age1)d,你的性别%(sex1)s' % {'name1':name,'age1':age,'sex1':sex}
# print(msg)

# bug 点  在格式化输出中，只想单纯的表示一个%时，应该用%% 表示
# msg = '我叫%s，今年%d，我的学习进度1%%' % ('关亮和',28)
# print(msg)