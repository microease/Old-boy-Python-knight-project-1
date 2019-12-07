# coding:utf-8
# File Name：     数据的提取
# Description :
# Author :       micro
# Date：          2019/12/3
file_path = "D:\Dropbox\\2骑士计划Python第一期\day08up 文件操作、读写追加操作\视频\下午技术分享\\csdn600w.txt"
save_file_path = "./email.txt"
save_file_open = open(save_file_path,"wb")
file = open(file_path, "rb")
for line in file:
    line = line.decode("gbk", errors='ignore')
    listStr = line.split(" # ")
    save_file_open.write(listStr[2].encode())
save_file_open.close()
file.close()