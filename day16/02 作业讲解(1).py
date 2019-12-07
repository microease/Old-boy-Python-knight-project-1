# # -*- coding: utf-8 -*-
# # @Time    : 2018/8/24 9:46
# # @Author  : 骑士计划
# # @Email   : customer@luffycity.com
# # @File    : 02 作业讲解.py
# # @Software: PyCharm
#
#
# 							Day15天作业及默写
# 1,完成下列功能:
#   1.1创建一个人类Person,再类中创建3个静态变量(静态字段)
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言'
#   1.2在类中定义三个方法,吃饭,睡觉,工作.
#   1.3在此类中的__init__方法中,给对象封装5个属性:国家,姓名,性别,年龄,  身高.
#   1.4实例化四个人类对象:
#     第一个人类对象p1属性为:中国,alex,未知,42,175.
#     第二个人类对象p2属性为:美国,武大,男,35,160.
#     第三个人类对象p3属性为:你自己定义.
#     第四个人类对象p4属性为:p1的国籍,p2的名字,p3的性别,p2的年龄,p3  的身高.
#   1.5 通过p1对象执行吃饭方法,方法里面打印:alex在吃饭.
#   1.6 通过p2对象执行吃饭方法,方法里面打印:武大在吃饭.
#   1.7 通过p3对象执行吃饭方法,方法里面打印:(p3对象自己的名字)在吃饭.
#   1.8 通过p1对象找到Person的静态变量 animal
#   1.9 通过p2对象找到Person的静态变量 soul
#   2.0 通过p3对象找到Person的静态变量 language

# class Person:
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言'
#     def __init__(self,country,name,sex,age,height):
#         self.country = country
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.height = height
#     def eat(self):
#         print('%s吃饭' %self.name)
#     def sleep(self):
#         print('睡觉')
#     def work(self):
#         print('工作')
# p1 = Person('中国','alex','未知',42,175)
# p2 = Person('美国','武大','男',35,140)
# p3 = Person('日本','西门','男',20,180)
# p4 = Person(p1.country,p2.name,'男',20,180)
# p1.eat()
# p2.eat()
# p3.eat()
# 2,通过自己创建类,实例化对象
#   在终端输出如下信息
#   小明，10岁，男，上山去砍柴
#   小明，10岁，男，开车去东北
#   小明，10岁，男，最爱大保健
#   老李，90岁，男，上山去砍柴
#   老李，90岁，男，开车去东北
#   老李，90岁，男，最爱大保健
#   老张…


# class Daylife:
#     def __init__(self,name,sex,age):
#
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def chop_wood(self):
#         print('%s,%s,%s,上山去砍柴' %(self.name,self.age,self.sex))
#     def drive(self):
#         print('%s,%s,%s,开车去东北' %(self.name,self.age,self.sex))
#     def health_care(self):
#         print('%s,%s,%s,最爱大保健' % (self.name, self.age, self.sex))
#
# p1 = Daylife('小明','男',10)
# p1.chop_wood()
# p1.drive()
# p1.health_care()



# 3,模拟英雄联盟写一个游戏人物的类（升级题）.
#   要求:
#   (1)创建一个 Game_role的类.
#   (2) 构造方法中给对象封装name,ad(攻击力),hp(血量).三个属性.
#   (3) 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
#       例: 实例化一个对象 盖伦,ad为10, hp为100
#       实例化另个一个对象 剑豪 ad为20, hp为80
#       盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血,  还剩多少血'的提示功能.
#
#
# 4,默写内容:
#   创建一个人类,定义三个静态变量,在构造方法中封装3个属性.然后实例化一个对象,对象调用自己的属性,对象调用类的静态方法,对象调用类中的方法.
#   默写一下实例化一个对象，具体经历了哪些阶段。
#
