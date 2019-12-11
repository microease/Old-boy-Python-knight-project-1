# 没有在本文件中处理sys.path
# 这个时候在sys.path中没有D:\骑士计划PYTHON1期\day27\模块导入练习路径
import sys
print(sys.path)
from core import auth  # ModuleNotFoundError
def entry_point():
    auth.login()

# 类特别大 那么单独放到一个文件里
# Person Student(Person)










