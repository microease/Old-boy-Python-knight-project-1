# 锁
# 抢票
# import time
# import json
# from multiprocessing import Process,Lock
# def search(person):
#     with open('ticket') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     print('%s查询余票 :'%person,dic['count'])
#
# def get_ticket(person):
#     with open('ticket') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     if dic['count'] > 0:
#         print('%s买到票了'%person)
#         dic['count'] -= 1
#         time.sleep(0.2)
#         with open('ticket','w') as f:
#             json.dump(dic,f)
#     else:
#         print('%s没买到票'%person)
#
# def ticket(person,lock):
#     search(person)
#     lock.acquire()
#     get_ticket(person)
#     lock.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10):
#         p = Process(target=ticket,args=('person%s'%i,lock))
#         p.start()
#         # p.join()

# 为了保证数据的安全
# 在异步的情况下，多个进程又可能同时修改同一份资源
# 就给这个修改的过程加上锁

# 加锁
# 降低了程序的效率，让原来能够同时执行的代码变成顺序执行了，异步变同步的过程
# 保证了数据的安全

# import time
from multiprocessing import Process,Lock
# def func(num,lock):
#     time.sleep(1)
#     print('异步执行',num)
#     lock.acquire()
#     time.sleep(0.5)
#     print( '同步执行',num)
#     lock.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10):
#         p = Process(target=func,args=(i,lock))
#         p.start()

# 锁
# 互斥锁Lock
# lock = Lock()
# lock.acquire()
# print('456')
# lock.release()
# lock.acquire()
# print('123')





