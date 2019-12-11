import os
import time
from threading import Thread
from multiprocessing import Process
# 并发
# def func(i):
#     print('子 ：',i,os.getpid())
#
# print('主 ：',os.getpid())
# for i in range(10):
#     t = Thread(target=func,args=(i,))
#     t.start()

# 轻量级
# def func(i):
#     print('子 ：',i,os.getpid())
#
# if __name__ == '__main__':
#     start = time.time()
#     t_lst = []
#     for i in range(100):
#         t = Thread(target=func,args=(i,))
#         t.start()
#         t_lst.append(t)
#     for t in t_lst:t.join()
#     tt = time.time()-start
#
#     start = time.time()
#     t_lst = []
#     for i in range(100):
#         t = Process(target=func, args=(i,))
#         t.start()
#         t_lst.append(t)
#     for t in t_lst: t.join()
#     pt = time.time() - start
#     print(tt,pt)

# 数据共享
# num = 100
# def func():
#     global num
#     num -= 1
#
# t_lst = []
# for i in range(100):
#     t = Thread(target=func)
#     t.start()
#     t_lst.append(t)
# for t in t_lst:t.join()
# print(num)
from threading import currentThread
def func():
    time.sleep(3)

# t = Thread(target=func)
# t.start()
# print(t.is_alive())
# print(t.getName())
# t.setName('t1')
# print(t.getName())


# from threading import currentThread
# def func():
#     print('子线程 ： ',currentThread().ident)
#     time.sleep(3)
#
# print('主线程 ： ',currentThread().ident)
# t = Thread(target=func)
# t.start()


# from threading import enumerate
# def func():
#     print('子线程 ： ',currentThread().ident)
#     time.sleep(3)
#
# print('主线程 ： ',currentThread().ident)
# for i in range(10):
#     t = Thread(target=func)
#     t.start()
# print(len(enumerate()))

# from threading import activeCount
# def func():
#     print('子线程 ： ',currentThread().ident)
#     time.sleep(3)
#
# print('主线程 ： ',currentThread().ident)
# for i in range(10):
#     t = Thread(target=func)
#     t.start()
# print(activeCount())