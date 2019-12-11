# blocking 阻塞
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.settimeout()
sk.listen()

while True:
    try:
        conn,addr = sk.accept()  # 如果没有人来连我 我不在这里等待
    except BlockingIOError:
        conn.recv()   # 也不阻塞了