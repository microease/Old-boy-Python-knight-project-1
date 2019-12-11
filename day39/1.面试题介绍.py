# 5个面试题的分享和讲解
    # 如果你有比较好的面试题 多分享
    # 面试题 ： 考试卷子、课上强调、课后练习题

# 以下代码的输出是什么？请给出答案并解释。
# def multipliers():
#     return [lambda x:i*x for i in range(4)]
# print([m(2) for m in multipliers()])
# 请修改multipliers的定义来产生期望的结果

# def multipliers():
#     l = []
#     i = 0
#     l.append(lambda x: i * x)
#     i = 1
#     l.append(lambda x: i * x)
#     i = 2
#     l.append(lambda x: i * x)
#     i = 3
#     l.append(lambda x: i * x)
#     return l
# l2 = []
# m = lambda x: 3 * 2
# m(2)

# def multipliers():
#     return (lambda x:i*x for i in range(4))
# print([m(2) for m in multipliers()])

# def multipliers():
#     for i in range(4):
#         yield lambda x:i*x
# print([m(2) for m in multipliers()])

# 2、程序从flag a执行到falg b的时间大致是多少秒？
# import time
# import threading
# def _wait():
# 	time.sleep(60)
# flag a
# start = time.time()
# t = threading.Thread(target=_wait,daemon = False)
# t.start()
# print(time.time() - start)
# flag b
# 整个程序执行完需要大概60s的时间，但是从flag a执行到falg b的时间非常短


# 3、程序从flag a执行到falg b的时间大致是多少秒？
# import time
# import threading
# def _wait():
# 	time.sleep(60)
# flag a
# t = threading.Thread(target=_wait,daemon = True)
# t.start()
# flag b
# 由于设置了守护线程，整个程序执行完需要的时间也非常短，从flag a执行到falg b的时间非常短


# 4、程序从flag a执行到falg b的时间大致是多少秒？
# import threading
# import time
# def _wait():
# 	time.sleep(60)
# # flag a
# t = threading.Thread(target=_wait,daemon = True)
# t.start()
# t.join()
# flag b
# 60s

# 读程序的题 并发

# 简述 进程、线程、协程的区别 以及应用场景？
# 进程
# 场景 利用多核、高计算型的程序、启动数量有限
    # 进程是计算机中最小的资源分配单位
    # 进程和线程是包含关系 每个进程中都至少有一条线程
    # 可以利用多核，数据隔离
    # 创建 销毁 切换 时间开销都比较大
    # 随着开启的数量增加 给操作系统带来负担

# 线程 高IO型 调度是我们不能干预的 我们只能写我们自己的逻辑
# 场景 一些协程协程现有的模块不能完成帮助我们规避IO操作的功能 适合使用多线程   urllib
    # 被CPU调度的最小单位，线程的切换时操作系统完成的
    # 在cpython解释器下不能利用多核，数据共享
    # 创建 销毁 切换 时间开销都比进程小很多
    # 随着开启的数量增加 给操作系统带来负担

# 协程 高IO型 用户可以自己控制的 我们能否抢占更多的资源完全取决于我们切换策略
# 场景 一些通用的场景 可以用协程现有的模块来规避一些IO操作适合使用协程
    # 协程的切换工作是用户完成的
    # 是一个线程，完全不能利用多核，不会产生数据不安全的现象
    # 多个任务之间互相切换不依赖操作系统，无论开启多少个协程都不会给操作系统带来负担










