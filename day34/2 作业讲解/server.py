import socket
from multiprocessing import Process
def communicate(conn):
    while True:
        conn.send(b'hello')
        print(conn.recv(1024))

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1',9000))
    sk.listen()

    while True:
        conn,addr = sk.accept()
        Process(target=communicate,args=(conn,)).start()
