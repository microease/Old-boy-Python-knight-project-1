# 1. 类变量（静态属性）和实例变量（对象属性）的区别？
# 2. super的作用？在子类中调用父类的方法
# 一般情况下 子类中有和父类相同的方法名
# 3. isinstance和type的区别并用代码举例说明？
# isinstance能判断对象与类之间的继承关系
# type只能判断这个对象是哪个类创建出来的

# 4. 补全代码
#     ``` python
#     def func(arg):
#         """
#         判断arg是否可以被调用，如果可以则执行并打印其返回值，否则直接打印结果
#         :param arg: 传入的参数
#         """
#         pass

# def func(arg):
#     """
#     判断arg是否可以被调用，如果可以则执行并打印其返回值，否则直接打印结果
#     :param arg: 传入的参数
#     """
#     if callable(arg):
#         ret = arg()
#         print(ret)
#     else:
#         print('else : ',arg)
# class Foo:pass
#
# func(Foo)   # 类可以被调用，而对象不行
# obj = Foo()
# func(obj)

# 5. 补全代码
#     ``` python
#     def func(*args):
#         """
#         计算args中函数、方法、Foo类的对象的个数，并返回给调用者。
#         :param args: 传入的参数
#         """
#         pass
#     ```
# from types import MethodType,FunctionType
# def func(*args):
#     function_count = 0
#     method_count = 0
#     foo_obj = 0
#     for item in args:
#         if isinstance(item,FunctionType):
#             function_count += 1
#         elif isinstance(item,MethodType):
#             method_count += 1
#         elif isinstance(item,Foo):
#             foo_obj += 1
#     return {'function_count':function_count,'method_count':method_count,'foo_obj':foo_obj}
# def func1():pass
# def func2():pass
# class Foo:
#     def method1(self):pass
#     def method2(self):pass
#     def method3(self):pass
# f1 = Foo()
# ret = func(func1,func2,f1.method1,Foo.method1,Foo(),Foo())
# print(ret)


# 6. 看代码写结果并画图表示对象和类的关系以及执行流程
#     ``` python
# class StarkConfig(object):
#     list_display = []
#
#     def get_list_display(self):
#         self.list_display.insert(0,33)
#         return self.list_display
#
# class RoleConfig(StarkConfig):
#     list_display = [11,22]
#
# s1 = StarkConfig()
# s2 = StarkConfig()
#
# result1 = s1.get_list_display()    # self.list_display = [33]
# print(result1)
#
# result2 = s2.get_list_display()   # self.list_display = [33,33]
# print(result2)
#     ```
# 7. 看代码写结果并画图表示对象和类的关系以及执行流程
#     ``` python
class StarkConfig(object):
    list_display = []

    def get_list_display(self):
        self.list_display.insert(0,33)
        return self.list_display

class RoleConfig(StarkConfig):
    list_display = [11,22]

s1 = StarkConfig()
s2 = RoleConfig()

result1 = s1.get_list_display()
print(result1)

result2 = s2.get_list_display()
print(result2)
#     ```
# 8. 看代码写结果并画图表示对象和类的关系以及执行流程
#     ```python
# class StarkConfig(object):
#     list_display = []
#
#     def get_list_display(self):
#         self.list_display.insert(0,33)
#         return self.list_display
#
# class RoleConfig(StarkConfig):
#     list_display = [11,22]
#
# s1 = RoleConfig()
# s2 = RoleConfig()
#
# result1 = s1.get_list_display()
# print(result1)
#
# result2 = s2.get_list_display()
# print(result2)
#     ```
# 9. 看代码写结果
#     ```python
#     class Base(object):
#         pass
#
#     class Foo(Base):
#         pass
#
#     print(issubclass(Base, Foo))  # False


