import select  #  模块
import socket
# 用来操作操作系统中的select（IO多路复用）机制
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.setblocking(False)
sk.listen()

r_lst = [sk,]
print(sk)
while True:
    r_l,_,_ = select.select(r_lst,[],[])  # r_lst = [sk,conn1,conn2,conn3]
    for item in r_l:
        if item is sk:
            conn, addr = sk.accept()
            r_lst.append(conn)
        else:
            try:
                print(item.recv(1024))
                item.send(b'hello')
            except ConnectionResetError:
                item.close()
                r_lst.remove(item)

# io多路复用机制
# select windows、mac\linux
    # 底层是操作系统的轮询
    # 有监听对象个数的限制
    # 随着监听对象的个数增加，效率降低
# poll mac\linux
    # 底层是操作系统的轮询
    # 有监听对象个数的限制，但是比select能监听的个数多
    # 随着监听对象的个数增加，效率降低
# epoll mac\linux
    # 给每一个要监听的对象都绑定了一个回调函数
    # 不再受到个数增加 效率降低的影响

# socketserver
    # IO多路复用 + threading线程
# selectors模块
    # 帮助你在不同的操作系统上进行IO多路复用机制的自动筛选


# IO多路复用
# asycio tornado twisted


