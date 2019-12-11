import time
from threading import Semaphore,Thread

def func(index,sem):
    sem.acquire()
    print(index)
    time.sleep(1)
    sem.release()

if __name__ == '__main__':
    sem = Semaphore(5)
    for i in range(10):
        Thread(target=func,args=(i,sem)).start()


# 信号量和池的区别
# 池
