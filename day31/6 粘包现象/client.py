import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9090))

ret1 = sk.recv(6)
print(len(ret1),ret1)
ret2 = sk.recv(5)
print(ret2)
sk.close()