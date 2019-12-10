# class Foo():
#     pass
#
# obj1 = Foo()
# obj2 = Foo()
# print(hash(obj1))  # 内存地址 97649779257
# print(hash(obj1))  # 内存地址 97649779257
# print(hash(obj1))  # 内存地址 97649779257
# print(hash(obj1))  # 内存地址 97649779257
# print(hash(obj1))  # 内存地址 97649779257
# print(hash(obj1))  # 内存地址 97649779257
# print(hash(obj1))  # 内存地址 97649779257
# print(hash(obj2))  # 97649779271

# 1.每次执行hash值都会变化
# 2.在一次执行的过程中对同一个值得hash结果总是不变的
# 字典为什么寻址快
# dic = {'name':'alex','age':83,'sex':'不详'}
# 字典在内存中是如何存储的？
# 为什么字典的key必须可hash

# hash算法
# 1.对于相同的值在一次程序的运行中是不会变化的
# 2.对于不同的值在一次程序的运行中总是不同的

# set的去重机制
# new_lst = [1,2,3,4,5,6,7,8,9,0,10,111,238579]
# lst = [2,2,43,53,238579,14780]
# for i in lst:
#     if i in new_lst:
#         pass
#     else:
#         new_lst.append(i)

# set = {1,2,'abc',3,4,5,6,7,8,9,'bca'}
# 不能通过逐个判断值相等这件事儿来做去重工作
# hash算法也不是完全的靠谱

# set 的去重机制
    # 1.对每一个元素进行hash计算出一个内存地址
    # 2.到这个内存地址上查看
        # 如果这块内存中没有值
            # 将这个元素存到对应的内存地址上
        # 如果这块内存中已经有值
            # 判断这两个值是否相等
                # 如果相等 就舍弃后面的值
                # 如果不相等 就二次寻址再找一个新的空间来存储这个值

# 员工类
# 姓名 年龄 性别 部门
# 转岗位
# 姓名 年龄变化了 性别 部门
# 100个员工，去掉重复的
# 员工的姓名 性别 是相同的，就认为是同一个员工

class Staff:
    def __init__(self,name,age,sex,dep):
        self.name = name
        self.age = age
        self.sex = sex
        self.dep = dep
    def __hash__(self):
        return hash(self.name + self.sex)
    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:
            return True

name_lst = ['yuan','egon','nazha','peiqi']
obj_lst = []
for i in range(100):
    name = name_lst[i%4]
    obj = Staff(name,i,'male','python')
    obj_lst.append(obj)
print(obj_lst)
ret = set(obj_lst)
print(ret)
for i in ret:
    print(i.name,i.age)




