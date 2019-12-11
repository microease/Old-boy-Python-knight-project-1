# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.file = open('file',mode = 'w')
#     def write(self):
#         self.file.write('sjahgkldhgl')
#     def __del__(self):    # 析构方法 ： 在删除这个类创建的对象的时候会先触发这个方法，再删除对象
#         # 做一些清理工作,比如说关闭文件，关闭网络的链接，数据库的链接
#         self.file.close()
#         print('执行del了')
#
# f = Foo('alex',20)
# print(f)
