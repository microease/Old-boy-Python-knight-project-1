# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 10:37
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 03 文件操作.py
# @Software: PyCharm

# f = open('d:\护士主妇空姐私密联系方式.txt',encoding='utf-8',mode='r')
# content = f.read()
# print(content)
# f.close()
'''
f, 变量f_obj,f_handler,f_h,fh,文件句柄。
open() python的内置函数（内部调用的是windows的系统命令），
1，打开文件，产生文件句柄。
2，对文件句柄进行操作。
3，关闭文件句柄。
'''

# 读
# r 对于r模式 mode可以默认不写
# f = open('d:\护士主妇空姐私密联系方式.txt',encoding='GB2312',mode='r')
# content = f.read()
# print(content)
# f.close()
# 1,全部读取
# f = open('文件操作1',encoding='utf-8',mode='r')
# content = f.read()  #
# print(content)
# f.close()

# 2,read(n)
# f = open('文件操作1',encoding='utf-8',mode='r')
# content = f.read(10)  # r 模式，按照字符读取。
# print(content)
# f.close()

# 3, 按行读取
# f = open('文件操作1',encoding='utf-8',mode='r')
# print(f.readline()) #
# print(f.readline()) #
# print(f.readline()) #
# print(f.readline()) #
# print(f.readline()) #
# print(f.readline()) #
# f.close()

# 4,按行读取，返回一个list
# f = open('文件操作1',encoding='utf-8',mode='r')
# content = f.readlines()
# print(content)
# f.close()
# rb


# 5,for 循环。
# f = open('文件操作1',encoding='utf-8',mode='r')
# for line in f:
#     print(line.strip())
# f.close()


# rb 文件操作中凡是 带b字母，都是与非文字类文件相关的。

# f = open('美女1.jpg',mode='rb')
# content = f.read()
# print(content)
# f.close()

# f = open('文件操作1',mode='rb')
# content = f.read(9)  # rb 模式 n 按照字节读取。
# print(content)
# f.close()

# r+ 读写：先读后追加。
# f = open('文件操作1',encoding='utf-8',mode='r+')
# content = f.read()
# print(content)
# f.write('666')
# f.close()

# f = open('文件操作1',encoding='utf-8',mode='r+')
# content = f.read(3)
# print(content)
# f.write('666')
# f.close()

# 不读直接写会怎样：直接从开始覆盖
# f = open('文件操作1',encoding='utf-8',mode='r+')
# f.write('深圳你好')
# f.close()
# r+b


# 写
#  w
# 没有文件，创建文件也要写。
# 有文件，先清空，后写入。

# f = open('文件操作2', encoding='utf-8',mode='w')
# f.write('深圳市南山区，福田区，罗湖区。。。')
# f.close()

# wb
# f = open('美女1.jpg',mode='rb')
# content = f.read()
# print(content)
#
# f1 = open(' 美女2.jpg',mode='wb')
# f1.write(content)
# f.close()
# f1.close()


# w+: 写读

# f = open('文件操作2', encoding='utf-8',mode='w+')
# f.write('深圳市南山区，福田区，罗湖区。。。')
# f.seek(3)  # 调整光标
# content = f.read()
# print(content)
# f.close()





# 追加

# a
# 没有文件，创建文件也要写。
# 有文件,直接在文件的最后面追加。
# f = open('文件操作3', encoding='utf-8',mode='a')
# f.write('\n南方水土好。。。')
# f.close()


# ab  a+ a+b

# 其他方法：readale ,writable,seek
# f = open('文件操作1',encoding='utf-8')
# if f.writable():
#     content = f.read()
#     print(content)
# f.close()

# seek 调整光标到开始，seek(0)  调整光标到结尾seek(0,2) *****
# f = open('文件操作1',encoding='utf-8')
# f.seek(6) # 按照字节去移动光标
# content = f.read()
# print(content)
# f.close()

# f = open('文件操作1',mode='rb')
# print(f.read())
# f.seek(6) # 按照字节去移动光标
# content = f.read()
# print(content)
# f.close()

# tell 告知光标的位置  *****
# f = open('文件操作1',encoding='utf-8')
# f.seek(0,2) # 按照字节去移动光标
# print(f.tell())
# f.close()

# truncate 要在writable模式下进行截取。
# r+ a+ ..不能在w模式下使用，对原文件进行截取
# f = open('文件操作1',encoding='utf-8',mode='r+')
# print(f.truncate(6))
# f.close()


# 1，主动关闭文件句柄
# with open('文件操作2',encoding='utf-8') as f1:
#     print(f1.read())
# 2，开启多个文件句柄。
# with open('文件操作2',encoding='utf-8') as f1,\
#         open('文件操作3',encoding='utf-8',mode='w') as f2:
#     print(f1.read())
#     f2.write('666666')


# 文件的改的操作

# 1，以读的模式打开原文件，产生一个文件句柄f1.
# 2,以写的模式创建一个新文件，产生一个文件句柄f2.
# 3,读取原文件内容，进行修改，并将修改后的写入新文件。
# 4，将原文件删除。
# 5，将新文件重命名成原文件。

#  low版
import os
with open('alex的深度剖析', encoding='utf-8') as f1,\
    open('alex的深度解析.bak',encoding='utf-8',mode='w') as f2:
    old_content = f1.read()
    new_content = old_content.replace('alex','SB')
    f2.write(new_content)
os.remove('alex的深度剖析')
os.rename('alex的深度解析.bak', 'alex的深度剖析')
#

import os
with open('alex的深度剖析', encoding='utf-8') as f1,\
    open('alex的深度解析.bak',encoding='utf-8',mode='w') as f2:
    for line in f1:
        new_line = line.replace('SB','alex')
        f2.write(new_line)
os.remove('alex的深度剖析')
os.rename('alex的深度解析.bak', 'alex的深度剖析')