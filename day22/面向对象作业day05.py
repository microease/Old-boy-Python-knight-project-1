# 1. 看代码写结果
#     '''python
#     class Foo(object):
#
#         def __init__(self):
#             self.name = '武沛齐'
#             self.age = 100
#
#     obj = Foo()
#     setattr(Foo, 'email', 'wupeiqi@xx.com')
#
#     v1 = getattr(obj, 'email')
#     v2 = getattr(Foo, 'email')  # 'wupeiqi@xx.com'
#
#     print(v1,v2)  # ('wupeiqi@xx.com','wupeiqi@xx.com')
#     '''



# 2. 如果有以下handler.py文件，补全func：
#     - dir方法能够得到当前文件中的所有成员
#     - 获取handler中名字叫Base的成员
#     - 检查其他成员是否是Base类的子类(不包含Base)，如果是则创建对象并添加到objs列表中。

    # ```python
    # # handler.py
# class Base(object):
#     pass
#
# class F1(Base):
#     pass
#
# class F2(Base):
#     pass
#
# class F3(F2):
#     pass
#
# class F4(Base):
#     pass
#
# class F5(object):
#     pass
#
# class F6(F5):
#     pass
#
# import sys
# def func():
#     name_lst = dir(sys.modules[__name__])
#     obj_list = []
#     for name in name_lst:
#         name_addr = getattr(sys.modules[__name__],name)
#         if type(name_addr) is type and issubclass(name_addr,Base) and name_addr is not Base:
#             obj_list.append(name_addr())
#     return obj_list
# ret = func()
# print(ret)

    # ```

# 3.补充代码
#     ```python
#     class Foo(object):
#         def __init__(self):
#             self.name = '武沛齐'
#             self.age = 100
#     obj = Foo()
#     setattr(obj, 'email', 'wupeiqi@xx.com')
#     print(obj.__dict__)
#     请实现：一行代码实现获取obj中所有成员（字典类型）

# 4.写一个类，包含对象属性和方法
# 根据用户的输入找到对应的类成员，如果是方法名就调用，如果是属性就打印
class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):print('吃')
    def drink(self):print('喝')
    def sleep(self):print('睡')

alex = Foo('alex',20)
while True:
    name = input('>>>')
    if hasattr(alex,name):
        name_addr = getattr(alex, name)
        if callable(name_addr):
             name_addr()
        else:print(name_addr)

# 5.继续完成学生选课系统的作业（必须用到反射）

# 6.预习http://www.cnblogs.com/Eva-J/articles/7228075.html 常用模块一
