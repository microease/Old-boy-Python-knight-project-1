import os
import json
import struct
base_path = r'D:\骑士计划PYTHON1期\day32\ftp\server\root'

def upload(conn,usr):
    fileinfo_len = conn.recv(4)
    fileinfo_len = struct.unpack('i',fileinfo_len)[0]
    fileinfo_str = (conn.recv(fileinfo_len)).decode('utf-8')
    fileinfo_dic = json.loads(fileinfo_str)
    file_path = os.path.join(base_path,usr,fileinfo_dic['filename'])
    with open(file_path,'wb') as f:
        while fileinfo_dic['filesize']:
            content = conn.recv(1024)
            fileinfo_dic['filesize'] -= len(content)
            f.write(content)
    print('接收完毕')