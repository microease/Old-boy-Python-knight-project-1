import os
import json
import struct
import socket
def my_send(opt_dic):
    str_opt = json.dumps(opt_dic).encode('utf-8')
    b_len = struct.pack('i', len(str_opt))
    sk.send(b_len)
    sk.send(str_opt)

# 下载
file_path = r'D:\video\5.网络基础2.mp4'
sk = socket.socket()
sk.connect(('127.0.0.1',9000))
operates = [('上传','upload'),('下载','download')]
for num,item in enumerate(operates,1):
    print(num,item[0])
choose = int(input('请选择您要做的操作 ：'))
operate = operates[choose-1][1]
# 上传，下载
opt_dic = {'operate':operate}
my_send(opt_dic)
# 发送要下载的文件的地址 ：
# 在客户端是由用户选择的
# 选择的这个路径应该是发送到server端拼成一个绝对路径laichuli

# 发送一个绝对路径
file_info = {'filepath':file_path}
my_send(file_info)

sk.recv() # 文件的总大小，文件的名字
# 等着下载 - 接收数据
# with open(filename,'wb') as f:
#     # 不知道要收多大的数据
#     pass

sk.close()