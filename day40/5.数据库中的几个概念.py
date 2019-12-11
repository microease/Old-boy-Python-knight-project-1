# 记录、数据 data
# id,name,passwd,age,number
# 1,alex,alex3714,83,13838384438   # 一条记录

# 表 table
# userinfo    # 一张表就是一个文件
# 1,alex,alex3714,83,13838384438
# 1,alex,alex3714,83,13838384438
# 1,alex,alex3714,83,13838384438

# 库 base
# 选课系统     userinfo/studentinfo/courseinfo
# 员工信息表   userinfo
# ftp          userinfo
# mysql这个软件来管理数据
# 只有一个mysql来管理你的程序，
# 你的程序之间的数据应该是隔离的
# 创建两个文件夹 ：选课系统、员工信息表
# 所谓数据库中的库 就是文件夹
    # 一般情况下 每个程序使用一个库

# 数据库管理系统 dbms
# database management system
# 能够通过一个软件来管理文件、文件夹、数据

# 数据库服务器
# 你把你的数据装在哪台机器上 这台机器就是数据库服务器

# 关系型数据库和非关系型数据库
# 关系型
    # 一条数据包含了一个事物的多条信息，这些信息之间是有关联性的
# 非关系型  :存取频繁的，并且要求效率高的，不突出数据之间关联的
    # k-v
    # id content

# 关系型数据库
    # mysql       开源
    # oracle      企业级
    # sqlite      轻量级
    # sql server  大学
# 非关系型数据库  ：消息转发
    # memcache
    # redis
    # MongoDB
    # nosql
