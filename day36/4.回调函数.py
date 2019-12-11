import os
from multiprocessing import Pool
# def func(i):
#     print('第一个任务',os.getpid())
#     return '*'*i,123
#
# def call_back(res):
#     print('回调函数 ：',os.getpid())
#     print('res -->',res)
#
# if __name__ == '__main__':
#     p = Pool()
#     print('主进程 ： ',os.getpid())
#     p.apply_async(func,args=(1,),callback=call_back)
#     p.close()
#     p.join()

# 当func执行完毕之后执行callback函数
# func的返回值会作为callback的参数
# 回调函数是哪个进程实现的？？？
    # 主进程

# 子进程有大量的计算要去做，回调函数等待结果做简单处理

# 子进程去访问网页，主进程处理网页的结果
# url_lst = [
#     'http://www.baidu.com',
#     'http://www.sohu.com',
#     'http://www.sogou.com',
#     'http://www.4399.com',
#     'http://www.cnblogs.com',
# ]
# import re
# from urllib.request import urlopen
# from multiprocessing import Pool
#
# def get_url(url):
#     response = urlopen(url)
#     ret = re.search('www\.(.*?)\.com',url)
#     print('%s finished'%ret.group(1))
#     return  ret.group(1),response.read()
#
# def call(content):
#     url,con = content
#     with open(url+'.html','wb') as f:
#         f.write(con)
#
# if __name__ == '__main__':
#     p = Pool()
#     for url in url_lst:
#         p.apply_async(get_url,args=(url,),callback=call)
#     p.close()
#     p.join()


# url_lst = [
#     'http://www.baidu.com',
#     'http://www.sohu.com',
#     'http://www.sogou.com',
#     'http://www.4399.com',
#     'http://www.cnblogs.com',
# ]
# import re
# from urllib.request import urlopen
# from multiprocessing import Pool
#
# def get_url(url):
#     response = urlopen(url)
#     ret = re.search('www\.(.*?)\.com',url)
#     print('%s finished'%ret.group(1))
#     return  ret.group(1),response.read()
#
# def call(content):
#     url,con = content
#     with open(url+'.html','wb') as f:
#         f.write(con)
#
# if __name__ == '__main__':
#     p = Pool()
#     ret_l = []
#     for url in url_lst:
#         ret = p.apply_async(get_url,args=(url,))
#         ret_l.append(ret)
#     for ret in ret_l:
#         call(ret.get())

# ret = apply_async
# ret.get()

# 1.代码简洁度不同
# 2.效率问题






