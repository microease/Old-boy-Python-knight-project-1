from multiprocessing import JoinableQueue
# JoinableQueue 类
# put
# get
    # task_done 通知队列已经有一个数据被处理了
# q.join() # 阻塞直到放入队列中所有的数据都被处理掉(有多少个数据就接收到了多少taskdone)

import time
import random
from multiprocessing import Process,JoinableQueue
def consumer(q,name):
    # 处理数据
    while True:
        food = q.get()
        time.sleep(random.uniform(0.5,1))
        print('%s吃了一个%s' % (name, food))
        q.task_done()

def producer(q,name,food):
    # 获取数据
    for i in range(10):
        time.sleep(random.uniform(0.3,0.8))
        print('%s生产了%s%s'%(name,food,i))
        q.put(food+str(i))

if __name__ == '__main__':
    jq = JoinableQueue()
    c1 = Process(target=consumer,args=(jq,'alex'))
    c2 = Process(target=consumer,args=(jq,'wusir'))
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()
    p1 = Process(target=producer,args=(jq,'杨宗河','泔水'))
    p2 = Process(target=producer,args=(jq,'何思浩','鱼刺和骨头'))
    p1.start()
    p2.start()
    p1.join()   # 生产者要先把所有的数据都放到队列中
    p2.join()
    jq.join()












