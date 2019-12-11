import socket
sk = socket.socket(type=socket.SOCK_DGRAM)

sk.sendto('%Y-%m-%d %H:%M:%S'.encode('utf-8'),('127.0.0.1',8848))
msg,_ = sk.recvfrom(1024)
print(msg.decode('utf-8'))

sk.close()


