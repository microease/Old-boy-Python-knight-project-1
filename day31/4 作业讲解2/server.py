import socket
sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9001))
fiends = {'苑昊':'\033[1;32;40m苑昊 : %s\033[0m','哪吒':'\033[1;33;44m哪吒 : %s\033[0m'}
while True:
    msg,addr = sk.recvfrom(1024)
    user,msg = msg.decode('utf-8').split(':')
    if msg.strip() == 'q':
        continue
    else:
        print(fiends[user]%msg)
    send_msg = input('>>>').encode('utf-8')
    sk.sendto(send_msg,addr)

sk.close()