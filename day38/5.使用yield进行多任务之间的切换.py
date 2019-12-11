# def my_generator():
#     for i in range(10):
#         yield i   # 保存当前程序的状态
#
# for num in my_generator():
#     print(num)

# def consumer():
#     g = producer()
#     for num in g:
#         print(num)
#
# def producer():
#     for i in range(1000):
#         yield i
#
# consumer()

# 更好的利用协程
# 一个线程的执行明确的切分开
# 两个人物 帮助你记住哪个任务执行到哪个位置上了，并且实现安全的切换
# 一个任务不得不陷入阻塞了，在这个任务阻塞的过程中切换到另一个任务继续执行
# 你的程序只要还有任务需要执行 你的当前线程永远不会阻塞
# 利用协程在多个任务陷入阻塞的时候进行切换来保证一个线程在处理多个任务的时候总是忙碌的
# 能够更加充分的利用CPU，抢占更多的时间片
# 无论是进程、还是线程都是由操作系统来切换的，开启过多的线程、进程会给操作系统的调度增加负担
# 如果我们是使用协程，协程在程序之间的切换操作系统感知不到，无论开启多少个协程对操作系统来说总是一个线程
# 操作系统的调度不会有任何压力

# 协程的本质就是一条线程，所以完全不会产生数据安全的问题


# 一个人
# 做饭 2个小时     米饭交给电饭煲在煮  --wait-> 米饭
# 洗衣服 1.5小时   5分钟的时间把衣服放洗衣机 --> 晾衣服   wait
# 收拾屋子 4个小时 收拾
# 洗碗  半个小时   洗碗机

# 爬虫
    # 大量的网页
    # 1个线程  访问5000个url
    # 5000个线程  urlopen
    # 一个线程 发起请求的时候

# 协程模块
    # greenlet  gevent的底层，协程，切换的模块
    # gevent    直接用的，gevent能提供更全面的功能
# import time
# from greenlet import greenlet
# def eat():
#     print('eating 1')
#     g2.switch()
#     time.sleep(1)
#     print('eating 2')
#
# def play():
#     print('playing 1')
#     time.sleep(1)
#     print('playing 2')
#     g1.switch()
#
# g1 = greenlet(eat)
# g2 = greenlet(play)
# g1.switch()

# import time
# import gevent
#
# def eat():
#     print('eating 1')
#     time.sleep(1)
#     print('eating 2')
#
# def play():
#     print('playing 1')
#     time.sleep(1)
#     print('playing 2')
#
# g1 = gevent.spawn(eat)   #  自动的检测阻塞事件，遇见阻塞了就会进行切换，有些阻塞它不认识
# g2 = gevent.spawn(play)
# g1.join()    # 阻塞直到g1结束
# g2.join()    # 阻塞直到g2结束

import time
# import gevent
#
# def eat():
#     print('eating 1')
#     gevent.sleep(1)
#     print('eating 2')
#
# def play():
#     print('playing 1')
#     gevent.sleep(1)
#     print('playing 2')
#
# g1 = gevent.spawn(eat)   #  自动的检测阻塞事件，遇见阻塞了就会进行切换，有些阻塞它不认识
# g2 = gevent.spawn(play)
# g1.join()    # 阻塞直到g1结束
# g2.join()    # 阻塞直到g2结束

from gevent import monkey
monkey.patch_all()
import time
import gevent

def eat():
    print('eating 1')
    time.sleep(1)
    print('eating 2')

def play():
    print('playing 1')
    time.sleep(1)
    print('playing 2')

g1 = gevent.spawn(eat)   #  自动的检测阻塞事件，遇见阻塞了就会进行切换，有些阻塞它不认识
g2 = gevent.spawn(play)
g1.join()    # 阻塞直到g1结束
g2.join()    # 阻塞直到g2结束




