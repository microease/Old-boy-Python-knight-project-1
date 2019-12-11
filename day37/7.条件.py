# notify 控制流量 通知有多少人可以通过了
# wait 在门口等待的所有人

# acquire
# wait 使用前后都需要加锁
# 做的事情
# release

# acquire
# notify 使用前后都需要加锁
# release

from threading import Condition,Thread
def func(con,index):
    print('%s在等待'%index)
    con.acquire()
    con.wait()
    print('%s do something'%index)
    con.release()

con = Condition()
for i in range(10):
    t = Thread(target=func,args=(con,i))
    t.start()
con.acquire()
con.notify_all()
con.release()
# count = 10
# while count > 0:
#     num= int(input('>>>'))
#     con.acquire()
#     con.notify(num)
#     count -= num
#     con.release()

