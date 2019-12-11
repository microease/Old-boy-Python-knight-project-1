# 扫端口
# 0-65535
# server 银行的账务的管理系统 -->
# connect
# recv
# send

# tcp协议
# 没有做登录验证

# hmac生成对随机字符串的摘要
# secret_key = b'alex_sb'
# msg = os.urandom(32)
# result = hmac.new(secret_key,msg)
# print(result.hexdigest())

# ip + port
import os
import hmac
import socket
def auth(conn):
    msg = os.urandom(32)  # # 生成一个随机的字符串
    conn.send(msg)  # # 发送到client端
    result = hmac.new(secret_key, msg)  # 处理这个随机字符串，得到一个结果
    client_digest = conn.recv(1024)  # 接收client端处理的结果
    if result.hexdigest() == client_digest.decode('utf-8'):
        print('是合法的连接')  # 对比成功可以继续通信
        return True
    else:
        print('不合法的连接')  # 不成功 close
        return False


secret_key = b'alex_sb'
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()
conn,addr = sk.accept()
if auth(conn):
    print(conn.recv(1024))
    # 正常的和client端进行沟通了
    conn.close()
else:
    conn.close()
sk.close()




