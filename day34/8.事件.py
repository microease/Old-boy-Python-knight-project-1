# 事件
# Event
# 阻塞事件 ：wait()方法
    # wait是否阻塞是看event对象内部的一个属性

# 控制这个属性的值
    # set() 将这个属性的值改成True
    # clear()  将这个属性的值改成False
    # is_set() 判断当前的属性是否为True

# 红绿灯
# 红灯停 绿灯行
# import time
# import random
# from multiprocessing import Process,Event
# def traffic_light(e):
#     print('\033[31m红灯亮\033[0m')
#     while True:
#         if e.is_set():
#             time.sleep(2)
#             print('\033[31m红灯亮\033[0m')
#             e.clear()
#         else:
#             time.sleep(2)
#             print('\033[32m绿灯亮\033[0m')
#             e.set()
#
# def car(e,i):
#     if not e.is_set():
#         print('car %s 在等待' % i)
#         e.wait()
#     print('car %s 通过了'%i)
#
# if __name__ == '__main__':
#     e = Event()
#     p = Process(target=traffic_light,args=(e,))
#     p.start()
#     for i in  range(20):
#         time.sleep(random.randrange(0,3,2))
#         p = Process(target=car,args=(e,i))
#         p.start()

import time
import random
from multiprocessing import Process,Event
def traffic_light(e):
    print('\033[31m红灯亮\033[0m')
    while True:
        if e.is_set():
            time.sleep(2)
            print('\033[31m红灯亮\033[0m')
            e.clear()
        else:
            time.sleep(2)
            print('\033[32m绿灯亮\033[0m')
            e.set()

def car(e,i):
    if not e.is_set():
        print('car %s 在等待' % i)
        e.wait()
    print('car %s 通过了'%i)

if __name__ == '__main__':
    e = Event()
    p = Process(target=traffic_light,args=(e,))
    p.daemon = True
    p.start()
    p_lst = []
    for i in  range(20):
        time.sleep(random.randrange(0,3,2))
        p = Process(target=car,args=(e,i))
        p.start()  # car19
        p_lst.append(p)
    for p in p_lst:p.join()
