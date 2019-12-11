# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 10:39
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 03 组合.py
# @Software: PyCharm

# 3,模拟英雄联盟写一个游戏人物的类（升级题）.
#   要求:
#   (1)创建一个 Game_role的类.
#   (2) 构造方法中给对象封装name,ad(攻击力),hp(血量).三个属性.
#   (3) 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
#       例: 实例化一个对象 盖伦,ad为10, hp为100
#       实例化另个一个对象 剑豪 ad为20, hp为80
#       盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血,  还剩多少血'的提示功能.

# 组合： 给一个类的对象封装一个属性，这个属性是另一个类的对象。


class Gamerole:
    def __init__(self,nickname,ad,hp):
        self.nickname = nickname
        self.ad = ad
        self.hp = hp

    def attack(self,role):
        role.hp = role.hp - self.ad
        print('%s攻击%s,%s掉了%s血,还剩%s血' %\
              (self.nickname,role.nickname,role.nickname,self.ad,role.hp))

    def equip_weaon(self,w):  # 给人物封装了一个武器属性，这个属性值是Weapon类的一个对象
        self.weapon = w   # 组合


class Weapon:
    def __init__(self,name,ad):
        self.name = name
        self.ad = ad
    def fight(self,role1,role2):
        role2.hp = role2.hp - self.ad
        print('%s 用 %s 攻击了%s, %s掉了%s血,还剩%s血'\
              %(role1.nickname,self.name,role2.nickname,role2.nickname,self.ad,role2.hp))

p1 = Gamerole('盖伦',20,500)
p2 = Gamerole('剑豪',100,200)
# p1.attack(p2)
# print(p2.hp)
# w1.fight(p1,p2) # 这样不好，动作的发起者应该是人而不是武器
# w1 = Weapon('大宝剑',30)
# w2 = Weapon('武士刀',80)
# print(w1)
# p1.equip_weaon(w1)
# print(p1.weapon)  #其实 他就是w1
# p1.weapon.fight(p1,p2)
# 让剑豪利用武士刀给盖伦一刀
# p2.equip_weaon(w2)
# p2.weapon.fight(p2,p1)

# 组合的意义：让类的对象与另一个类的对象产生关系，类与类之间产生关系。

