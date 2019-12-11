from multiprocessing import Queue
# import queue
# 先进先出
q = Queue(2)
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())

# q.get()
# try:
#     print(q.get_nowait())
# except queue.Empty:
#     print('empty')

# q.put_nowait(3)

# put()
# get()
# get_nowait()
# put_nowait()
# print(q.empty())
# print(q.full())

from multiprocessing import Process,Queue

def consume(q):
    print('son-->',q.get())
    q.put('abc')

if __name__ == '__main__':
    q = Queue()
    p = Process(target=consume,args=(q,))
    p.start()
    q.put({'123':123})
    p.join()
    print('Foo-->',q.get())












