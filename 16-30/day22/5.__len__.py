# len()  lst dict set str
# print('__len__' in dir(list))
# print('__len__' in dir(dict))
# print('__len__' in dir(set))
# print('__len__' in dir(tuple))
# print('__len__' in dir(str))
#
# print('__len__' in dir(int))
# print('__len__' in dir(float))

# class Foo:
#     def __len__(self):
#         return 1
# obj = Foo()
# print(len(obj))

# class Class:
#     def __init__(self,name,course):
#         self.name = name
#         self.course = course
#         self.students = []
#     def __len__(self):
#         return len(self.students)
# s1 = Class('骑士1班','python')
# s1.students.append('wuyi')
# s1.students.append('yangyi')
# s1.students.append('wangfan')
# print(len(s1))