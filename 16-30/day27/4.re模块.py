# re
import re
# findall
# ret = re.findall('\d+','SGY93SHD2183Y0')
# print(ret)
# 参数 正则表达式 待匹配的字符串
# 返回值 是一个列表 所有匹配到的项

# search
# ret = re.search('\d+','SGY93SHD2183Y0')
# print(ret)
# print(ret.group())

# ret = re.search('\d+','SGahsf')
# print(ret)
# if ret:
#     print(ret.group())
# search
# 返回值 ： 返回一个SRE_Match对象
#           通过group去取值
#           且只包含第一个匹配到的值

# 需求：
# 有一个字符串'2*3/4*5'，需要我们不用eval，自己计算出这个表达式的结果
# 这个表达式只含有乘除法
# ret = re.search('\d[*/][\d]','2*3/4*5')
# print(ret.group())
# 计算2*3
# 6 替换2*3
# 6/4*5
# 6/4 = 1.5
# 1.5替换6/4
# 1.5*5 = 7.5

# ret = re.search('\d(\.\d)?[*/]\d','1.5*5')
# print(ret.group())
#
# ret = re.findall('\d(\.\d)?[*/]\d','1.5*5')
# print(ret)

# findall 有一个特点，会优先显示分组中的内容
# ret = re.findall('(www)\.(baidu|oldboy)\.(com)','www.baidu.com')
# print(ret)
# 'www\.(baidu|oldboy)\.com','www.baidu.com'
# 'www\.(baidu)\.com','www.baidu.com'
# baidu

# ret = re.search('(www)\.(baidu|oldboy)\.(com)', 'www.baidu.com')
# # print(ret.group(0))
# # print(ret.group(1))
# # print(ret.group(2))
# # print(ret.group(3))


# ret=re.findall(r"\d+\.\d+|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)
# ret.remove('')
# print(ret)