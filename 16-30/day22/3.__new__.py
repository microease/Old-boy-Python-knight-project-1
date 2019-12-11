# __new__
# 在init之前，实例化对象的第一步是__new__创建了一个空间

# class Foo:
#     def __init__(self):                 # 初始化方法
# #         print('执行了init')
# #     def __new__(cls, *args, **kwargs):  # 构造方法
# #         # object.__new__(cls)
# #         print('执行了new')
# #         return object.__new__(cls)
#
# obj = Foo()
# 创造一个对象 比喻成 捏小人
# new 是小人捏出来了
# init 给小人穿衣服

# 设计模式 常用的23种
# java里来的
# python
    # 推崇设计模式 java开发
    # 贬低设计模式 纯python开发

# 单例模式
# 一个类 只有一个实例的时候 单例模式
# class Foo:
#     __instance = None
#     def __init__(self,name,age):                 # 初始化方法
#         self.name = name
#         self.age = age
#         self.lst = [name]
#     def __new__(cls, *args, **kwargs):  # 构造方法
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
# obj1 = Foo('alex',20)
# obj2 = Foo('egon',22)
# print(obj1.lst,obj2.lst)







