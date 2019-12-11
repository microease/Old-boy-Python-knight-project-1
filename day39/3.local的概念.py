import time
import random
from threading import local,Thread

loc = local()
def func2():
    global loc
    print(loc.name,loc.age)


def func(name,age):
    global loc
    loc.name = name
    loc.age = age
    time.sleep(random.random())
    func2()

Thread(target=func,args=('alex',40)).start()
Thread(target=func,args=('boss_jin',38)).start()

# 多个线程之间 使用threading.local对象 可以实现多个线程之间的数据隔离