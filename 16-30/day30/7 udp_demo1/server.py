import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9000))

msg,addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))
print(addr)
sk.sendto('再见'.encode('utf-8'),addr)

sk.close()