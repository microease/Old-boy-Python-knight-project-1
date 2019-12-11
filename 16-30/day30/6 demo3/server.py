# tcp协议的socket
# server 网盘
# client 端 可以上传一个文件 到server端
import socket
sk = socket.socket()
sk.bind(('192.168.16.11',8080))
sk.listen()

conn,addr = sk.accept()
filename = conn.recv(1024)
print('-->filename ：',filename)
with open(filename,'wb') as f:
    content = conn.recv(4096)
    f.write(content)
conn.close()
sk.close()

# 大文件
# read
# 读一点儿 发一点儿
# 收一点儿 写一点儿
