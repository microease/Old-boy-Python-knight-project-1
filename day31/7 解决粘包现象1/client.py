import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9090))

ret1 = sk.recv(4)
num1 = int(ret1.decode('utf-8'))
ret = sk.recv(num1)
print(ret)
ret2 = sk.recv(4)
num2 = int(ret2.decode('utf-8'))
ret = sk.recv(num2)
print(ret)
sk.close()

# 自定义了一个协议
# 4 表示要接受的长度
# 接下来根据要接受的长度来接收数据