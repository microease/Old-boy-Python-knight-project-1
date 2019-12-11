# 异常处理
# 语法错误 :在程序之前就规避掉，不应该留到程序中来进行异常处理
    # 编译、执行
    # 编译的过程中报错
    # if name == 1:
    #     pass
# 异常
    # 在编译阶段没问题，在执行阶段才报错
# num = int(input('>>>'))
# print(num)

# 异常出现之后的现象 ：程序就不继续执行了

# 如何来查看异常？
# def func(c,d):
#     import re
#     print(re.search(c,d))
# def main(a,b):
#     func(a,b)
# main(1,2)

# 哪些错误
# l = []
# l[3]  # IndexError
# import Index  # ModuleNotFoundError
# open('aaaaaa') # FileNotFoundError
# 1/0 # ZeroDivisionError
# dic = {}
# dic['k']  # KeyError

# 多分支
# l = ['登陆','注册']
# try:
#     num = int(input('num : '))
#     print(l[num - 1])
# except ValueError:
#     print('输入了错误的内容')
# except IndexError:
#     print('您输入的内容不在范围内')
#
# print('其他内容')

# l = ['登陆','注册']
# try:
#     num = int(input('num : '))
#     print(l[num - 1])
# except (ValueError,IndexError):
#     print('输入了错误的内容')
#
# print('其他内容')

# 即便是放在try语句中的内容，在遇到报错之后也会中断这段语句的执行

# 万能异常
# try:
#     # l = []
#     # l[3]  # IndexError
#     # import Index  # ModuleNotFoundError
#     open('aaaaaa') # FileNotFoundError
#     1/0 # ZeroDivisionError
#     dic = {}
#     dic['k']  # KeyError
# except Exception:
#     print('异常啦')

# as语法
# try:
#     # l = []
#     # l[3]  # IndexError
#     # import Index  # ModuleNotFoundError
#     open('aaaaaa') # FileNotFoundError
#     1/0 # ZeroDivisionError
#     dic = {}
#     dic['k']  # KeyError
# except Exception as e:
#     print(e)

# 多分支 + 万能异常
# l = ['登陆','注册']
# try:
#     num = int(input('num : '))
#     print(l[num - 1])
# except (ValueError,IndexError):
#     print('输入了错误的内容')
# except Exception as e:
#     print(e)
#
# print('其他内容')

# try:
#     可能发生异常的代码
#     三行
# except 错误类型:
#     处理的代码

# try:
#     可能发生异常的代码
#     三行
# except 错误类型1:
#     处理的代码1
# except 错误类型2:
#     处理的代码2

# try:
#     可能发生异常的代码
#     三行
# except (错误类型1,错误类型2):
#     处理的代码

# try:
#     可能发生异常的代码
#     三行
# except (错误类型1,错误类型2):
#     处理的代码
# except Exception as e:
#     print(e)

# 异常处理中的其他机制
# else
# try:
#      pass
#     # 发邮件的逻辑
# except ValueError:
#     print('触发了一个name error')
# else:
#     pass
    # 汇报这段代码顺利的执行了 ： 发短信通知，记录到文件中

# finally
# try:
#     name = 123
# except NameError:
#     print(1111111)
# finally:
#     print('执行我啦')

# def func():
#     try:
#         f = open('content')
#         return f.read()
#     finally:
#         f.close()
#         print('closed')
#
# func()


# try:
#     f = open('content')
#     name
# finally:
#     f.close()
#     print('closed')

# finally 无论如何都要执行
# 收尾工作，打开了一个文件，占用了一个网络资源，打开了一个和数据库的链接


# try:
# except 错误类型:
# except 错误类型:
# except Exception:
# else:
# finally:

# try/except
# try/except/else
# try/finally
# try/ except / finally
# try/ except / else / finally

# raise NameError("name 'name' is not defined")
# raise NameError

# 自定义异常
# class EvaException(BaseException):
#     def __init__(self,msg):
#         super().__init__()
#         self.msg = msg
#     def __str__(self):
#         return self.msg
#
# raise EvaException('eva的异常')

# assert 1 == 1
# print('*'*100)
# assert 1 == 2
# print('*'*100)