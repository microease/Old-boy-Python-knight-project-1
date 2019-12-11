import socket
sk = socket.socket(type = socket.SOCK_DGRAM)
sk.sendto('你好'.encode('utf-8'),('127.0.0.1',9000))
msg,addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
print('server addr :',addr)
sk.close()