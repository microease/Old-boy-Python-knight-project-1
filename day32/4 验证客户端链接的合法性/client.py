import hmac
import socket
def auth(sk):
    msg = sk.recv(32)
    result = hmac.new(key, msg)
    res = result.hexdigest()
    sk.send(res.encode('utf-8'))

key = b'alex_s'
sk = socket.socket()
sk.connect(('127.0.0.1',9000))
auth(sk)
sk.send(b'upload')
# 进行其他正常的和server端的沟通
sk.close()