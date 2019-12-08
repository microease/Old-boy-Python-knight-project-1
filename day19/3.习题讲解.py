# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 9:04
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 3.习题讲解.py
# @Software: PyCharm

# 1.简述编写类和执行类中方法的流程
# 给类起一个名字 class 类名 类名需要大写
# 定义静态属性，定义方法

# 实例化一个对象
# 对象名.方法名()
    # 对象在自己的内存空间中找不到方法的名字，所以就（依靠类的指针）到类中去寻找
# class Student:
#     def __init__(self):
#         self.name = 'alex'
#
#     def name(self):
#         print(12212)
#
# alex = Student()
# print(alex.name)  #'alex'()
# Student.name(alex)

# 简述面向对象的三大特性
# 继承 ：提高代码的重用性，规范性
# 多态
# 封装

# class A:
#     def func(self,a):
#         print(a)

# 方法和函数的区别
# 只有被对象调用的类中的方法才能被成为一个方法
# class A:
#     def func(self):pass
# a = A()
# print(a.func)
# print(A.func)
# from types import MethodType,FunctionType
# print(isinstance(a.func,MethodType))
# print(isinstance(a.func,FunctionType))
# print(isinstance(A.func,FunctionType))
# print(isinstance(A.func,MethodType))

# 初始化函数？？ __init__
# 构造函数 __new__

# self指的是对象本身

# 7.每个对象的属性存储在自己的内存空间中
# 8.对象的方法 存储在类的命名空间中

# 9.
# class Foo:
#     def func(self):
#         print('foo.func')
#
# obj = Foo()
# f = obj.func
# print(obj.func())
# print(f)
# f()

# 15
# class Person:
#     def __init__(self,name,pwd,email):
#         self.name = name
#         self.pwd = pwd
#         self.email = email
#
# user_list = []
# i = 0
# while True:
#     if i>=3:break
#     i += 1
#     user = input("请输入用户名:")
#     pwd = input("请输入密码:")
#     email = input("请输入邮箱:")
#     obj = Person(user,pwd,email)
#     user_list.append(obj)
#
# for  i in user_list:
#     print('我是%s,我的邮箱是%s'%(i.name,i.email))


# 16
class User:
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd

class Account:
    def __init__(self):
        self.user_list = []

    def login(self):
        username = input('username : ')
        password = input('password : ')
        for  usr in self.user_list:
            if usr.name == username and usr.pwd == password:
                print('登录成功')
                return True


    def register(self):
        username = input('username : ')
        password = input('password : ')
        usr = User(username,password)
        self.user_list.append(usr)

    def run(self):
        for i in range(2):
            self.register()
        for i in range(3):
            if self.login():
                break
        else:
            print('登录失败')

obj = Account()
obj.run()















