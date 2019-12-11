import struct
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9090))
sk.listen()

conn,addr = sk.accept()
while True:
    s = input('>>>').encode('utf-8')
    pack_num = struct.pack('i',len(s))
    conn.send(pack_num)
    conn.send(s)

conn.close()
sk.close()
