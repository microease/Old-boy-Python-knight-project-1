# web qq
# ftp : struct定制协议
# 10240
# while filesize:
    # ret.send()

# 内容回顾
# Process
    # 创建进程对象
        # Process
        # MyProcess
    # 方法：
        # daemon   属性True 表示这个子进程为守护进程
        # start()  开启一个子进程
        # join()   阻塞直到子进程结束
# Lock
    # 锁 互斥锁
    # 在进程之间保证数据安全性
    # lock.acquire()
    # lock.release()
# Semaphore
    # 计数器+锁
# Event
    # 事件
    # 内部有一个信号控制wait的阻塞事件
    # 控制这个信号：
        # set()
        # clear()
        # is_set()

# 进程之间的通信？？？
    # 多个进程之间有一些固定的通信内容
    # 一些信号
    # socket 给予文件家族通信

# 进程之间虽然内存不共享，但是是可以通信的
    # Lock Semaphore Event 都在进行进城之间的通信
    # 只不过这些通信的内容我们不能改变

# 让进城之间通信





