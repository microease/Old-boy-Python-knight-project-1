# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 17:17
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 05 类名称空间，对象名称空间.py
# @Software: PyCharm

# 公用模板，公共框架
# class GameRole:
#
#     rule = '游戏规则'
#     hp = 1800
#     def __init__(self,area,nickname,hp,ad):
#         self.area = area
#         self.nickname = nickname
#         self.hp = hp
#         self.ad = ad
#
#     def attack(self):
#         print('谁施展了一个攻击')
#
#     def pen(self):
#         self.pen=10000
# gailun = GameRole('德玛西呀','草丛伦',1000,75)
# print(GameRole.attack)
# print(gailun.attack)
# gailun.attack = '攻击力'
# gailun.attack()
# yasuo = GameRole('艾欧尼亚','托儿所',500,150)
# penzi = GameRole('中国','键盘侠',10,100)
# penzi.pen = 10000
# penzi.pen()
# print(penzi.__dict__)
# 1对象为什么能调用类中的属性与方法而且只是调用，不能改变？
# gailun.属性名  先从自己空间去找，没有此属性他会通过类对象指针从类去找，  类中找不到，会从父类去找。
# print(gailun.hp)
# gailun.attack = 666  # 给对象增加一个属性 attack = 666
# print(gailun.attack)
# gailun.rule = gailun.rule  # '游戏规则'
# # gailun.rule = 游戏规则'
# # 对象.属性名='游戏规则'
# print(gailun.rule)
# gailun.nikename = '盖伦'
# print(gailun.nickname)
# 对象只能查看类中的属性，不能增删改类中的属性。

# 2，类能不能调用对象的属性？ 不能


# print(GameRole.area)
# 3，对象与对象之间可不可互相调用？
# 同一个类实例化出来的对象之间是不能互相访问的。
# 不同类实例化的对象有可能互相访问。

# 给对象封装属性：__init__ 任意位置。

