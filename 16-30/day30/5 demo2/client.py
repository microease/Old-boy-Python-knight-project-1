import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))
while True:
    msg = sk.recv(1024)
    if msg == b'q':
        break
    print(msg.decode('utf-8'))
    re_msg = input('>>>')
    sk.send(re_msg.encode('utf-8'))
    if re_msg == 'q':
        break
sk.close()

#
