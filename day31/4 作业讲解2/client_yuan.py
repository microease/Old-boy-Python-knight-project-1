import socket

sk = socket.socket(type = socket.SOCK_DGRAM)
addr = ('127.0.0.1',9001)
user = '苑昊'
while True:
    send_msg = input('>>>')
    sk.sendto(('%s:%s'%(user,send_msg)).encode('utf-8'),addr)
    if send_msg == 'q':
        break
    msg,_ = sk.recvfrom(1024)
    print(msg.decode('utf-8'))

sk.close()