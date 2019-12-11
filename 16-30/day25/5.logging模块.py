# 什么是日志
# 无处不在的
# 所有的程序都必须记录日志

# 1.给用户看的
    # 购物软件
    # 视频软件
    # 银行卡
# 2.给内部人员看的
    # 给技术人员看的
        # 计算器
        # 500个小表达式
        # 一些计算过程、或者是一些操作过程需要记录下来
        # 程序出现bug的时候 来帮助我们记录过程 排除错误
    # 给非技术人员看的
        # 学校、公司的软件
            # 谁在什么时候做了什么事儿，删除操作

# print()
# f.write()

# import time
# class Student:
#     def __init__(self,name):
#         self.name = name
#
#     def select_course(self):
#         print('选课成功')
#         with open('log','a',encoding='utf-8') as f:
#             f.write('%s : %s选%s课成功'%(time.strftime('%H:%M:%S'),self.name,'python'))
#
# zhuge = Student('诸葛')
# zhuge.select_course()

import logging
# logging.basicConfig(level=logging.INFO)
# logging.debug('debug message')    # 计算或者工作的细节
# logging.info('info message')      # 记录一些用户的增删改查的操作
# logging.warning('input a string type') # 警告操作
# logging.error('error message')     # 错误操作
# logging.critical('critical message')  # 批判的 直接导致程序出错退出的

# 简单配置
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%c',
#                     filename='test.log')
# logging.warning('input a string type') # 警告操作
# logging.error('EOF ERROR ') # 警告操作
# logging.info('小明买了三斤鱼') # 警告操作

# 对象的配置
    # 解决中文问题
    # 同时向文件和屏幕输出内容

# 先创建一个log对象 logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# 还要创建一个控制文件输出的文件操作符
fh = logging.FileHandler('mylog.log')
# 还要创建一个控制屏幕输出的屏幕操作符
sh = logging.StreamHandler()
# 要创建一个格式
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fmt2 = logging.Formatter('%(asctime)s - %(name)s[line:%(lineno)d] - %(levelname)s - %(message)s')

# 文件操作符 绑定一个 格式
fh.setFormatter(fmt)
# 屏幕操作符 绑定一个 格式
sh.setFormatter(fmt2)
sh.setLevel(logging.WARNING)
# logger对象来绑定：文件操作符， 屏幕操作符
logger.addHandler(sh)
logger.addHandler(fh)


logger.debug('debug message')    # 计算或者工作的细节
logger.info('info message')      # 记录一些用户的增删改查的操作
logger.warning('input a string type') # 警告操作
logger.error('error message')     # 错误操作
logger.critical('critical message')  # 批判的 直接导致程序出错退出的
