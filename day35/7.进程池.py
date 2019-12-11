# 4c/8c/16c
# 为什么要有进程池？
# 开启过多的进程并不能提高你的效率
# 反而会降低效率

# 计算密集型  充分占用CPU 多进程可以充分利用多核
    # 适合开启多进程，但是不适合开启很多多进程
# IO密集型    大部分时间都在阻塞队列，而不是在运行状态中
    # 根本不太适合开启多进程

# 500个任务
# 5个进程

# 信号量
    # 500件衣服    任务
    # 500个人      进程
    # 只有4台机器  CPU

# 多进程
    # 500件衣服
    # 500个人
    # 抢4台机器

# 进程池
    # 500件衣服
    # 4个人
    # 4台机器
# import time
# from multiprocessing import Pool,Process
#
# def func(num):
#     print('做了第%s件衣服'%num)
#
# if __name__ == '__main__':
#     start = time.time()
#     p = Pool(4)
#     for i in range(100):
#         p.apply_async(func,args=(i,))  # 异步提交func到一个子进程中执行
#     p.close()    # 关闭进程池，用户不能再向这个池中提交任务了
#     p.join()     # 阻塞，直到进程池中所有的任务都被执行完
#     print(time.time() - start)

    # start = time.time()
    # p_lst = []
    # for i in range(100):
    #     p = Process(target=func,args=(i,))
    #     p.start()
    #     p_lst.append(p)
    # for p in p_lst:p.join()
    # print(time.time() - start)

import os
import time
from multiprocessing import Pool

# def task(num):
#     time.sleep(1)
#     print('%s : %s'%(num,os.getpid()))
#     return num**2
#
# if __name__ == '__main__':
#     p = Pool()
#     for i in range(20):
#         res = p.apply(task,args=(i,))   # 提交任务的方法 同步提交
#         print('-->',res)

# def task(num):
#     time.sleep(1)
#     print('%s : %s'%(num,os.getpid()))
#     return num**2
#
# if __name__ == '__main__':
#     p = Pool()
#     for i in range(20):
#         p.apply_async(task,args=(i,))   # 提交任务的方法 异步提交
#     p.close()
#     p.join()

# def task(num):
#     time.sleep(1)
#     print('%s : %s'%(num,os.getpid()))
#     return num**2
#
# if __name__ == '__main__':
#     p = Pool()
#     res_lst = []
#     for i in range(20):
#         res = p.apply_async(task,args=(i,))   # 提交任务的方法 异步提交
#         res_lst.append(res)
#     for res in res_lst:
#         print(res.get())

# def task(num):
#     time.sleep(1)
#     print('%s : %s'%(num,os.getpid()))
#     return num**2
#
# if __name__ == '__main__':
#     p = Pool()
#     p.map(task,range(20))
# 实例化 传参数 进程的个数 cpu/cpu+1
# 提交任务
    # 同步提交 apply
        # 返回值 ： 子进程对应函数的返回值
        # 一个一个顺序执行的，并没有任何并发效果
    # 异步提交 apply_async
        # 没有返回值，要想所有任务能够顺利的执行完毕
            # p.close()
            # p.join() # 必须先close再join，阻塞直到进程池中的所有任务都执行完毕
        # 有返回值的情况下
            # res.get() # get不能再提交任务之后立刻执行，应该是先提交所有的任务再通过get获取结果
        # map()方法
            # 异步提交的简化版本
            # 自带close和join方法

# 6个cpu
# 6-8个进程
# 6-8个任务
# 5000个任务

# 默写 生产者消费者模型
# 使用进程池 实现一个 socket 并发通信
# 整理进程池 和队列 这两个关键的知识点
# 继续完成ftp
# 准备一些进程方面的面试题

# 线程

