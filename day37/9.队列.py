import queue

# 线程安全 队列 ： 排队相关的逻辑
# q = queue.Queue()
# q.put()
# q.get()
# q.put_nowait()
# q.get_nowait()

# qps 每秒钟接受的请求数
# 帮助你维持程序相应的顺序

# from queue import LifoQueue
# 栈 完成算法
# lq = LifoQueue()
# lq.put(1)
# lq.put(2)
# lq.put(3)
# lq.put('a')
# lq.put('b')
# print(lq.get())
# print(lq.get())
# print(lq.get())

# from queue import PriorityQueue
# pq = PriorityQueue()
# pq.put((15,'abc'))
# pq.put((5,'ghi'))
# pq.put((12,'def'))
# pq.put((12,'aaa'))
#
# print(pq.get())
# print(pq.get())
# print(pq.get())

# from queue import PriorityQueue
# pq = PriorityQueue()
# pq.put(15)
# pq.put(5)
# pq.put(12)
# pq.put(12)
#
# print(pq.get())
# print(pq.get())
# print(pq.get())

# from queue import PriorityQueue
# pq = PriorityQueue()
# pq.put('abc')
# pq.put('def')
#
# print(pq.get())
# print(pq.get())

