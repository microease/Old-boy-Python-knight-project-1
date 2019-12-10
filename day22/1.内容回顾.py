# 路飞学城
    # 老村长
        # 你应该比你旁边的人更努力
        # 总得为自己负责任
    # 作业
        # 1. 在讲解之前就要尽量多写 ： 组内讨论 组间讨论
        # 2. 所有的作业讲解之后必须再写一遍
# 反射 用字符串类型的变量名来获取变量的值
    # hasattr(命名空间,'变量名')
    # getattr(命名空间,'变量名')
        # 类名.静态属性  getattr(类名,'静态属性')
        # 类名.类方法()  getattr(类名,'类方法')()
        # 类名.静态方法()  getattr(类名,'静态方法')()

        # 对象.对象属性  getattr(对象,'对象属性')
        # 对象.方法()    getattr(对象,'方法')()

        # 模块名.方法名
        # 模块名.类名
        # 模块名.变量
        # 模块名.函数

        # 本文件反射
        # import sys
        # getattr(sys.modules[__name__],'所有定义在这个文件中的名字')
    # setattr 给命名空间的某一个名字设置一个值
    # delattr 删除某一个命名空间中变量对应的值
# 内置方法
    # 不用调用调用这个方法就可以出发这个方法的执行
    # class Foo:
    #     def __str__(self):
    #         return 'abcd'
    #     def __repr__(self):
    #         return 'dcba'
    # obj = Foo()
    # __str__ ：
        # print(obj)
        # '%s'%obj
        # str(obj)
    # __repr__  : # 当使用会触发str方法的方式，但是Foo类内部又没有实现__str__方法的时候，都会调用__repr__
        # '%r'%obj
        # repr(obj)


