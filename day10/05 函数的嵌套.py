# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 11:44
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 05 函数的嵌套.py
# @Software: PyCharm

# def func1():
#     print(111)
# def func2():
#     print(222)
#     func1()
#     print(333)
# print(666)
# func2()
# print(555)


#
# def func1():
#     print(222)
#     def func2():
#         print(333)
#     print(111)
#     func2()
#     print(666)
# func1()
# 222 111 333 666

# global nonlocal
# 局部名称空间 对全局名称空间的变量可以引用，但是不能改变。
# count = 1
# def func1():
#     count = 2
#     print(count)
# func1()
# count = 1
# def func1():
#     # count = 3
#     count = count + 1  # local variable 'count' referenced before assignment
#     print(count)
# func1()
# 如果你在局部名称空间 对一个变量进行修改，那么解释器会认为你的这个变量在局部中已经定义了，
# 但是对于上面的例题，局部中没有定义，所以他会报错，
# global
    # 1，在局部名称空间声明一个全局变量。
# def func2():
#     global name
#     name = 'alex'
# func2()
# print(name)
    # 2，在局部名称空间可以对全局变量进行修改。
# count = 1
# def func1():
#     global count
#     count = count + 1
#     print(count)
# func1()
# print(count)

# nonlocal
# def func1():
#     count = 666
#     def func2():
#         print(count)
#     func2()
# func1()


# nonlocal
# 子函数对父函数的变量进行修改。
# 此变量不能是全局变量。

# 在局部作用域中，对父级作用域（或者更外层作用域非全局作用域）的变量进行引用和修改，
# 并且引用的哪层，从那层及以下此变量全部发生改变。
def func1():
    count = 666
    def inner():
        print(count)
        def func2():
            nonlocal count
            count += 1
            print('func2',count)
        func2()
        print('inner',count)
    inner()
    print('func1',count)
func1()
#  666  func2 667  inner 667  func1 667
#

