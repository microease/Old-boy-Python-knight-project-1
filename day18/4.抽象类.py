# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 10:44
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 4.抽象类.py
# @Software: PyCharm

# 工作中 公司有使用抽象类开发的规则
# 源码 别人使用抽象类

# 支付功能
from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):   # 模板的功能
    @abstractmethod     # abstractmethod是一个装饰器，装饰器怎么用？放在函数/类的上一行
    def pay(self):pass

    @abstractmethod
    def shouqian(self):pass

class Alipay(Payment):
    def pay(self,money):
        print('使用支付宝支付了%s元'%money)

class Wechatpay(Payment):
    def pay(self,money):
        print('使用微信支付了%s元'%money)

class ApplePay(Payment):
    def pay(self,money):
        print('使用applepay支付了%s元' % money)

def pay(obj,money):
    obj.pay(money)

p = Payment()
# a = Alipay()
# # a.pay(100)
# pay(a,100)
#
# we = Wechatpay()
# # we.pay(200)
# pay(we,200)
#
# ap = ApplePay()


# 规范
# 多人开发、复杂的需求、后期的扩展
# 手段 来帮助我们完成规范

# 抽象类
    # 抽象类是一个规范，它基本不会实现什么具体的功能，抽象类是不能被实例化
    # 要想写一个抽象类
        # from abc import ABCMeta,abstractmethod
        # 在这个类创建的时候指定 metaclass = ABCMeta
        # 在你希望子类实现的方法上加上一个 @abstractmethod装饰器
    # 使用抽象类
        # 继承这个类
        # 必须实现这个类中被@abstractmethod装饰器装饰的方法


