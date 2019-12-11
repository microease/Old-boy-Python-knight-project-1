# 线程为什么要有锁
    # GIL
    # 线程之间的数据安全问题 ：
        # += -= 赋值操作不安全
            # 1500000
            # 100 1500000 +=
            # 100 1500000 -=
        # pop append 都是线程安全的
        # 队列也是数据安全的
# 互斥锁和递归锁
    # 互斥锁

from threading import Thread,Lock
n = 0
def func(lock):
    global n
    for i in range(1500000):
        lock.acquire()
        n  -= 1
        lock.release()

def func2(lock):
    global n
    for i in range(1500000):
        lock.acquire()
        n += 1
        lock.release()

if __name__ == '__main__':
    t_lst = []
    lock = Lock()
    for i in range(10):
        t2 = Thread(target=func2,args=(lock,))
        t = Thread(target=func,args=(lock,))
        t.start()
        t2.start()
        t_lst.append(t)
        t_lst.append(t2)
    for t in t_lst:
        t.join()
    print('-->',n)


