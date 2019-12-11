import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

while True:
    conn,addr = sk.accept()
    while True:
        conn.send(b'hello')
        print(conn.recv(1024))