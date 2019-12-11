# 同步
    # 一件事情做完再做另一件事情
# 异步
    # 同时做多件事情
    # 相对论 多线程 多进程 协程 异步的程序
        # 宏观角度 ：异步 并发聊天
# 阻塞
    # sleep input join shutdown get acquire wait
    # accept recv recvfrom
# 非阻塞
    # setblocking(False)

# 网络IO模型
# socket
# 用socket 一定会用到accept recv recvfrom这些方法
# 正常情况下 accept recv recvfrom都是阻塞的
# 如果setblocking(False) 整个程序就变成一个非阻塞的程序了

# 阻塞IO
# recv做了哪些事情
# 阻塞IO的recv，
    # wait for data阶段     阻塞
    # copy data   阶段      阻塞

# 非阻塞IO
# import time
# import socket
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.setblocking(False)   # 设置当前的socket server为一个非阻塞IO模型
# sk.listen()
# conn_l = []
# del_l = []
# while True:
#     try:
#         conn,addr = sk.accept()
#         conn_l.append(conn)   # [conn1,conn2]
#     except BlockingIOError:
#         for conn in conn_l:   # [conn1,conn2]
#             try:
#                 conn.send(b'hello')
#                 print(conn.recv(1024))
#             except (NameError,BlockingIOError):pass
#             except ConnectionResetError:
#                 conn.close()
#                 del_l.append(conn)
#         for del_conn in del_l:
#             conn_l.remove(del_conn)
#         del_l.clear()

# 没有并发编程的机制
# 同步的程序
# 非阻塞的特点
# 程序不会再某一个连接的recv或者sk的accept上进行阻塞
# 我就有更多的事件来做信息的收发工作

# 太多while True 高速运行着
# 大量的占用了CPU导致了资源的浪费

# 阻塞IO的问题：
#     一旦阻塞就不能做其他事情了
# 非阻塞IO的问题：
#     给CPU造成了很大的负担
































