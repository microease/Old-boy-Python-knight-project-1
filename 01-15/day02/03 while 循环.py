# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 10:32
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 03 while 循环.py
# @Software: PyCharm

# while True:  # 死循环
#     print('大悲咒')
#     print('两只老虎')
#     print('大王别姬')
#     print('老司机带带我')

# while 循环的结构：
'''
while 条件:
    循环体
'''

# 如何终止循环？
# 1，改变条件 （标志位的概念）
# 2, break 终止循环。
# flag = True
# while flag:
#     print('大悲咒')
#     print('两只老虎')
#     flag = False
#     print('大王别姬')
#     print('老司机带带我')

# 练习 1 ---100
# 1
# 2
# 3
# ...
# 100
# 方法1：
# flag = True
# count = 1
# while flag:
#     print(count)
#     count = count + 1
#     if count == 101:
#         flag = False

# 方法2：
# count = 1
# while count < 101:
#     print(count)
#     count = count + 1

# break 循环中只要遇到break 立马结束循环。

# while True:
#     print(111)
#     print(222)
#     break
#     print(333)
#     print(444)
# print(123)

# 利用break，while, 计算 1 + 2 + 3 ....100 的结果

# count = 1
# sum = 0
# while True:
#     sum = sum + count
#     count = count + 1
#     if count == 101:
#         break
# print(sum)

# continue: 结束本次循环，继续下一次循环。

# while True:
#     print(111)
#     print(222)
#     continue
#     print(333)

# while else  结构

# 如果while循环被break打断，则不执行else代码。
# count = 1
# while count < 5:
#     print(count)
#     count = count + 1
#     if count == 3: break
# else:
#     print(666)
# print(222)

# 应用场景：
#     验证用户名密码，重新输入这个功能需要while循环。
#     无限次的显示页面，无限次的输入......