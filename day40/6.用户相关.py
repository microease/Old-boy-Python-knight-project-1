# 启动server端  - 可以在service服务中操作
    # >net start mysql

# 使用默认用户启动mysql客户端，默认的用户登录 是没有权限查看所有库的
    # >mysql 表示启动mysql 客户端
    # mysql> select user();  # 查看当前登录的用户
        # liqinyang@192.168.16.53 # 用户名@ip地址

    # mysql> show databases; # 查看所有的库
    # mysql> exit  # 退出当前的客户端

# 指定用户登录 root用户 mysql当中权限最高的 管理员用户
# 用户名root登录
    # > mysql -uroot -p
    # 初始化没有密码的时候 直接按回车键进入数据库
    # mysql> select user();

# 在输入sql语句的过程中 如果想要放弃本条语句 \c

# 设置密码
    # mysql> set password = password('123');

# 创建用户 create user
    # create user 'alex'@'192.168.16.*' identified by '123';
    # create user 'eva'@'%' identified by '123';
    # > mysql -ueva -p123 -h 192.168.16.39  远程登录一个mysql服务
    # 新创建出来的用户eva没有使用数据库的权限

# 给新用户授权 grant
    # grant 操作(select/all) on '库.表' to '用户'@'ip地址'
    # grant select on '*.*' to 'eva'@'%'

# 创建用户并授权 grant
    # mysql> grant all on *.* to 'eva'@'%' identified by '123

# 让公司的DBA给你创建用户并且授权
    # 用户名 要哪个库的哪些权限




