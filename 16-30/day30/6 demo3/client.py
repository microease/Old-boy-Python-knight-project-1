import time
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',8080))

sk.send('4.笔记.py'.encode('utf-8'))
time.sleep(0.1)
with open(r'D:\骑士计划PYTHON1期\day29\4.笔记.py','rb') as f:
    content = f.read()
    print('len  : ',len(content))
    sk.send(content)
sk.close()