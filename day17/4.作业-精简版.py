# -*- coding: utf-8 -*-
# @Time    : 2018/8/27 14:38
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 4.作业.py
# @Software: PyCharm

# 对于文件的
# 增 删 改 查
# 增

# add Alex,22,13651054608,IT
    # Alex,22,13651054608,IT 按照逗号分隔开
    # 第一个值必须是字母开头的，第二个值必须是全数字，第三个值必须是11位全数字，最后一位20个字符

def add(sql):  # ' Alex, 22, 13651054608,IT'
    sql = sql.replace(' ','')  # sql = Alex,22,13651054608,IT
    with open('record') as f:
        index = int(f.read())
    line = '%s,%s\n'%(index+1,sql)
    with open('record','w') as f:
        f.write(str(index+1))
    with open('staff_info','a',encoding='utf-8') as f:
        f.write(line)

def read_line():
    with open('staff_info', encoding='utf-8') as f:
        for line in f:  # 2,Egon,23,13304320533,Tearcher
            lst = line.strip().split(',')  # lst = ['2','Egon','23','13304320533','Tearcher']
            yield lst

def filter(col_name,val,col_lst,condition):
    dic = {'id': 0, 'name': 1, 'age': 2, 'phone': 3, 'job': 4}
    for lst in read_line():
        if eval(condition):  # dic[col_name] = dic['age'] = 2 --> lst[dic[col_name] = lst[2]
            # 根据要显示的列进行显示
            for c in col_lst:  # 'name','age'
                print(lst[dic[c]], end=' ')
            print()

def select(sql):  # sql = name, age where age>22

    sql = sql.replace(' ','')  # sql = name,agewhereage>22
    col,con = sql.split('where')  # col = name,age  con = age>22
    col_lst = col.split(',')  # col_lst = ['name','age']
    # 先根据条件进行筛选
    if '>' in con:  # con = age>22
        col_name,val = con.split('>')   # col_name = 'age' val = '22'
        condition = 'int(lst[dic[col_name]]) > int(val)'
    elif '<' in con:
        col_name, val = con.split('<')
        condition = 'int(lst[dic[col_name]]) < int(val)'
    filter(col_name, val, col_lst, condition)
    'age=22'
    'agelike22'

while True:
    sql = input('>>>')
    if sql == 'q':
        break
    elif sql.startswith('add'):
        lst = sql.split('add')          # add Alex,22,13651054608,IT
        add(lst[1])
    elif sql.startswith('select'):     # select name, age where age>22
        lst = sql.split('select')
        select(lst[1])

# 基本
    # 功能
    # 安全
# 进阶
    # 性能 ：
        # 空间
        # 时间
    # 简洁度 ： 用很少的代码实现更多的功能
    # 可读性 ： 让其他人能更容易的读懂代码



