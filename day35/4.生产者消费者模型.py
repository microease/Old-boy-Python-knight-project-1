# 5000个网页
# 爬取这5000个网页
# 把网页中所有的url链接拿到

# 获取网页 、 从网页的内容中提取链接
# 网速慢、网页的服务器响应慢
import time
import random
from multiprocessing import Process,Queue
def consumer(q,name):
    # 处理数据
    while True:
        food = q.get()
        if food is None:break
        time.sleep(random.uniform(0.5,1))
        print('%s吃了一个%s' % (name, food))

def producer(q,name,food):
    # 获取数据
    for i in range(10):
        time.sleep(random.uniform(0.3,0.8))
        print('%s生产了%s%s'%(name,food,i))
        q.put(food+str(i))

if __name__ == '__main__':
    q = Queue()
    c1 = Process(target=consumer,args=(q,'alex'))
    c2 = Process(target=consumer,args=(q,'wusir'))
    c1.start()
    c2.start()
    p1 = Process(target=producer, args=(q, '杨宗河','泔水'))
    p2 = Process(target=producer, args=(q, '何思浩','鱼刺和骨头'))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    q.put(None)   # 有几个consumer就需要放几个None
    q.put(None)












