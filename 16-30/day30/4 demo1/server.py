import socket

sk = socket.socket()  # 买手机
# sk.bind(('192.168.16.11',9000))  # 给新买的手机换上一张卡
sk.bind(('127.0.0.1',9000))  # 给新买的手机换上一张卡
sk.listen()           # 开机
while True:
    try:
        conn,addr = sk.accept()   #  等电话
        while True:
            msg = input('>>>')
            conn.send(msg.encode('utf-8'))# 说话
            msg = conn.recv(1024)         # 听对方说
            print(msg.decode('utf-8'))
        conn.close()                  # 挂电话
    except UnicodeDecodeError:
        pass

sk.close()

