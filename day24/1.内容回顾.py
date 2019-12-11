# time模块
    # 时间戳格式 浮点型
    # 结构化时间 元组
    # 格式化时间 字符串
        # '%Y %m % d %H %M %S'
    # 时间戳时间 -localtime/gmtime->  结构化时间 -strftime-> 格式化时间
    # 时间戳时间 <-mktime-  结构化时间 <-strptime- 格式化时间

# random模块
    # random.random 随机小数（0,1）
    # random.uniform 随机小数(n,m)
    # random.randint 随机整数 [n,m]
    # random.range(start,end,step)  随机整数 [n:m:s)
    # random.choice(list/range/tuple/str) 随机抽取一个值
    # random.sample(list/range/tuple/str,n) 随机抽取n个值
    # random.shuffle(list) 乱序，在原有基础上乱序

# os 和操作系统交互
    # 文件和文件夹的操作
        # os.remove
        # os.rename
        # os.mkdir
        # os.makedirs
        # os.rmdir
        # os.removedirs
        # os.listdir
        # os.stat 获取文件的信息
    # 路径的操作
        # os.path.join   目录的拼接
        # os.path.split(path) # 将路径分割成两个部分，目录、文件/文件夹的名字
        # os.path.dirname(path) # 返回这个path的上一级目录
        # os.path.basename(path) # 文件/文件夹的名字
        # os.path.exits  这个路径是否存在
        # os.path.isfile 是否文件目录
        # os.path.isdir  是否文件夹目录
        # os.path.abspath 规范文件目录、返回一个绝对路径
        # os.path.getsize
    # 和python程序的工作目录相关的
        # getcwd  # 获取当前的工作目录 get current working dir
        # chdir   # 改变当前的工作目录 change dir
    # 执行操作系统命令
        # os.system(命令)
        # os.popen(命令).read()
# __file__文件中的一个内置变量，描述的是这个文件的绝对路径
# sys 和python解释器
    # sys.argv 执行py文件的时候传入的参数
    # sys.path 查看模块搜索路径 import 模块的时候从这个路径下来寻找
    # sys.modules 查看当前导入的模块和它的命名空间