import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9090))

while True:
    print(sk.recv(1024))
    sk.send(b'byebye')

