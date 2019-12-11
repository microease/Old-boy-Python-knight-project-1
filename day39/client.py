import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))
for i in range(1000000):
    sk.send(b'world')
    print(sk.recv(1024))   # 收到对面的消息

sk.close()