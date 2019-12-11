# 检测数据库连接
# wait() 等待 事件内的信号编程True
# set()  把信号变成True
# clear  把信号变成False
# is_set 查看信号状态是否为True
# from threading import Event
#
# e = Event()
# print(e.is_set())
# e.wait(timeout = 5)
# print(e.is_set())
import time
import random
from threading import Event,Thread
def check(e):
    print('开始检测数据库连接')
    time.sleep(random.randint(1,5))  # 检测数据库连接
    e.set()  # 成功了

def connect(e):
    for i in range(3):
        e.wait(0.5)
        if e.is_set():
            print('数据库连接成功')
            break
        else:
            print('尝试连接数据库%s次失败'%(i+1))
    else:
        raise TimeoutError

e = Event()
Thread(target=connect,args=(e,)).start()
Thread(target=check,args=(e,)).start()

