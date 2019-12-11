# -*- coding: utf-8 -*-
# @Time    : 2018/8/27 14:39
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 3.作业需求分析.py
# @Software: PyCharm

# 实现员工信息表
# 文件存储格式如下：
# id，name，age，phone，job
# 1,Alex,22,13651054608,IT
# 2,Egon,23,13304320533,Tearcher
# 3,nezha,25,1333235322,IT

# 我们需要把数据存储在文件中 为了这个数据可以永久的保存
# 就规范了一些简单的指令，能够直接要求代码来完成我们的指令，从而更方便的为用户提供数据的增删改查操作
# 什么叫数据库？？？
# 为什么要用这么复杂的语法来操作数据库呢？
# 广义的数据库的定义 ： 用简单的命令 就可以处理 文件中的数据

# 现在需要对这个员工信息文件进行增删改查。
# 增 add boss_jin,40,13838384438,driver
# 删 del 2    # 模仿数据库操作
# 改 set age=18 where name='nezha'
# # 查 select name, age where age>22
# nezha,25
# boss_jin,40

# 程序开始
# input('>>>')  输入一个语句

# 不允许一次性将文件中的行都读入内存。
# 基础必做：
# a.可以进行查询，支持三种语法：
# select 列名1，列名2，… where 列名条件
# 支持：大于小于等于，还要支持模糊查找。
# 示例：
# select name, age where age>22
# select * where job=IT
# select * where phone like 133

# 进阶选做：
# b.可创建新员工记录，id要顺序增加
# c.可删除指定员工记录，直接输入员工id即可
# d.修改员工信息
# 语法：set 列名=“新的值” where 条件
# #先用where查找对应人的信息，再使用set来修改列名对应的值为“新的值”
#
# 注意：要想操作员工信息表，必须先登录，登陆认证需要用装饰器完成
# 其他需求尽量用函数实现