# 协程
# 协程的本质
    # 在一条线程中执行多个任务，每个任务执行一段时间

# 扩展模块
# greenlet 底层的协程模块
    # 帮助我们进行在任务之间的切换
    # 只是单纯的切换，不能帮我们规避IO操作

# gevent
    # 能够自动帮我们检测程序中的IO操作
    # 并且在遇到IO操作的时候能帮助我们自动切换到不阻塞的任务执行

# 什么样的问题适合用协程来解决
    # 高IO、高并发

# 协程是用户级的切换
# 能够帮助我们让一条线程总是有执行要被执行
    # 这条线程总是在就绪和运行的状态之间切换
    # 能够抢占更多的cpu资源

# 线程池
    # concurrent.futures
    # ThreadPoolExcutor/ProcessPoolExcutor
    # submit/map
    # shutdown  等待池中的任务结束
    # result()  获取任务的返回值
    # add_done_callback 回调函数
        # 子线程/主进程执行

