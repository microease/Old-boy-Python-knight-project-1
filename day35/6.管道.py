# 队列是基于管道实现的
# 管道是基于socket实现的
# 队列 + 锁 简便的IPC机制 使得 进程之间数据安全
# 管道  进城之间数据不安全 且存取数据复杂
# socket + pickle

# from multiprocessing import Pipe
# left,right = Pipe()
# left.send(12345)
# print(right.recv())
import time
from multiprocessing import Pipe,Process

# def consumer(left,right):
#     time.sleep(1)
#     print(right.recv())
#
# if __name__ == '__main__':
#     left,right = Pipe()
#     Process(target=consumer,args=(left,right)).start()
#     left.send(1234)

# def consumer(left,right):
#     left.close()
#     while True:
#         try:
#             print(right.recv())
#         except EOFError:
#             break
#
# if __name__ == '__main__':
#     left,right = Pipe()
#     Process(target=consumer,args=(left,right)).start()
#     right.close()
#     for i in range(10):
#         left.send('泔水%s'%i)
#     left.close()

# pipe的端口管理不会随着某一个进程的关闭就关闭
# 操作系统来管理进程对这些端口的使用
# left,right
# left,right
# 操作系统管理4个端口  每关闭一个端口计数-1，直到所有的端口都关闭了，
# 剩余1个端口的时候 recv就会报错















