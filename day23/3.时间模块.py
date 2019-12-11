import time

# 时间模块
# 三种格式
    # 时间戳时间 浮点数 秒为单位
        # 1970.1.1 0:0:0 英国伦敦时间
        # 1970.1.1 8:0:0 东8区
    # 结构化时间 元组
    # 格式化时间 str数据类型的
# print(time.time())
# 1536023489.3035157
# 1536023501.1504664

# struct_time = time.localtime()
# print(struct_time)

# fmt1 =time.strftime('%H:%M:%S')
# fmt2 =time.strftime('%Y-%m-%d')
# fmt3 =time.strftime('%y-%m-%d')
# fmt4 =time.strftime('%c')
# print(fmt1)
# print(fmt2)
# print(fmt3)
# print(fmt4)

# 2018年8月8日 格式化时间
# 时间戳时间 时间戳时间

# str_time = '2018-8-8'
# struct_time = time.strptime(str_time,'%Y-%m-%d')
# print(struct_time)
# timestamp = time.mktime(struct_time)
# print(timestamp)

# timestamp = 1500000000
# struct_time = time.localtime(timestamp)
# fmt_time = time.strftime('%Y-%m-%d %H:%M:%S',struct_time)
# print(fmt_time)

# 2000000000
# struct_time = time.localtime(2000000000)
# fmt_time = time.strftime('%Y-%m-%d %H:%M:%S',struct_time)
# print(fmt_time)

# 写函数，计算本月1号的时间戳时间
# 通过我拿到的这个时间，能迅速的知道我现在所在时间的年 月
# def get_timestamp():
#     fmt_time = time.strftime('%Y-%m-1')
#     struct = time.strptime(fmt_time,'%Y-%m-%d')
#     res = time.mktime(struct)
#     return res
# ret = get_timestamp()
# print(ret)



