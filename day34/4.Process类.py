import os
import time
import random
from multiprocessing import Process

# def func(index):
#     time.sleep(random.randint(1,3))
#     print('邮件已经发送完毕')
#
#
# if __name__ == '__main__':
#     p = Process(target=func, args=(1,))
#     p.start()
#     p.join()   # 阻塞 直到p进程执行完毕就结束阻塞
#     print('10个邮件已经发送完毕')

# def func(index):
#     time.sleep(random.random())
#     print('第%s个邮件已经发送完毕'%index)
#
# if __name__ == '__main__':
#     p_lst = []
#     for i in range(10):
#         p = Process(target=func,args=(i,))
#         p.start()
#         p_lst.append(p)
#     for p in p_lst:
#         p.join()
#     print('10个邮件已经发送完毕')

# 开启进程的第二种方式
# class MyProcess(Process):
#     def run(self):
#         print('子进程:',os.getpid(),os.getppid())
#
# if __name__ == '__main__':
#     p = MyProcess()
#     p.start()   # 开启一个子进程，让这个子进程执行run方法
#     print('主进程:',os.getpid())

# 开启进程的第二种方式 给子进程传参数
# class MyProcess(Process):
#     def __init__(self,arg):
#         super().__init__()
#         self.arg = arg
#     def run(self):
#         time.sleep(1)
#         print('子进程:',os.getpid(),os.getppid(),self.arg)
#
# if __name__ == '__main__':
#     # p = MyProcess('参数')
#     # p.start()   # 开启一个子进程，让这个子进程执行run方法
#     # p.join()
#     # print('主进程:',os.getpid())
#     for i in range(10):
#         p = MyProcess('参数%s'%i)
#         p.start()  # 开启一个子进程，让这个子进程执行run方法
#     print('主进程:', os.getpid())

