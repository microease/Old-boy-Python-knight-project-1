# sys.argv
# sys.path
# sys.modules  查看当前内存空间中所有的模块，和这个模块的内存空间
import sys
# print(sys.path)

# 一个模块能否被导入，就看这个模块所在的目录在不在sys.path路径中
# 内置模块和第三方扩展模块都不需要我们处理sys.path就可以直接使用
# 自定义的模块的导入工作需要自己手动的修改sys.path

# print(sys.argv) # python D:/骑士计划PYTHON1期/day23/6.sys模块.py