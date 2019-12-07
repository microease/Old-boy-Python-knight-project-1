# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 10:26
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 03 列表.py
# @Software: PyCharm
# 列表：python基础数据类型之一：其他语言中也有列表的概念，js 数组，可索引，可切片，可加步长
# li = ['alex', 100, True, [1, 2, 3], {'name':'太白'},(22, 33)]
# s1 = '[1,2,3]'
# 列表可以存储大量的数据32位python的限制是 536870912 个元素,64位python的限制是 1152921504606846975 个元素。
# li = ['alex', 100, True, [1, 2, 3], {'name':'太白'},(22, 33)]
# 第一：索引，切片，切片+步长。
# print(li[0],type(li[0]))
# print(li[1],type(li[1]))
# print(li[2],type(li[2]))
# print(li[:4])
# print(li[::2])
# print(li[-1:-4:-2])
# print(li[-1:2:-2])

l1 = ['alex', 'wusir', 'taibai', 'egon', '景女神', '文周老师', '日天']
#第二：增删改查，其他方法。
# 增
# append  追加
# l1.append('小温老师')
# print(l1.append([1, 2, 3]))
# print(l1)
# name_list = ['赵三', '里斯']
# while 1:
#     username = input('请输入新员工姓名：').strip()
#     if username.upper() == 'Q' : break
#     name_list.append(username)
#
# print(name_list)
# insert 插入
# l1.insert(1,'宝元')
# print(l1)

# extend  迭代着追加
# l1.extend('abc')
# # l1.extend([111,222,333])
# l1.extend(['alex','sb'])
# print(l1)


#  删除
# pop 按照索引去删除
# ret = l1.pop(0)
# print(ret) # 返回值
# print(l1)

# remove 按照元素删除
# l1.remove('alex')
# print(l1)

# clear 清空
# l1.clear()
# print(l1)

# del
# 可以按照索引删除
# del l1[0]
# print(l1)
# 可以按照切片删除（可以加步长）
# del l1[:2]
# del l1[3:]
# del l1[1::2]
# print(l1)
# 可以在内存级别删除整个列表
# del l1
# print(l1)

# 改
# 按照索引改
# l1[2] = '男神'
# l1[-1] = '泰迪'
# 按照切片（加步长）
    # 按照切片
# l1[:2] = 'sbsbsb'
# l1[:4] = [11,22,33,44,55,66,77]
    #按照切片 + 步长  一一对应
# l1[:3:2] = 'af'
# print(l1)

# 查
# 索引，切片，切片+步长
# for 循环
# for i in l1:
#     print(i)

# 其他方法
# print(len(l1))  # 查询总个数
# print(l1.count('alex')) # 某个元素出现的次数
# index 通过元素找索引
# print(l1.index('taibai'))
# l2 = [5, 6, 7, 1, 4, 3, 2, 9]
# sort
# l2.sort()  # 从小到大
# print(l2)

# l2.sort(reverse=True)  # 从大到小
# print(l2)

# l2.reverse()  # 反转
# print(l2)


#第三：列表的嵌套。

l3 = ['alex', 'wusir', ['taibai', 99, 'ritian'], 20]
# 1， 找到alex的e元素。
# s1 = l3[0]
# print(s1)
# print(s1[2])
# s2 = l3[0][2]
# print(s2)
# 2， 将wusir变成大写。
# w1 = l3[1]
# w2 = w1.upper()
# l3[1] = w2
# print(l3)

# l3[1] = 'WUSIR'
# l3[1] = l3[1].upper()
# print(l3)

# 3， 给此列表['taibai',99,'ritian'] 追加一个元素,'文周'
# print(l3[2])
# l3[2].append('文周')
# print(l3)
# 4，将 'taibai' 首字母大写。
# print(l3[2][0])
# s1 = l3[2][0].capitalize()
# # print(s1)
# l3[2][0] = s1

# l3[2][0] = l3[2][0].capitalize()
# l3[2].append(666)
# l3[2][0].capitalize()
# print(l3)

# 5，将 99 通过数字加1 的方式变成100，并放回原处。
# l3[2][1] = l3[2][1] + 1
# l3[2][1] += 1
# print(l3)