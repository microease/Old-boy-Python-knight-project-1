# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 8:33
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 1.内容回顾.py
# @Software: PyCharm

# 类 具有相同属性和方法的一类事物
# 实例化 类名()
    # 开辟了一块内存空间
    # 执行init
    # 封装属性
    # 自动的把self返回给实例化对象的地方
# 对象/实例
    # 一个实实在在存在的实体
# 组合
    # 一个类的对象 作为另一个类对象的属性
    # 让两个类之间产生关系

# 类和对象的命名空间

# class Course:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

# class Student:
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.course = course
#
# python = Course('python',19800)
# xiaoming1 = Student('小明',22,python)
# xiaoming2 = Student('小明',22,python)
# xiaoming3 = Student('小明',22,python)
# python.price = 29800
# print(xiaoming.course.name)

# class Student:
#     def __init__(self,name,age,course_name,course_price):
#         self.name = name
#         self.age = age
#         self.course_name = course_name
#         self.course_price = course_price
#
# xiaoming1 = Student('小明',22,'python',19800)
# xiaoming1 = Student('小明',22,'python',19800)
# xiaoming1 = Student('小明',22,'python',19800)
# xiaoming1 = Student('小明',22,'python',19800)

# __dict__ :
# 类中 ： 所有的静态属性 和 方法
# 对象 ： 所有的对象的属性 、 类对象指针
# class Foo:
#     count = 0
#     def __init__(self):
#         self.count += 1
# f1 = Foo()
# f2 = Foo()
# print(Foo.count)  # 0
# print(f1.count)   # 1
# print(f2.count)
# 静态属性 ： 类的属性，所有的对象共享这个变量
# 对象名 去修改 类的静态属性
    # 在对象的空间中又创建了一个属性，而不能修改类中属性的值
# 操作静态属性 应该 用类名来操作

# 请你写一个类，能够统计一共实例化了多少个对象？
# class Foo:
#     count = 0
#     def __init__(self):
#         Foo.count += 1
#
# f1 = Foo()
# print(f1.count)
# f2 = Foo()
# f3 = Foo()
# f4 = Foo()
# f5 = Foo()
# print(f1.count)
# print(f5.count)
# print(Foo.count)
#  当类中的属性发生改变的时候，对象中没有同名的属性、方法的时候，对象使用属性名会跟着类中的变量走

# class Foo:
#     count = [0]
#
# f1 = Foo()
# f1.count[0] += 1
# print(f1.count[0])
# print(Foo.count[0])
# f1.count = [2]
# print(f1.count)
# print(Foo.count)

# 只要对象的某个属性被直接赋值，那么一定是对象的命名空间发生变化

# 只要是静态变量，就用类名操作








