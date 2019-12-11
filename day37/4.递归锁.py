# 例子
# import time
# from threading import Thread,Lock
#
# noodle_lock = Lock()
# fork_lock = Lock()
# def eat1(name):
#     noodle_lock.acquire()
#     print('%s拿到面条了'%name)
#     fork_lock.acquire()
#     print('%s拿到叉子了'%name)
#     print('%s吃面'%name)
#     time.sleep(0.3)
#     fork_lock.release()
#     print('%s放下叉子'%name)
#     noodle_lock.release()
#     print('%s放下面'%name)
#
# def eat2(name):
#     fork_lock.acquire()
#     print('%s拿到叉子了' % name)
#     noodle_lock.acquire()
#     print('%s拿到面条了'%name)
#     print('%s吃面'%name)
#     time.sleep(0.3)
#     noodle_lock.release()
#     print('%s放下面'%name)
#     fork_lock.release()
#     print('%s放下叉子' % name)
#
# if __name__ == '__main__':
#     name_list = ['alex','wusir']
#     name_list2 = ['nezha','yuan']
#     for name in name_list:
#         Thread(target=eat1,args=(name,)).start()
#     for name in name_list2:
#         Thread(target=eat2,args=(name,)).start()

# 死锁现象
# 两把锁
# 异步的
# 操作的时候 抢到一把锁之后还要再去抢第二把锁
# 一个线程抢到一把锁
# 另一个线程抢到了另一把锁

# from threading import Thread,RLock
# rlock = RLock()
# def func(name):
#     rlock.acquire()
#     print(name,1)
#     rlock.acquire()
#     print(name,2)
#     rlock.acquire()
#     print(name,3)
#     rlock.release()
#     rlock.release()
#     rlock.release()
#
# for i in range(10):
#     Thread(target=func,args=('name%s'%i,)).start()

# import time
# from threading import Thread,RLock
#
# fork_lock = noodle_lock = RLock()
# def eat1(name):
#     noodle_lock.acquire()
#     print('%s拿到面条了'%name)
#     fork_lock.acquire()
#     print('%s拿到叉子了'%name)
#     print('%s吃面'%name)
#     time.sleep(0.3)
#     fork_lock.release()
#     print('%s放下叉子'%name)
#     noodle_lock.release()
#     print('%s放下面'%name)
#
# def eat2(name):
#     fork_lock.acquire()
#     print('%s拿到叉子了' % name)
#     noodle_lock.acquire()
#     print('%s拿到面条了'%name)
#     print('%s吃面'%name)
#     time.sleep(0.3)
#     noodle_lock.release()
#     print('%s放下面'%name)
#     fork_lock.release()
#     print('%s放下叉子' % name)

# if __name__ == '__main__':
#     name_list = ['alex','wusir']
#     name_list2 = ['nezha','yuan']
#     for name in name_list:
#         Thread(target=eat1,args=(name,)).start()
#     for name in name_list2:
#         Thread(target=eat2,args=(name,)).start()

# 递归锁可以解决互斥锁的死锁问题
    # 互斥锁
        # 两把锁
        # 多个线程抢
    # 递归锁
        # 一把锁
        # 多个线程抢

# 递归锁能够快速的解决死锁问题
# 递归锁好不好？
    #

import time
from threading import Thread,Lock

fork_noodle_lock = Lock()
def eat1(name):
    fork_noodle_lock.acquire()
    print('%s拿到面条了'%name)
    print('%s拿到叉子了'%name)
    print('%s吃面'%name)
    time.sleep(0.3)
    fork_noodle_lock.release()
    print('%s放下叉子'%name)
    print('%s放下面'%name)


def eat2(name):
    fork_noodle_lock.acquire()
    print('%s拿到叉子了' % name)
    print('%s拿到面条了'%name)
    print('%s吃面'%name)
    time.sleep(0.3)
    fork_noodle_lock.release()
    print('%s放下面'%name)
    print('%s放下叉子' % name)

if __name__ == '__main__':
    name_list = ['alex','wusir']
    name_list2 = ['nezha','yuan']
    for name in name_list:
        Thread(target=eat1,args=(name,)).start()
    for name in name_list2:
        Thread(target=eat2,args=(name,)).start()

# 递归锁可以解决互斥锁的死锁问题
    # 互斥锁
        # 两把锁
        # 多个线程抢
    # 递归锁
        # 一把锁
        # 多个线程抢

# 递归锁好不好？
    # 递归锁并不是一个好的解决方案
    # 死锁现象的发生不是互斥锁的问题
    # 而是程序员的逻辑有问题导致的
    # 递归锁能够快速的解决死锁问题
# 递归锁
    # 迅速恢复服务 递归锁替换互斥锁
    # 在接下来的时间中慢慢把递归锁替换成互斥锁
        # 能够完善代码的逻辑
        # 提高代码的效率
# 多个线程之间，用完一个资源再用另外一个资源
# 先释放一个资源，再去获取一个资源的锁

# a = 0
# b = 1
# acquire()
# c = a+b
# release()
#
# a = 0
# b = 1
# acquire()
# a += 1
# release()
# acquire()
# b -= 1
# release()










