# hashlib
# 模块
# 内部有算法的模块
# 内部不止一种算法

# 由于数据的不安全性，为了保证用户的信息绝对的安全，所以所有人的密码都不能以
# 明文的形式存储，而应该经过适当的处理以密文的形式存起来。

# 大家去计算这个密文 使用的是相同的算法
# alex3714
# 这个算法不可逆
# 不同的字符串通过这个算法的计算得到的密文总是不同的
# 相同的算法 相同的字符串 获得的结果总是相同的
    # 不同的语言 不同的环境(操作系统、版本、时间)

import hashlib

# md5_obj = hashlib.md5()
# # md5_obj.update(b'alex3714')
# md5_obj.update('999'.encode('utf-8'))
# ret = md5_obj.hexdigest()
# print(ret,type(ret),len(ret))

# def get_md5(s):
#     md5_obj = hashlib.md5()
#     md5_obj.update(s.encode('utf-8'))
#     ret = md5_obj.hexdigest()
#     return ret
#
# usrname = input('username : ')
# passwd = input('password : ')
# with open('userinfo') as f:
#     for line in f:
#         usr,pwd = line.strip().split('|')
#         if usrname == usr and get_md5(passwd) == pwd:
#             print('登录成功')
#             break
#     else:
#         print('登录失败')

# 1.文件操作 ： f.readlines()浪费内存
# 2.md5_obj不能重复使用
# md5_obj = hashlib.md5()
# md5_obj.update('alex3714'.encode('utf-8'))
# ret = md5_obj.hexdigest()
#
# md5_obj2 = hashlib.md5()
# md5_obj2.update('666'.encode('utf-8'))
# ret = md5_obj2.hexdigest()

# hashlib 摘要算法
# 多种算法
# md5算法 ：32位16进制的数字字符组成的字符串
    # 应用最广大的摘要算法
    # 效率高，相对不复杂，如果只是传统摘要不安全
# sha算法 ：40位的16进制的数字字符组成的字符串
    # sha算法要比md5算法更复杂
    # 且shan n的数字越大算法越复杂，耗时越久，结果越长，越安全
# sha_obj = hashlib.sha512()
# sha_obj.update('alex3714'.encode('utf-8'))
# ret = sha_obj.hexdigest()
# print(len(ret))

# def get_md5(s):
#     md5_obj = hashlib.md5()
#     md5_obj.update(s.encode('utf-8'))
#     ret = md5_obj.hexdigest()
#     return ret
#
# print(get_md5('111111'))
# print(get_md5('123456'))
# print(get_md5('alex3714'))
# print(get_md5('999'))

# 撞库

# 加盐
# def get_md5(s):
#     md5_obj = hashlib.md5('盐'.encode('utf-8'))
#     md5_obj.update(s.encode('utf-8'))
#     ret = md5_obj.hexdigest()
#     return ret
# 恶意的注册账号
# 张三|666
# 李四|999
# print(get_md5('666'))

# 动态加盐
# 每一个用户创建一个盐 - 用户名
# def get_md5(user,s):
#     md5_obj = hashlib.md5(user.encode('utf-8'))
#     md5_obj.update(s.encode('utf-8'))
#     ret = md5_obj.hexdigest()
#     return ret
#
# print(get_md5('alex','alex3714'))
# print(get_md5('wusir','666'))
# print(get_md5('zhangsan','666'))


# 登录验证 - hashlib
    # 两种算法 md5，sha
    # 常规验证 - 撞库
    # 加盐 - 固定的盐 会导致恶意注册的用户密码泄露
    # 动态加盐 - 每个用户都有一个固定的并且互不相同的盐

# 文件的一致性校验
# 给一个文件中的所有内容进行摘要算法得到一个md5的结果
# 铺垫知识
import hashlib

# md5_obj = hashlib.md5()
# md5_obj.update('hello,world'.encode('utf-8'))
# ret = md5_obj.hexdigest()
# print(ret)

# 3cb95cfbe1035bce8c448fcaf80fe7d9
# 3cb95cfbe1035bce8c448fcaf80fe7d9
# md5_obj = hashlib.md5()
# md5_obj.update('hello'.encode('utf-8'))
# md5_obj.update(',world'.encode('utf-8'))
# ret = md5_obj.hexdigest()
# print(ret)

# def get_file_md5(file_path):
#     md5_obj = hashlib.md5()
#     with open(file_path,encoding='utf-8') as f:
#         for line in f:
#             md5_obj.update(line.encode('utf-8'))
#     ret = md5_obj.hexdigest()
#     print(ret)  # ca3f1aebfe1810a6035971b63599e75a
#
# get_file_md5('1.内容回顾.py')
# get_file_md5('1.内容回顾.py.bak')

# 下载的是视频、或者大文件
# 应该是以rb的形式来读 读出来的都是bytes
# 并且不能按行读 也不能一次性读出来
# getsize()  -->  字节大小
# 10240
# 1024
# ‪D:\讲师课程文件\python讲师 Jingliyang\day24\video\3.习题讲解2.mp4
import os
import hashlib
def get_file_md5(file_path,buffer = 1024):
    md5_obj = hashlib.md5()
    # file_path = r'3.习题讲解2.mp4'   # 路径里不能有空格
    file_size = os.path.getsize(file_path)
    with open(file_path,'rb') as f:
        while file_size:
            content = f.read(buffer)   # 1024 1024 1024  。。。 5
            file_size -= len(content) #  5 -=5
            md5_obj.update(content)
    return md5_obj.hexdigest()

print(get_file_md5( r'3.习题讲解2.mp4'))

# 666666
# 999999
# import hashlib
# md51 = hashlib.md5()
# md51.update(b'666666')  # f379eaf3c831b04de153469d1bec345e
# print(md51.hexdigest())

# md51 = hashlib.md5()
# md51.update(b'999999')  # 52c69e3a57331081823331c4e69d3f2e
# print(md51.hexdigest())

# md51 = hashlib.md5()
# md51.update(b'666666')
# md51.update(b'999999')   # 1ad2daed30c3862a267485c7cc9aacce
# print(md51.hexdigest())
#
# md51 = hashlib.md5()
# md51.update(b'666666999999') # 1ad2daed30c3862a267485c7cc9aacce
# print(md51.hexdigest())