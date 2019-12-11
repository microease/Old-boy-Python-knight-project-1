import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))
while True:
    ret = sk.recv(1024)
    print(ret)
    sk.send(b'byebye')
sk.close()