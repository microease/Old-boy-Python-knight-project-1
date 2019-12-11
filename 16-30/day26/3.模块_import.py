# import my_module
# 在import的过程中发生了哪些事情
# import一个模块相当于执行了这个模块

# 一个模块能不能被重复导入？？？不会
# import my_module

# 如何去使用被导入模块中的名字？
# print(my_module.name)
# my_module.read1()
# name = 'zhuge'
# print(name)

# 在import模块的时候发生的事情
# 1.寻找模块
# 2.如果找到了，就开辟一块儿空间，执行这个模块
# 3.把这个模块中用到的名字都收录到新开辟的空间中
# 4.创建一个变量来引用这个模块的空间

# *1.模块不会被重复导入
# *2.模块和文件之间的内存空间始终是隔离的
# *3.模块的名字必须是符合变量命名规范的

# import my_module
# my_module.read2()
# name = 'alex'
# my_module.read2()
# my_module.name = 'alex'
# my_module.read2()

# 导入多个模块
# import os,time,my_module

# 注意：
# pep8规范
# import os
# import time
# import my_module
# 内置，第三方，自定义
# import os
#
# import django
#
# import my_module

# 给模块起别名
# m.name
# my_module.name

# def dump(method):
#     if method == 'json':
#         import json
#         with open('file','w') as f:
#             json.dump([1,2,3],f)
#     elif method == 'pickle':
#         import pickle
#         with open('file', 'w') as f:
#             pickle.dump([1, 2, 3], f)

# def dump(method):
#     if method == 'json':
#         import json as m
#     elif method == 'pickle':
#         import pickle as m
#     with open('file', 'w') as f:
#         m.dump([1, 2, 3], f)

# 模块搜索路径
# import sys
# print(sys.path)
# import my_module

# 正常的sys.path中出了内置、扩展模块所在的路径之外
# 只有一个路径是永远不会出问题
    # 你直接执行的这个文件所在的目录
# 一个模块是否能被导入，就看这个模块所在的目录在不在sys.path中
# import my_module2  # ModuleNotFoundError

# import sys
# sys.path.append('D:\骑士计划PYTHON1期\day26\glance')
# import my_module2

# 两种运行一个py文件的方式
# 直接运行它 ： cmd python xx.py  pycharm  脚本
# __name__ == '__main__'
# 导入它 ： 模块
# __name__ == '模块名'
# import my_module
# my_module