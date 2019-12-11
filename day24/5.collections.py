# 内置的数据类型
    # int float complex
    # str list tuple
    # dict set
# 基础数据类型
    # int float complex
    # str list tuple
    # dict

# collections模块
    # 根据基础数据类型又做了一些扩展
    # 有序字典  py3.6以后自动有序
    # Counter   计数器
    # 默认字典
    # 可命名元组
    # 双端队列

# from collections import Iterable
# from collections import Iterator

# dic = {'a':1}
# d = dict([('a',1),('k1','v1')])
# print(d)

# s = '123'
# s = str('123')

# from collections import OrderedDict
# dd = OrderedDict([('a',1),('k1','v1')])
# print(dd)
# for k in dd:
#     print(k,dd[k])
# dd['k2'] = 'v2'
# print(dd)

from collections import defaultdict
# d = defaultdict(list)
# print(d['a'])
# d['b'].append(123)
# print(d)
# d = {}
# d['a']

# func = lambda :'default'
# d = defaultdict(func)
# print(d['kkk'])
# d['k'] = 'vvvvv'
# print(d)

# from collections import namedtuple
# birth = namedtuple('Struct_time',['year','month','day'])
# b1 = birth(2018,9,5)
# print(type(b1))
# print(b1.year)
# print(b1.month)
# print(b1.day)
# print(b1)
# 可命名元组非常类似一个只有属性没有方法的类
# ['year','month','day']是对象属性名
# Struct_time是类 的名字
# 这个类最大的特点就是一旦实例化 不能修改属性的值

# class A:
#     pass
# B = A
# a = A()
# b = B()
# print(type(a))
# print(type(b))

# 双端队列
# list的缺点
# 双端队列可以弥补
# 队列
# from collections import deque
# dq = deque()
# dq.append(1)
# dq.append(2)
# dq.appendleft(3)
# print(dq)
# print(dq.pop())
# print(dq.popleft())

# import queue
# q = queue.Queue()  # 队列
# q.put(1)
# q.put(2)
# q.put('aaa')
# q.put([1,2,3])
# q.put({'k':'v'})
# print(q.get())
# print(q.get())