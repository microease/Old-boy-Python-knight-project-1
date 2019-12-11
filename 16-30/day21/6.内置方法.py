# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 12:03
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 6.内置方法.py
# @Software: PyCharm

# 在不是需要程序员定义，本身就存在在类中的方法就是内置方法
# 内置的方法通常都长这样 ： __名字__
# 名字 ： 双下方法、 魔术方法、 内置方法

# __init__
    # 不需要我们主动调用，而是在实例化的时候内部自动调用的
# 所有的双下方法，都不需要我们直接去调用,都有另外一种自动触发它的语法

# __str__ __repr__
# class Course:
#     def __init__(self,name,period,price,teacher):
#         self.name= name
#         self.period = period
#         self.price = price
#         self.teacher = teacher
#
#     def __str__(self):
#         return 'str : %s %s %s %s' % (self.name, self.period, self.price, self.teacher)
#
#     def __repr__(self):
#         return 'repr : %s %s %s %s' % (self.name, self.period, self.price, self.teacher)
# course_lst = []
# python = Course('python','6 month',29800,'boss jin')
# course_lst.append(python)
# linux = Course('linux','5 month',25800,'oldboy')
# course_lst.append(linux)
# for id,course in enumerate(course_lst,1):
#     # print('%s %s %s %s %s'%(id,course.name,course.period,course.price,course.teacher))
#     print(id,course)
#     print('%s %s'%(id,course))
#     print(str(course))
#     print(repr(course))
#     print('%r'%course)

# __str__
# 当你打印一个对象的时候 触发__str__
# 当你使用%s格式化的时候 触发__str__
# str强转数据类型的时候  触发__str__

# __repr__
# repr是str的备胎
# 有__str__的时候执行__str__,没有实现__str__的时候，执行__repr__
# repr(obj)内置函数对应的结果是 __repr__的返回值
# 当你使用%r格式化的时候 触发__repr__

# 学生选择课程的时候，要显示所有的课程

# class Foo:
#     # def __str__(self):
#     #     return 'Foo.str'
#     def __repr__(self):
#         return 'Foo.repr'
#
#
# class Son(Foo):
#     pass
#     # def __str__(self):
#     #     return 'Son.str'
#
#     # def __repr__(self):
#     #     return 'Son.repr'
#
# s1 = Son()
# print(s1)