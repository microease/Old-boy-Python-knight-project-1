# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 9:25
# @Author  : 骑士计划
# @Email   : customer@luffycity.com
# @File    : 02 作业讲解.py
# @Software: PyCharm

# s1 = '太白'
# b1 = s1.encode('gbk')
# print(b1)
# s2 = b1.decode('gbk')  # unicode 的字符串
# b2 = s2.encode('utf-8')
# print(b2)

# s1 = 'alex'
# b1 = s1.encode('gbk')
# s2 = b1.decode('utf-8')
# print(s2)

# 上面代码能成立：因为utf-8 gbk,unicode等编码的英文字母，数字，特殊字符都是映射的ascii码。

# 商品列表：
# 	 goods = [{"name": "电脑", "price": 1999},
#          {"name": "鼠标", "price": 10},
#          {"name": "游艇", "price": 20},
#          {"name": "美女", "price": 998}, ]
#
# 要求:
# 1：页面显示 序号 + 商品名称 + 商品价格，如：
#       		1 电脑 1999
# 	   		2 鼠标 10
#      		…
# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 4：用户输入Q或者q，退出程序。

goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998}, ]

while 1:
    print('****商品具体展示：****')
    for index,i in enumerate(goods,1):
        print('{}\t{}\t{}'.format(index,i['name'],i['price']))
    print('*********************')
    choice_num = input('输入商品序号：').strip()
    if choice_num.isdigit():
        if 0 < int(choice_num) <= len(goods):
            print(goods[int(choice_num)-1]['name'])
        else:
            print('超出范围，重新选择...')
    else:
        print('请输入数字,请重新输入')
