from gevent import monkey;monkey.patch_all()
# 导入其他模块 内部带有一些阻塞事件

# spawn(函数名)  产生了一个协程任务 在遇到IO操作的时候帮助我们在多任务之间自动切换
# join()         阻塞 直到某个任务被执行完毕
# join_all()
# value属性      获取返回值

# from gevent import monkey
# monkey.patch_all()
# import time
# import gevent
#
# def eat():
#     print('eating 1')
#     time.sleep(1)
#     print('eating 2')
#     return 'eat finished'
#
# def play():
#     print('playing 1')
#     time.sleep(1)
#     print('playing 2')
#     return 'play finished'
#
# g1 = gevent.spawn(eat)   #  自动的检测阻塞事件，遇见阻塞了就会进行切换，有些阻塞它不认识
# g2 = gevent.spawn(play)
# gevent.joinall([g1,g2])
# print(g1.value)
# print(g2.value)


# 爬虫
# from gevent import monkey;monkey.patch_all()
# import time
# import gevent
# import requests
# url_lst = [
#     'http://www.baidu.com',
#     'http://www.4399.com',
#     'http://www.7k7k.com',
#     'http://www.sogou.com',
#     'http://www.sohu.com',
#     'http://www.sina.com',
#     'http://www.jd.com',
#     'https://www.luffycity.com/home',
#     'https://www.douban.com',
#     'http://www.cnblogs.com/Eva-J/articles/8324673.html',
#     'http://www.baidu.com',
#     'http://www.4399.com',
#     'http://www.7k7k.com',
#     'http://www.sogou.com',
#     'http://www.sohu.com',
#     'http://www.sina.com',
#     'http://www.jd.com',
#     'https://www.luffycity.com/home',
#     'https://www.douban.com',
#     'http://www.cnblogs.com/Eva-J/articles/8324673.html',
#     'http://www.baidu.com',
#     'http://www.4399.com',
#     'http://www.7k7k.com',
#     'http://www.sogou.com',
#     'http://www.sohu.com',
#     'http://www.sina.com',
#     'http://www.jd.com',
#     'https://www.luffycity.com/home',
#     'https://www.douban.com',
#     'http://www.cnblogs.com/Eva-J/articles/8324673.html',
#     'http://www.baidu.com',
#     'http://www.4399.com',
#     'http://www.7k7k.com',
#     'http://www.sogou.com',
#     'http://www.sohu.com',
#     'http://www.sina.com',
#     'http://www.jd.com',
#     'https://www.luffycity.com/home',
#     'https://www.douban.com',
#     'http://www.cnblogs.com/Eva-J/articles/8324673.html',
# ]
#
#
# def get_url(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         print(url,len(response.text))
#
# start = time.time()        # 两个网页  0.01+0,01 = 0.02
# for url in url_lst:
#     get_url(url)
# print(time.time()-start)   # 7.075469017028809
#
# start = time.time()
# g_lst = []
# for url in url_lst:
#     g = gevent.spawn(get_url,url)
#     g_lst.append(g)
# gevent.joinall(g_lst)
# print(time.time()-start)   # 1.5963938236236572

# 协程 来实现并发的socket server













