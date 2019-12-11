import socket
from threading import Thread
def client():
    sk = socket.socket()
    sk.connect(('127.0.0.1',9000))
    while True:
        print(sk.recv(1024))
        sk.send(b'byebye')

for  i in range(5):
    Thread(target=client).start()