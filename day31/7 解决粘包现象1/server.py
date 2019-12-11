import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9090))
sk.listen()

conn,addr = sk.accept()
s = input('>>>')  # 'a'*20
str(len(s))  # '20'
str(len(s)).zfill(4)+str(len(s))

 # 两个弊端
 # 复杂
 # 最多也只能一次性传递9999个字节

conn.send(b'0011hello,zhuge')
conn.send(b'0005world')
conn.close()

sk.close()

print('20'.zfill(4))

# 能够把不管多长的数据 都转换成一个4位的字节
# 10238976 -> 4位的字节
# 1位数    -> 4位的字节
# 简单





