# 6天
# 网络编程 + 并发编程 60分
# 周二 : 线程
# 周三 : 协程
# 周四 : IO多路复用
# 周五 : 数据库day1、下午考试
# 周六 : 数据库day2
# 周日 : 数据库day3
    # 5天
    # 数据库的基本操作 3天
    # 进阶知识 ： 数据库性能的优化\数据库中进阶的工具 2天
    # python中的模块操作mysql数据库
# 十一假期 : 数据库作业
# 前端 : html css js jq

# 交作业 ：6点之前 ftp

# 线程
# 线程和进程之间的关系
    # 每个进程内都有一个线程
    # 线程是不能独立存在的
# 线程和进程之间的区别
    # 同一个进程中线程之间的数据是共享的
    # 进程之间的数据是隔离的
    # 线程是被cpu执行的最小单位
        # 操作系统调度
    # 进程是计算机中最小的资源分配单位
# python
    # GIL锁 全局解释器锁 全局锁
        #  cpython解释器中的
        # 锁线程 ：同一时刻同一个进程只会有一个线程访问CPU
            # 锁的是线程而不是数据
    # 当程序是高IO型的 多线程
    # 当程序是高计算(CPU)型的 多进程
        # cpu*1 ~ cpu*2

# threading
# Thread
    # 守护线程 ：主线程结束之后才结束

# socket_server IO多路复用 + 多线程
# 框架 并发的效果 ：多线程、协程的概念 flask
# 爬虫 ：线程池 协程

# set、dict、list
# 生成器
# 面向对象的进阶 ：魔术方法
# 管道
# socket_server的源码