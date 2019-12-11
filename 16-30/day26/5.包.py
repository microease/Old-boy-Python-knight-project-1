# 从包中导入模块
# import
# import glance2.api.policy
# glance2.api.policy.get()
#
# import glance2.api.policy as policy
# policy.get()

# from import
# from glance2.api import policy
# policy.get()

# from glance2.api.policy import get
# get()

# 导入包
# 绝对导入
# glance2.api.policy.get()
# 导入包的过程中发生了什么事？
# 相当于执行了这个包的 __init__.py文件
# sys.path中的内容 永远是当前你执行的文件
# ['D:\骑士计划PYTHON1期\day26']

# 相对导入  运用了相对导入的文件不能被直接执行
# '.'表示当前目录
# '..'表示上一级目录
# import glance3
from outer import glance3









