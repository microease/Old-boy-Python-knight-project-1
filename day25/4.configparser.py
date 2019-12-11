# 配置文件
# 'userinfo'
    # 当你把你的userinfo copy到其他目录下
    # 如果你不是在当前这个userinfo文件所在的目录去执行py文件

# 绝对路径 D:\骑士计划PYTHON1期\day25\userinfo
    # 当你把你的整个程序包括userinfo文件 copy到另一台机器上

# 开发环境
# 测试环境
# 生产环境

# 把路径记录在文件里
# with open('config',encoding='utf-8') as f:
#     for line in f:
#         if line.startswith('userinfo'):
#             key,value = line.split('=')
#             print(value.strip())

# import configparser
#
# config = configparser.ConfigParser()
#
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                       'Compression': 'yes',
#                      'CompressionLevel': '9',
#                      'ForwardX11':'yes'
#                      }
#
# config['bitbucket.org'] = {'User':'hg'}
#
# config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}
#
# with open('example.ini', 'w') as configfile:
#    config.write(configfile)


import configparser

# config = configparser.ConfigParser()
# print(config.sections())        #  []
# config.read('example.ini')
# print(config.sections())        #   ['bitbucket.org', 'topsecret.server.com']
#
# print('bytebong.com' in config) # False
# print('bitbucket.org' in config) # True
# print(config['bitbucket.org']["user"])  # hg
# print(config['DEFAULT']['Compression']) #yes
# print(config['topsecret.server.com']['ForwardX11'])  #no
# print(config['bitbucket.org'])          #<Section: bitbucket.org>
# for key in config['bitbucket.org']:     # 注意,有default会默认default的键
#     print(key)
# print(config.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键
# print(config.items('bitbucket.org'))    #找到'bitbucket.org'下所有键值对
# print(config.get('bitbucket.org','compression')) # yes       get方法Section下的key对应的value
