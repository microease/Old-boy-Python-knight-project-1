import socket
# 下载
sk = socket.socket()
sk.connect(('127.0.0.1',9000)) # ('127.0.0.1',9000) ('127.0.0.1',97521)
filename = sk.recv(1024)
print('--> ',filename)
filename = filename.decode('utf-8')
with open(filename,'wb') as f:
    while True:
        content = sk.recv(1024)
        if content:
            f.write(content)
        else:break
sk.close()