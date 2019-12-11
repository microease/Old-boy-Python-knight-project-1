import random
# 取随机小数 *
# print(random.random())   #(0,1)
# print(random.uniform(2,3))  #(n,m)

# 取随机整数   ****
# print(random.randint(1,2))  # [1,2]
# print(random.randrange(1,2))  # [1,2)
# print(random.randrange(1,100,2))

# 从一个列表中随机抽取 ****
# lst = [1,2,3,4,5,('a','b'),'cc','dd']
# ret = random.choice(lst)
# print(ret)
# ret = random.choice(range(100))
# print(ret)
#
# ret = random.sample(lst,3)
# print(ret)

# 乱序 ***
# lst = [1,2,3,4,5,('a','b'),'cc','dd']
# random.shuffle(lst)
# print(lst)


# 验证码
# 6位数字验证码
# random.randint(100000,999999)
# random.sample(range(10),6)
# def get_code(n=6):
#     code = ''
#     for i in range(n):
#         num = random.randint(0,9)
#         code += str(num)
#     return code
# ret1 = get_code()
# ret2 = get_code(4)
# print(ret1,ret2)

# 请你生成一个6位验证码（数字 和 字母）
# 字母怎么生成 chr(65)  'A'
# print(chr(65))
    # 生成一个随机字母
# 65-90 A-Z
# num = random.randint(65,90)
# print(chr(num))
# 97-122 a-z
# num = random.randint(97,122)
# print(chr(num))

# 每一位上出现的内容既可以是数字 也可以是字母
# 随机生成一个数字 一个大写字母 一个小写字母
# def get_code(n):
#     code = ''
#     for i in range(n):
#         num = str(random.randint(0,9))
#         alpha_upper = chr(random.randint(65, 90))
#         alpha_lower = chr(random.randint(97, 122))
#         c = random.choice([num,alpha_upper,alpha_lower])
#         code += c
#     return code
# ret = get_code()
# print(ret)

# 验证码
# def get_code(n = 6,alph_flag = True):
#     code = ''
#     for i in range(n):
#         c = str(random.randint(0,9))
#         if alph_flag:
#             alpha_upper = chr(random.randint(65, 90))
#             alpha_lower = chr(random.randint(97, 122))
#             c = random.choice([c,alpha_upper,alpha_lower])
#         code += c
#     return code
# ret = get_code()
# print(ret)


