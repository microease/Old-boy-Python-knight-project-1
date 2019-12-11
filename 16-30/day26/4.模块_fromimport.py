# from my_module import name
# print(name)
# from my_module import name,read2
# name = 'alex'
# read2()
# 在from import 的过程中发生了什么事儿
# 要找到my_module
# 开空间，执行my_module
# 所有的my_module中的名字都存储在my_module所属的空间中
# 建立一个引用name，read2分别取引用my_module空间中的名字
# from my_module import name
# from my_module import read2

# name = 'alex'
# from my_module import name
# print(name)

# from my_module import name,read1,read2
# from my_module import name as n,read1 as r1,read2 as r2

# from my_module import *
# print(name)
# read1()
# read2()

# from my_module import *
# print(name)
# read1()

# from my_module import read2
# read2()

# 模块的导入和修改
# import time
# import my_module
# print(my_module.name)
# time.sleep(10)
# print(my_module.name)

# import time
# import my_module
# print(my_module.name)
# time.sleep(10)
# import my_module
# print(my_module.name)

# from importlib import reload
# import time
# import my_module
# print(my_module.name)
# time.sleep(10)
# reload(my_module)
# print(my_module.name)

import my_module
print(dir(my_module))