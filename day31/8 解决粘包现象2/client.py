import socket
import struct
sk = socket.socket()
sk.connect(('127.0.0.1',9090))

while True:
    pack_num = sk.recv(4)
    num = struct.unpack('i',pack_num)[0]
    ret = sk.recv(num)
    print(ret.decode('utf-8'))
sk.close()