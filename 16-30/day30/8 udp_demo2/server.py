import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9000))

while True:
    msg,addr = sk.recvfrom(1024)
    # '老班长|msg'
    print(addr , msg.decode('utf-8'))
    msg_send = input('>>>')
    sk.sendto(msg_send.encode('utf-8'),addr)
    # '诸葛|recv_msg'
sk.close()