# from gevent import monkey;monkey.patch_all()
# import socket
# import gevent
# from threading import current_thread
# def talk(conn):
#     print('-->',current_thread())
#     while True:
#         conn.send(b'hello')
#         conn.recv(1024)
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
#
# while True:
#     conn,addr = sk.accept()
#     gevent.spawn(talk,conn)


# 主线程 accept  基本上都是阻塞
# 任务一 talk
# 任务二 talk
# 任务三 talk
# 任务四 talk
# 任务五 talk

# 协程  500个任务提供服务
# 4c
# 进程 4
# 线程 20
# 协程 500

# 500*20*4 = 4w

# nginx
# 消息的接受和转发

# 框架的程序
# 自动化开发 运维经验 大规模的机器的管理
# 并发的需求


# 并发的内容
# 进程、线程   操作系统级别的调度
# 协程         用户界别的调度

# 基础概念
# 区别
# 线程数据安全的问题

# socket server
# 生产者消费者模型
# 爬取网页的例子（多线程 协程）











