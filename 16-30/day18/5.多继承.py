# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 11:09
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 5.多继承.py
# @Software: PyCharm

# class Parent1:pass
# class Parent2:pass
# class Son(Parent1,Parent2):pass
# print(Son.__bases__)

# 不是所有的语言都支持多继承 java
# c++ 支持多继承

# 天鹅  飞 游泳 走路
# 老虎  走路 游泳
# 鹦鹉  飞 说话 走路
# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def talk(self):
#         print('%s说话了'%self.name)
#
#     def swim(self):
#         print('%s在游泳'%self.name)
#
#     def fly(self):
#         print('%s在飞'%self.name)
#
#     def walk(self):
#         print('%s在走路'%self.name)
class Animal:
    def __init__(self,name):
        self.name = name

class FlyAnimal(Animal):
    def fly(self):
        print('%s在飞' % self.name)
class WalkAnimal(Animal):
    def walk(self):
        print('%s在走路'%self.name)
class SwimAnimal(Animal):
    def swim(self):
        print('%s在游泳'%self.name)

class Tiger(SwimAnimal,WalkAnimal):
    pass

class Swan(SwimAnimal,WalkAnimal,FlyAnimal):
    pass

class Parrot(FlyAnimal,WalkAnimal):
    def talk(self):
        print('%s说话了'%self.name)

swan = Swan('天鹅')
swan.fly()
swan.walk()


