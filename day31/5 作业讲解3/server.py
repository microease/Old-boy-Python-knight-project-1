import time
import socket

sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',8848))
while True:
    msg,addr = sk.recvfrom(1024)
    fmt_time = time.strftime(msg.decode('utf-8'))
    sk.sendto(fmt_time.encode('utf-8'),addr)

sk.close()