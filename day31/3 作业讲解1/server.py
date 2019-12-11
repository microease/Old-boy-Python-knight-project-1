import os
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()   # ('127.0.0.1',9000)

conn,addr = sk.accept()  # ('127.0.0.1',9000) ('127.0.0.1',49513)
# 先传文件名
file_path = r'D:\video\5.网络基础2.mp4'
filename = os.path.basename(file_path)
conn.send(filename.encode('utf-8'))

# 再传文件
file_size = os.path.getsize(file_path)
with open(file_path,'rb') as f:
    while file_size:
        content = f.read(1024)
        file_size -= len(content)
        conn.send(content)
conn.close()
sk.close()



