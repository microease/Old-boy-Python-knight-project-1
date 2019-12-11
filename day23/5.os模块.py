import os
# os.mkdir('dirname')
# os.makedirs('dirname1/dirname2')

# os.rmdir('dirname')
# os.removedirs('dirname1/dirname2')

# ret = os.listdir('D:\骑士计划PYTHON1期')
# print(ret)

# print(os.stat('D:\骑士计划PYTHON1期\day13.py'))

# ret1 = os.path.abspath('D:/骑士计划PYTHON1期/day23/5.os模块.py')
# print(ret1)
# ret2 = os.path.abspath('5.os模块.py')
# print(ret2)

path = 'D:/骑士计划PYTHON1期/day23/5.os模块.py'
# ret = os.path.split(path)
# print(ret)
# ret1 = os.path.dirname(path)
# print(ret1)
# ret2 = os.path.basename(path)
# print(ret2)

# res = os.path.exists('D:/骑士计划PYTHON1期/day23/5.os模块.py')
# res = os.path.exists('D:/骑士计划PYTHON1期/day23/6.os模块.py')
# print(res)

# r1 = os.path.isfile('D:/骑士计划PYTHON1期/day23')
# r2 = os.path.isdir('D:/骑士计划PYTHON1期/day23')
# print(r1,r2)

# ret = os.path.join('D:/骑士计划PYTHON1期','day23')
# ret = os.path.abspath(ret)
# print(ret)

# size = os.path.getsize('D:/骑士计划PYTHON1期/day23/5.os模块.py')
# print(size)  # 大小
# size = os.path.getsize('D:/骑士计划PYTHON1期/day21')
# print(size)  # 大小

# windows 4096
    # 文件的信息
# linux、mac
    # 文件夹占的大小 32/64


# os.system("bash command")
# os.popen("bash command").read()
# os.getcwd()
# os.chdir("dirname")

# 操作系统命令
# python代码

# os.system('dir') # - 以字符串的形式来执行操作系统的命令
# exec - 以字符串的形式来执行python代码

# ret = os.popen('dir')
# print(ret.read())
# eval   以字符串的形式来执行python代码 且返回结果

# print('-->cwd : ',os.getcwd())
# open('file','w').close()   # 文件在执行这个文件的目录下创建了
# 不是当前被执行的文件所在的目录，而是执行这个文件所在的目录
# 工作目录在哪儿，所有的相对目录文件的创建，都是在哪儿执行这个文件，就在哪儿创建

# os.chdir('D:\骑士计划PYTHON1期\day23')
# open('file3','w').close()
# print('-->cwd : ',os.getcwd())

# print(__file__)







