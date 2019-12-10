# class Staff:
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#     def __eq__(self, other):
#         return self.__dict__ == other.__dict__
# alex = Staff('alex','不详')
# alex2 = Staff('alex','不详')
# alex22 = Staff('alex2','female')
# print(alex == alex2)  # alex.__eq__(alex2)
# print(alex2 == alex22)

# l1 = [1,2,3,4]
# l2 = [1,2,3,4]
# print(id(l1),id(l2))
# print(l1 == l2)
# print(l1 is l2)