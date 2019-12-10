# 模块
# 别人写好的功能放在一个文件里
# 内置模块  ： 安装python解释器的时候一起装上的
# 第三方模块、扩展模块 ：需要自己安装
# 自定义模块 ： 你写的py文件

# 序列化模块
# 序列
    # 列表
    # 元组
    # 字符串  *
    # bytes   *
# 什么叫序列化
    # 把一个数据类型转换成 字符串、byets类型的过程就是序列化
# 为什么要把一个数据类型序列化？
    # {'name':'何青松'，'sex':'male'}
    # 当你需要把一个数据类型存储在文件中
    # 当你需要把一个数据类型通过网络传输的时候
# 及其不安全的
# stu = {'name':'何青松','sex':'male'}
# ret = str(stu)
# print([ret])
# print([eval(ret)])  # 用户输入的、文件读入的、网络传入的

import json
# stu = {'name':'何青松','sex':'male'}
# ret = json.dumps(stu)  # 序列化的过程
# print(stu,type(stu))
# print(ret,type(ret))
#
# d = json.loads(ret)    # 反序列化的过程
# print('d-->',d,type(d))

# lst = [1,2,3,4,'aaa','bbb']
# ret = json.dumps(lst)  # 序列化的过程
# print(lst,type(lst))
# print(ret,type(ret))
#
# d = json.loads(ret)    # 反序列化的过程
# print('d-->',d,type(d))

# json的优点
    # 所有的语言都通用
# 缺点
    # 只支持非常少的数据类型
    # 对数据类型的约束很苛刻
        # 字典的key必须是字符串
        # 只支持 ： 数字 字符串 列表 字典

# stu = {'name':'何青松','sex':'male',1:('a','b')}
# ret = json.dumps(stu)  # 序列化的过程
# print(stu,type(stu))
# print(ret,type(ret))
# d = json.loads(ret)    # 反序列化的过程
# print('d-->',d,type(d))

import pickle
# stu = {'name':'何青松','sex':'male',1:('a','b')}
# ret = pickle.dumps(stu)
# print(ret)
# d = pickle.loads(ret)
# print(d,type(d))
class Course():
    def __init__(self,name,price):
        self.name = name
        self.price = price

python = Course('python',29800)
ret = pickle.dumps(python)
print(ret)

p = pickle.loads(ret)
print(p.name,p.price)