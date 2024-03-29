# 交作业
# 考试 28号
# tcp是流式传输，字节流，数据与数据之间是没有边界的
    # 流式传输
        # 不限定长度
        # 可靠传输
    # 慢
    # 和一个人的通信连接conn会一直占用我们的通信资源

# udp协议 面向数据包的传输
    # 数据包
    # ip port mac ip port mac hello
        # 不能传输过长的数据
        # 不可靠
    # 快
    # 由于不需要建立连接，所以谁发消息我都能接收到

# 粘包现象
    # 由于流式传输的特点 产生了数据连续发送的粘包现象
        # 在一个conn建立起来的连接上传输的多条数据是没有边界的
    # 数据的发送和接收实际上不是在执行send/recv的时候就立刻被发送或者接收
    # 而是需要经过操作系统内核
    # Nagle算法 能够将发送间隔时间得很近的短数据合成一个包发送到接收端
        # send(5)   --> recv(1024)  收到11个字节  多收了
        # send(6)
    # 拆包机制  当要发送的数据超过了网络上能传输的最大长度，就会被tcp协议强制拆包
        # send(4096)    --> recv(4096)  # 少收了
        # 4096 拆成4个包 --> 2048
    # 如果是短数据 ：只需要告诉对方边界就可以了
    # 如果是长数据 ：不仅要告诉对方边界，还要保证对面完整的接受了

# 解决粘包问题
    # struct
    # pack('i',len(msg))   # 把数字转成4字节
    # num = unpack('i',bytes)[0]  # 把4字节转回数字







