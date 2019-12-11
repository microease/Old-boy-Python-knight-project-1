from threading import Timer
def func():
    print('执行我啦')

t = Timer(3600,func)
t.start()
print('主线程')

# 只起一个线程 ：做定时任务
# 1个小时  做一件事儿
# 1个小时  做两件事儿
# 1个小时  做三件事儿
# 1个小时  做四件事儿
# 1个小时  做五件事儿

# crontab linux操作系统上 做定时任务 工具
