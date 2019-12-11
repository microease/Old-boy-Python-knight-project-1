# 1.计算时间差的功能
# 如果是年开头 只显示年月
# 2018-9-3 22:48:20
# 2018-9-4 10:15:20
# str1 = '2018-9-4 10:15:20'
# str2 = '2018-9-3 22:48:20'
import time
# struct_time1 = time.strptime(str1,'%Y-%m-%d %H:%M:%S')
# stamp1 = time.mktime(struct_time1)
# struct_time2 = time.strptime(str2,'%Y-%m-%d %H:%M:%S')
# stamp2 = time.mktime(struct_time2)
# t = stamp1-stamp2
# ret = time.gmtime(t)
# print('%s %s %s %s %s %s'%(ret.tm_year-1970,ret.tm_mon-1,ret.tm_mday-1,ret.tm_hour,ret.tm_min,ret.tm_sec))

# def time_diff(time_start,time_end,fmt='%Y-%m-%d %H:%M:%S'):
#     stamp_func = lambda t: time.mktime(time.strptime(t,fmt))
#     stamp1 = stamp_func(time_end)
#     stamp2 = stamp_func(time_start)
#     t = abs(stamp1-stamp2)
#     ret = time.gmtime(t)
#     return (ret.tm_year-1970,ret.tm_mon-1,ret.tm_mday-1,ret.tm_hour,ret.tm_min,ret.tm_sec)
# ret = time_diff(str2,str1)
# print(ret)

# 2.写一个发红包，接受两个参数：金额 个数
# 发n个红包 每个人取到m块钱的几率是一样的
# money = 200
# num = 10
# 0-200之间取num-1个点
import random
# ret = random.sample(range(1,money*100),num-1)
# ret.sort()
# ret.insert(0,0)
# ret.append(20000)
# lst = []
# for i in range(len(ret)-1):
#     money = ret[i+1] - ret[i]
#     lst.append(money/100)
# print(lst)

# def lucky_money(money,num):
#     ret = random.sample(range(1,money*100),num-1)
#     ret.sort()
#     ret.insert(0,0)
#     ret.append(20000)
#     for i in range(len(ret)-1):
#         money = ret[i+1] - ret[i]
#         yield money/100
#
# for money in lucky_money(200,15):
#     print(money)

# import  random
# def bouns(money,amount):   # 100,10
#     while amount:  # while 10
#         if amount==1:
#             yield float('%.2f' % money)
#         else:
#             money1 = random.uniform(0,money)    # 0,100   90
#             money2 = random.uniform(1/amount,3/amount)*money1   # 1/10,3/10  # 2/10 0.2 * 90 = 18
#             money -= float('%.2f' % money2)
#             yield float('%.2f' % money2)
#         amount -=1
# g = bouns(200,10)
# print(list(g))

# 3.统计文件夹文件的总大小
# 如果这个文件夹中还有文件夹，应该继续到这个文件夹中去计算
# 计算阶乘
# 5！ 5*4*3*2*1
# def fn(n):
#     if n == 1:
#         return n
#     return n * fn(n-1)
# print(fn(5))

# def fn(5):
#     if 5 == 1:
#         return n
#     return 5 * fn(4)
#
# def fn(4):
#     if 4 == 1:
#         return n
#     return 4 * fn(3)
#
# def fn(3):
#     if n == 1:
#         return n
#     return 3 * fn(2)
#
# def fn(2):
#     if n == 1:
#         return n
#     return 2 * fn(1)
#
# def fn(1):
#     if n == 1:
#         return n
#     return n * fn(n-1)
# 递归
import os
def get_size(path):
    sum_size = 0
    if os.path.isdir(path):
        name_lst = os.listdir(path)
        for name in name_lst:
            name_path = os.path.join(path,name)
            if os.path.isfile(name_path):
                sum_size += os.path.getsize(name_path)
            elif os.path.isdir(name_path):
                sum_size += get_size(name_path)
        return sum_size
    elif os.path.isfile(path):
        return os.path.getsize(path)

# ret = get_size('D:\骑士计划PYTHON1期')
# print(ret)
# get_size('D:\骑士计划PYTHON1期\day24')

# def get_size(path):  # 'D:\骑士计划PYTHON1期\day24'
#     sum_size = 0
#     name_lst = os.listdir(path)  #name_lst = [wahaha,1.内容回顾,2.作业讲解,3.init.py]
#     for name in name_lst:  # wahaha
#         name_path = os.path.join(path,name)  # name_path = 'D:\骑士计划PYTHON1期\day24\wahaha'
#         if os.path.isfile(name_path):
#             sum_size += os.path.getsize(name_path)
#         elif os.path.isdir(name_path):      #  True
#             sum_size += 70 # get_size('D:\骑士计划PYTHON1期\day24\wahaha')
#     return sum_size
#
# def get_size(path):  # path = 'D:\骑士计划PYTHON1期\day24\wahaha'
#     sum_size = 0
#     name_lst = os.listdir(path)   # name_lst = QQXING,init.py,file
#     for name in name_lst:         # qqxing init.py file
#         name_path = os.path.join(path,name)  # D:\骑士计划PYTHON1期\day24\wahaha\qqxing
#         if os.path.isfile(name_path):
#             sum_size += os.path.getsize(name_path)  # sum_size = 70
#         elif os.path.isdir(name_path):       # True
#             sum_size += 20  # getsize(D:\骑士计划PYTHON1期\day24\wahaha\qqxing)
#     return sum_size  # 70
#
# def get_size(path):  # path = 'D:\骑士计划PYTHON1期\day24\wahaha\qqxing'
#     sum_size = 0
#     name_lst = os.listdir(path)   # name_lst = 1Q,init
#     for name in name_lst:         # 1Q,init
#         name_path = os.path.join(path,name)  # D:\骑士计划PYTHON1期\day24\wahaha\qqxing\1q
#         if os.path.isfile(name_path):        #True  True
#             sum_size += os.path.getsize(name_path)  #sum_size += 20 sumsize=20+0 = 20
#         elif os.path.isdir(name_path):
#             sum_size += get_size(name_path)
#     return sum_size  # 20

# ---------------循环---------------
# lst = ['D:\骑士计划PYTHON1期']   # 数据结构 ： 栈  后进去的先出来
# sum_size = 0
# while lst:
#     path = lst.pop()
#     name_lst = os.listdir(path)
#     for name in name_lst:
#         name_path = os.path.join(path,name)
#         if os.path.isfile(name_path):
#             sum_size = sum_size + os.path.getsize(name_path)
#         elif os.path.isdir(name_path):
#             lst.append(name_path)
# print(sum_size)

# 三级菜单 练习和扩展


# 4.当前文件的所在目录的父目录
# import os
# base_path = os.path.dirname(os.path.dirname(__file__))
# print(base_path)

# 5.用python创建一个目录结构
# -- glance
#   -- app
#       -- policy.py
#       -- config.py
#   -- db
#       -- model.py
# os.makedirs(r'glance\app')
# os.makedirs(r'glance\db')
# open(r'glance\app\policy.py','w').close()
# open(r'glance\app\config.py','w').close()
# open(r'glance\db\model.py','w').close()

# 6.用执行py文件的形式来完成登录校验  sys.argv
# user_dict = {'alex':'alex3714','boss_jin':'666'}
# # python xxx.py alex alex3714
# import sys
# if sys.argv[1] in user_dict and user_dict[sys.argv[1]] == sys.argv[2]:  # [xxx.py,alex,alex3714]
#     print('登录成功')
# else:
#     exit()
# print('执行文件中的功能')