import re
# 从一个字符串中获取要匹配的内容
# findall ****半
# 列表

# search  *****  验证用户输入内容 '^正则规则$'
# ret = re.search('^\d+','293ahs293djjk293sahf2938u')
# print(ret)

# match  验证用户输入内容
# ret = re.match('\d+','293ahs293djjk293sahf2938u')
# print(ret)
# print(ret.group())

# 切割split
# s1 = 'alex||egon|boss_jin'
# print(s1.split('|'))

# s = 'alex8123egon1120boss_jin'
# ret = re.split('\d+',s)
# print(ret)
# ret = re.split('(\d+)',s)  # (\d)+ \d\d\d\d\d...(\d)
# print(ret)
# ret = re.split('\d(\d)',s)
# print(ret)

# 替换sub
# s = 'alex|egon|boss_jin'
# print(s.replace('|','-'))
# s1 = 'alex8123egon1120boss_jin626356'
# ret = re.sub('\d+','|',s1)
# print(ret)
# ret = re.sub('\d+','|',s1,1)
# print(ret)
# ret = re.subn('\d+','|',s1)
# print(ret)

# compile ****半 编译正则规则
# com = re.compile('\d+')
# print(com)
# ret = com.search('abc1cde2fgh3skhfk')
# print(ret.group())
# ret = com.findall('abc1cde2fgh3skhfk')
# print(ret)
# ret = com.finditer('abc1cde2fgh3skhfk')
# for i in ret:
#     print(i.group())

# finditer ****半 节省空间的方法
# ret = re.finditer('\d+','abc1cde2fgh3skhfk')
# print(ret)
# for i in ret:
#     print(i.group())

# findall search
# compile finditer

# 分组命名、分组约束
# 前端
# <h1>函数</h1>
# <h2>初识函数</h2>
# 花花绿绿的样式
# 实际上对于前端语言来说 都是把不同样式的字体放在不同的标签中
# 标签语言

# <h1>函数</h1>
# <a>函数</a>
# <(.*?)>.*?</(.*?)>
#
# pattern = '<(?P<tag>.*?)>.*?</(?P=tag)>'
# ret = re.search(pattern,'<h1>函数</h1>')
# print(ret)
# if ret:
#     print(ret.group())
#     print(ret.group(1))
#     print(ret.group('tag'))


# pattern = r'<(.*?)>.*?</\1>'
# ret = re.search(pattern,'<a>函数</a>')
# print(ret)
# if ret:
#     print(ret.group())
#     print(ret.group(1))

# (?:正则表达式) 表示取消优先显示功能
# (?P<组名>正则表达式) 表示给这个组起一个名字
    # (?P=组名) 表示引用之前组的名字，引用部分匹配到的内容必须和之前那个组中的内容一模一样










