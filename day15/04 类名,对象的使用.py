# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 15:09
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 04 类名,对象的使用.py
# @Software: PyCharm


# 一个公共框架，一个公共模型
# class Person:
#
#     animal = '高级动物'
#     walk_way = '直立行走'
#     language = '语言'
#
#     def eat(self):
#         print('该吃吃，该喝喝，啥事别忘心里搁')
#
#     def work(self):
#         print('人类都需要工作。。。')

# 类名
    # 1，查看类中的所有属性及方法 __dict__
# print(Person.__dict__)
# print(Person.__dict__['animal']) # 通过__dict__方式 单独的属性及方法可以查，但是不能增删改
# Person.__dict__['animal'] = '低级动物'
# Person.__dict__['name'] = 'alex'
# print(Person.__dict__)
# 工作中，学习中 一般用到 __dict__查看类中的所有属性及方法,不进行其他操作。
    #2，查看,（增删改）类中某个，某些属性 用     万能的点 .
# print(Person.animal)  # 查
# print(Person.language)
# Person.name = 'alex'  # 增
# print(Person.name)
# Person.animal = '低级动物' # 改
# del Person.walk_way  # 删
# print(Person.__dict__)
    #3，操作方法 一般不通过类名操作！！！
# Person.__dict__['work'](111) 不建议通过__dict__执行方法
# Person.work(666)

# 对象

class Person:

    animal = '高级动物'
    walk_way = '直立行走'
    language = '语言'

    def __init__(self,name,age,eye):  # 功能：给对象封装属性的。
        self.name1 = name
        self.age1 = age
        self.eye1 = eye

    def eat(self):
        # print(self)
        print('该吃吃，该喝喝，啥事别忘心里搁')

    def work(self):
        print('人类都需要工作。。。')

# obj = Person('alex',1000,'小眼睛')  # 这个过程是一个实例化过程，他会实例化一个对象（他会在内存实例化一个对象空间）。
# print(obj)
# print(obj.name1)
# 实例化过程内部进行了三个阶段：
# 1,在内存中开辟了一个对象空间
# 2，自动执行类中的__init__方法，并且将对象空间自动传给self参数，其他参数手动传入。
# 3， 执行__init__方法 给对象空间封装相应的属性。
obj = Person('alex',1000,'小眼睛')
# 对象：
    # 对象操作对象空间
        # 对象查看对象空间所有的属性  __dict__
# print(obj.__dict__)
        # 对象操作对象的某个属性 增删改查  万能的点.
# obj.sex = '男'  # 增
# del obj.eye1  # 删
# obj.eye1 = '大一点'  # 改
# print(obj.name1)
# print(obj.__dict__)
    # 对象操作类空间的属性 只能查
# print(obj.animal)
# obj.animal = '低级动物'
# print(obj.animal)
# print(obj.__dict__)
# print(Person.__dict__)
    # 对象操作类空间的方法
# print(obj)
obj.eat()
