import socket
def upload():
    pass

def download():
    pass

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,addr = sk.accept()


conn.close()
sk.close()