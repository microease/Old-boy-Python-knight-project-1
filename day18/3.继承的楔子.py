# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 9:22
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 3.继承的楔子.py
# @Software: PyCharm

# 游戏
# 梅西 奥巴马 史努比 史派克 小猪配齐 猪八戒   # 实例
# 人  狗  猪  # 分类
# 动物  # 汇总

# 先抽象 后继承



# 猫类 ：
    # 属性 ： 名字，品种，食物
    # 方法 ： 叫，抓老鼠，吃，喝
# 狗类 ：
    # 属性 ： 名字，品种，食物
    # 方法 ： 叫，看家，吃，喝
# class Animal:
#     def __init__(self,name,kind,food,language):
#         self.name = name
#         self.kind = kind
#         self.food = food
#         self.language = language
#     def yell(self):
#         print('%s叫'%self.language)
#     def eat(self):
#         print('吃%s'%(self.food))
#     def drink(self):
#         print('喝水')
#
# class Cat(Animal):
#     def catch_mouse(self):
#         print('抓老鼠')
#
# class Dog(Animal):
#     def look_after_house(self):
#         print('看家')

# 继承
# 父类/超类/基类 ：Animal
# 子类/派生类    ：Cat、Dog

# 继承与重用 -  父类中所有的属性和方法都可以被子类使用了
# 阿猫 = Cat('阿猫','橘猫','牛杂','喵喵')
# print(阿猫.name)
# 阿猫.drink()
# 阿猫.eat()
# 阿猫.yell()
#
# 阿狗 = Dog('阿狗','土狗','阿猫','汪汪')
# print(阿狗.name)
# 阿狗.drink()
# 阿狗.eat()
# 阿狗.yell()

# 派生
# class Animal:
#     def __init__(self,name,kind,food,language):
#         print('in animal')
#         self.name = name
#         self.kind = kind
#         self.food = food
#         self.language = language
#     def yell(self):
#         print('%s叫'%self.language)
#     def eat(self):
#         print('吃%s'%(self.food))
#     def drink(self):
#         print('喝水')
#
# class Cat(Animal):   # Animal的派生类
#     def __init__(self,name,kind,food,language,eye_color):
#         print('in Cat')
#         self.eye_color = eye_color    # 派生属性
#         Animal.__init__(self,name,kind,food,language)
#         # super().__init__(name,kind,food,language)
#
#     def catch_mouse(self):   # 派生方法
#         print('抓老鼠')
#
#     def eat(self):           # 不仅执行了父类中的基础功能，还完成了特殊的功能
#         Animal.eat(self)
#         # super().eat()
#         self.weight = 10
#
# class Dog(Animal):
#     def look_after_house(self):
#         print('看家')
#
#     def eat(self):
#         # Animal.eat(self)
#         super().eat()
#         self.drink()
#
# 阿猫 = Cat('阿猫','橘猫','牛杂','喵喵','绿色')
# print(阿猫.eye_color)
# print(阿猫.food)
# 阿猫.catch_mouse()
# 阿猫.eat()
# print(阿猫.weight)
# 当子类当中有要被调用的方法的时候，子类的对象会直接选择子类中的方法、变量,父类中的方法不会被自动执行
# 如果我们既想要执行子类的方法，也想要执行父类的方法，那么需要在子类的方法中调用父类的方法：
# 父类名.方法名(self,...)
# super().方法名(...)
# 帮助我们在子类中调用父类中的同名方法

# 面试题
# class Foo:
#     def __init__(self):
#         self.func()
#     def func(self):
#         print('in Foo')
#
# class Son(Foo):
#     def func(self):
#         print('in Son')
#
# s1 = Son()

# class Foo:
#     Country = 'China'
#     def func(self):
#         print(self.Country)
#
# class Son(Foo):
#     Country = 'English'
#     def func(self):     # 走这个方法
#         print(self.Country)
#
# s = Son()
# s.func()

# class Foo:
#     Country = 'China'
#     def func(self):  # 走这个方法
#         print(self.Country)
#
# class Son(Foo):
#     Country = 'English'
#
# s = Son()
# s.func()   # English

# class Foo:
#     Country = 'China'
#     def func(self):
#         print(self.Country)
#
# class Son(Foo):pass
#
# s = Son()
# s.func()   # 'China'




