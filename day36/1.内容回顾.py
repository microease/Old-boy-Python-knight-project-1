# EOFError 子进程里用了input
# 同步 和 异步
    # 异步 并行
    # 异步 值得就是程序能够同时做多件事情
    # 同步控制 ：
        # 加锁
        # 修改购票文件的时候就变成一个一个改  微观上同步了
        # 宏观上 仍然是异步的
# 生产者消费者模型
    # 最后的put(None)不能放在生产者进程中

# 内容回顾
    # 进城之间通信 IPC
        # 队列 ：数据安全、先进先出、基于管道+锁实现的
            # 生产者消费者模型
            # JoinableQueue
        # 管道 ：
            # Pipe ：socket pickle
            # 管道是队列的底层，并且数据不安全
    # 池 Pool multiprocessing起进程池
        # 不能传队列作为子进程的参数，只能传管道
        # 进程池中开启的个数 ：默认是cpu的个数
        # 提交任务
            # apply 同步提交
                # 直接返回结果
            # apply_async 异步提交
                # 不会直接返回一个结果 而是返回一个对象
                # 后期通过对象get()获取返回值
                # p.close()
                # p.join()
            # map
                # 简化了apply_async的操作
                # 直接拿到返回值的可迭代对象
                # 循环就可以获取返回值
# 返回值 回调函数
# 使用进程池在多个进程之间通信
    # 第三方工具 ：数据安全、redis、kafka、memcache

# from multiprocessing import Pool,Queue,Pipe
# def func(q):
#     print(q)
#
# if __name__ == '__main__':
#     p = Pool()
#     q =Pipe()
#     p.apply(func,args=(q,))
#     p.close()
#     p.join()

# import time
# from multiprocessing import Pool,Queue,Pipe
# def func(q):
#     print(q)
#     time.sleep(1)
#     return q
#
# if __name__ == '__main__':
#     p = Pool()
#     ret = p.map(func,range(20))
#     for i in ret:
#         print('--> ',i)

