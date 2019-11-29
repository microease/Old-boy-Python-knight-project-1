# -*- coding: utf-8 -*-
# @Time    : 2018/8/6 8:51
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 02 作业讲解.py
# @Software: PyCharm

# count = 1
# # while count < 4:
# #     print(count)
# #     count += 1
# #     break
# # else:
# #     print(666)


# 7、使用while循环输出 1 2 3 4 5 6 8 9 10
# count = 1
# while count < 11:
#     if count == 7:
#         count += 1
#     print(count)
#     count += 1


# 8、求1-100的所有数的和（三种方法）

# count = 0
# sum1 = 0
# while True:
#     # sum1 = sum1 + count
#     sum1 += count
#     count += 1
#     if count == 101: break
# print(sum1)
# 9、输出 1-100 内的所有奇数（两种方法）

# 10、输出 1-100 内的所有偶数（两种方法）
# count = 1
#
# while count <= 100:
#     if count % 2 == 0:
#         print(count)
#     count += 1

# count = 0
# while count <= 100:
#     print(count)
#     count = count + 2

# 11、求1-2+3-4+5 ... 99的所有数的和
# count = 0
# sum1 = 0
# # while count < 100:
# #     if count % 2 == 0:
# #         sum1 = sum1 - count
# #     else:
# #         sum1 = sum1 + count
# #     count += 1
# # print(sum1)
# while count < 100:
#     sum1 = sum1 + count*(-1)**(count+1)
#     count += 1
# print(sum1)

# 12、⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）
# input while

# i = 0
# while i < 3:
#     username = input('请输入用户名：')
#     password = input('请输入密码：')
#     if username == 'alex' and password == '123':
#         print('登陆成功')
#         break
#     else:
#         print('登陆失败,您还有%d机会' % (2-i))
#     i += 1
# 思考题：如果机会用完了，可以再给用户选择继续的机会，
# 如果机会，给他三次机会，如果不继续退出循环，并且说一句：要不脸呀你。

import sys
print(sys.maxunicode)