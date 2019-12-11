# 1.读代码说结果
# v = dict.fromkeys(['k1','k2'],[])
# lst = []
# v = {'k1':lst,'k2':lst}
# v['k1'].append(666)
# v = {'k1':[666],'k2':[666]}
# print(v)
# v['k1'] = 777
# v = {'k1':777,'k2':[666]}
# print(v)

# 2.什么是正则的贪婪匹配？
# 尽可能多匹配，它底层实现的算法是回溯算法

# 3.面向对象的经典类和新式类的区别
# 经典类 ：
    # 3.*中没有，在2.7 不主动继承object
    # 继承查找顺序 深度优先，没有mro方法，没有super方法
    # class Payment:
        # __metaclass__ = ABCMeta
# 新式类 ：
    # 3.*中所有的类都是新式类，在2.7中主动继承object
    # 继承查找顺序 广度优先，遵循mro方法，有super方法遵循mro顺序
    # class Payment(metaclass = ABCMeta)

# 元类 ： 创建类的类就是元类
# 默认情况下所有的类的元类都是type，除非你指定metaclass

# 4.简述 yield和yield from关键字的区别
# def func():
#     yield from 'egon'
#     yield from 'alex'
#     # for i in 'egon':yield i
#     # for j in 'alex':yield j
#
# g = func()
# print(list(g))

# 5.IO多路复用的作用？
# IO多路复用是操作系统提供的
# 有个代理，帮助你监听 网络IO对象，监听对象的读事件、写事件、特殊条件事件
# 提供给网络应用一个能够大幅度的降低cpu压力，增加了单线程网络通信程序的兵法效果




