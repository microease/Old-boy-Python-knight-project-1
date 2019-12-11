import time
from threading import Thread
def func1():
    while True:
        time.sleep(0.5)
        print(123)

def func2():
    print('func2 start')
    time.sleep(3)
    print('func2 end')

t1 = Thread(target=func1)
t2 = Thread(target=func2)
t1.setDaemon(True)
t1.start()
t2.start()
print('主线程的代码结束')

# 守护线程 是在主线程代码结束之后，还等待了子线程执行结束才结束
# 主线程结束 就意味着主进程结束
# 主线程等待所有的线程结束
# 主线程结束了之后 守护线程随着主进程的结束自然结束了

# 基于threading模块socket server
# ftp

