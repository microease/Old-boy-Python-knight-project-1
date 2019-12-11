from urllib.request import urlopen

ret = urlopen('https://movie.douban.com/top250?start=225&filter=')
content = ret.read().decode('utf-8')
print(type(content))