# import time
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# #
# def func(i):
#     print('thread',i)
#     time.sleep(1)
#     print('thread %s end'%i)
#
# # tp = ThreadPoolExecutor(5)
# if __name__ == '__main__':
#     tp = ProcessPoolExecutor(5)
#     tp.submit(func,1)
#     tp.shutdown()
#     print('主线程')

# import time
# from concurrent.futures import ThreadPoolExecutor
# from threading import current_thread as cthread
#
# def func(i):
#     print('thread',i,cthread().ident)
#     time.sleep(1)
#     print('thread %s end'%i)
#
# tp = ThreadPoolExecutor(5)
# for i in range(20):
#     tp.submit(func,i)
# tp.shutdown()
# print('主线程')

# 获取返回值
# import time
# from concurrent.futures import ThreadPoolExecutor
# from threading import current_thread as cthread
#
# def func(i):
#     print('thread',i,cthread().ident)
#     time.sleep(1)
#     print('thread %s end'%i)
#     return i* '*'
#
# tp = ThreadPoolExecutor(5)
# ret_l = []
# for i in range(20):
#     ret = tp.submit(func,i)
#     ret_l.append(ret)
# for ret in ret_l:
#     print(ret.result())
# print('主线程')

# map
# import time
# from concurrent.futures import ThreadPoolExecutor
# def func(i):
#     print('thread',i)
#     time.sleep(1)
#     print('thread %s end'%i)
#     return i* '*'
#
# tp = ThreadPoolExecutor(5)
# res = tp.map(func,range(20))
# for i in res:print(i)

# 回调函数
# import time
# from concurrent.futures import ThreadPoolExecutor
# from threading import current_thread as cthread
# # 线程池的回调函数 子线程完成的
# def func(i):
#     print('thread',i,cthread().ident)
#     time.sleep(1)
#     print('thread %s end'%i)
#     return i* '*'
#
# def call_back(arg):
#     print('call back : ',cthread().ident)
#     print('ret : ',arg.result())
#
# tp = ThreadPoolExecutor(5)
# ret_l = []
# for i in range(20):
#     tp.submit(func,i).add_done_callback(call_back)
# print('主线程',cthread().ident)

# import os
# import time
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# #
# def func(i):
#     print('thread',i,os.getpid())
#     time.sleep(1)
#     print('thread %s end'%i)
#
# # tp = ThreadPoolExecutor(5)
# if __name__ == '__main__':
#     tp = ProcessPoolExecutor(5)
#     tp.submit(func,1)
#     tp.shutdown()
#     print('主线程',os.getpid())

# 回调函数
# import os
# import time
# from concurrent.futures import ProcessPoolExecutor
# from threading import current_thread as cthread
# # 线程池的回调函数 子线程完成的
# def func(i):
#     print('thread',i,os.getpid())
#     time.sleep(1)
#     print('thread %s end'%i)
#     return i* '*'
#
# def call_back(arg):
#     print('call back : ',os.getpid())
#     print('ret : ',arg.result())
#
# if __name__ == '__main__':
#     tp = ProcessPoolExecutor(5)
#     ret_l = []
#     for i in range(20):
#         tp.submit(func,i).add_done_callback(call_back)
#     print('主线程',os.getpid())

# 回调函数
    # 进程池 是由主进程实现的
    # 线程池 是由子线程实现的

# 线程池
    # 实例化线程池  ThreadPoolExcutor    5*cpu_count
    # 异步提交任务  submit / map
    # 阻塞直到任务完成 shutdown
    # 获取子线程的返回值 result
    # 回调函数      add_done_callback

# concurrent futrues
# 工作中
    # 多进程 cpu_count
    # 多线程 cpu_cpunt * 5
    # 20 * 4 = 80 并发





