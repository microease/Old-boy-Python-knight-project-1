# 调整好放假前的心态
# 调整好上课的状态
# 开始复习 整理出一部分大练习题、作业

# 线程
# 为什么要有锁
    # 保证数据安全
    # GIL保证只有一个线程能使用CPU
    # 每个线程拥有GIL锁的时间是有限的
        # 当一个线程已经到了GIL轮转的临界点的时候
        # 线程的调度 —— 操作系统的
        # 哪个线程处于就绪状态 —— Cpython解释器控制
        # 数据不安全的本质 ：一句python代码对应了多条cpu指令
        # dis模块查看cpu指令 ： load 读数据 func 放回去的过程
# 互斥锁和递归锁
    # 互斥锁 ：
        # 在一个线程里 只用一个锁的时候 互斥锁
        # 为了提高效率 锁多个资源的时候 应该酌情选用互斥锁
    # 递归锁 ：
        # 在一个线程里 用多个锁的时候 递归锁
        # 实例化一个锁 acquire两次
# 信号量和事件
# 条件和定时器
# 队列：优先级队列，栈，队列
    # mulprocessing 队列 IPC进城之间通信 在文件级别的
    # queue 队列 在内存级别的

import dis
# def func():
#     a = 0
#     a += 1

# dis.dis(func)

 # 24           4 LOAD_FAST                0 (a)
 #              6 LOAD_CONST               2 (1)
 #              8 INPLACE_ADD
 #             10 STORE_FAST               0 (a)
 #             12 LOAD_CONST               0 (None)
 #             14 RETURN_VALUE


# def func2():
#     a = 0
#     a+1
# dis.dis(func2)

