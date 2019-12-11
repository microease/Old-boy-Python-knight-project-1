# 4个屋子
# 10个人
import time
import random
from multiprocessing import Process,Semaphore

def ktv(person,sem):
    sem.acquire()
    print('%s走进ktv'%person)
    time.sleep(random.randint(1,5))
    print('%s走出ktv'%person)
    sem.release()

if __name__ == '__main__':
    sem = Semaphore(4)
    for i in range(10):
        p = Process(target=ktv,args=('person%s'%i,sem))
        p.start()

# 信号量的实现机制
    # 计数器 + 锁实现的
