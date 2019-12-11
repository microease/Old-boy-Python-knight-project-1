# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 10:59
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @Software: PyCharm

import sys
from conf.settings import *
from core.auth import login
from core.manager import Manager
from core.course import Course
from core.student import Student

def main():
    ret = login()
    if ret['result']:
        print('\033[1;32;40m登录成功\033[0m')
        if hasattr(sys.modules[__name__],ret['id']):
            cls = getattr(sys.modules[__name__],ret['id'])
            obj = cls.init(ret['name'])   # 实例化
            while True:
                for id,item in enumerate(cls.operate_lst,1):
                    print(id,item[0])
                func_str = cls.operate_lst[int(input('>>>')) - 1][1]
                print(func_str)
                if hasattr(obj,func_str):
                    getattr(obj,func_str)()
    else:
        print('登录失败')