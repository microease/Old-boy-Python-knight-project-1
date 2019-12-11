from multiprocessing import Manager
# 把所有实现了数据共享的比较便捷的类都重新又封装了一遍，并且在原有的multiprocessing基础上
# 增加了新的机制 list dict

# 数据共享的机制
    # 支持数据类型非常有限
    # list dict都不是数据安全的，你需要自己加锁来保证数据安全

from multiprocessing import Manager,Process,Lock
def work(d,lock):
    with lock:
        d['count']-=1

if __name__ == '__main__':
    lock=Lock()
    with Manager() as m:
        dic=m.dict({'count':100})
        p_l=[]
        for i in range(100):
            p=Process(target=work,args=(dic,lock))
            p_l.append(p)
            p.start()
        for p in p_l:
            p.join()
        print(dic)

# with ....
    # 一大段语句
# dis模块

# python的上下文管理
# 在执行一大段语句之前 自动做某个操作 open
# 在执行一大段语句之后 自动做某个操作 close

# 面向对象的魔术方法: __enter__\__exit__