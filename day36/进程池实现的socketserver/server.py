import socket
from multiprocessing import Pool
def talk(conn):
    try:
        while True:
            conn.send(b'hello')
            print(conn.recv(1024))
    finally:
        conn.close()

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1',9090))
    sk.listen()
    p = Pool()
    while True:
        conn,addr = sk.accept()
        p.apply_async(talk,args=(conn,))
    sk.close()

