# 进程是
    # 计算机中最小的资源分配单位
    # 进程对于操作系统来说还是有一定负担
    # 创建一个进程 操作系统要分配的资源大致有 ：
        # 代码
        # 数据
        # 文件

# 为什么要有线程
    # 轻量级的概念
    # 他没有属于自己的进程资源：
        # 一条线程只负责执行代码，没有自己独立的
        # 代码、变量、文件资源
# 什么是线程
    # 线程是计算机中被CPU调度的最小单位
    # 你的计算机当中的cpu都是执行的线程中的代码
# 线程和进程之间的关系
    # 每一个进程中都有至少一条线程在工作
# 线程的特点
    # 同一个进程中的所有线程的资源是共享的
    # 轻量级 没有自己的资源
# 进程和线程之间的区别
    # 占用的资源
    # 调度的效率
    # 资源是否共享
# 通用的问题
    # 一个进程中的多个线程能够并行么？
    # java c++ c#

# python中的线程
    # 一个进程中的多个线程能够并行么？ 不行
    # python是一个解释型语言
        # 为什么不行？
        # Cpython解释器 内部有一把全局解释器锁 GIL
            # 所以线程不能充分的利用多核
            # 同一时刻用一个进程中的线程只有一个能被CPU执行
        # GIL锁 确实是限制了你的程序效率
        # GIL锁 目前 是能够帮助你在线程的切换中提高效率
    # 是不是python就没有前途
        # cpu - 计算型
        # web 爬虫 金融分析
    # 就是想写高计算型
        # 多进程
        # 换一个解释器
























