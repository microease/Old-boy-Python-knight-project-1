import time
from multiprocessing import Process

# def func():
#     print('子进程 start')
#     time.sleep(3)
#     print('子进程 end')
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.daemon = True     # 设置p为一个守护进程，必须在start之前完成
#     p.start()
#     time.sleep(2)
#     print('主进程')

# 主进程会等待子进程完全结束才结束
# 主进程还会等待子进程结束么？？？
# 守护进程会随着主进程的代码执行完毕而结束

def func1():
    count = 1
    while True:
        time.sleep(0.5)
        print(count*'*')
        count += 1

def func2():
    print('func2 start')
    time.sleep(5)
    print('func2 end')

if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.daemon = True
    p1.start()
    Process(target=func2).start()
    time.sleep(3)
    print('主进程')

# 如果主进程代码已经执行完毕，但是子进程还没执行完，守护进程都不会继续执行
# 守护进程会随着主进程的代码执行完毕而结束
# 主进程会等待子进程结束，守护进程只等待主进程代码结束就结束了

# 程序的报活
# 主程序
# 守护进程 ：每隔五分钟就向一台机器汇报自己的状态

def func():
    while True:
        time.sleep(5*60)
        print('我还活着')

def main():
    print('主程序会7*24小时的提供服务')

# 10个服务
# 第11个服务 ： 检测其它10个服务是否还活着


