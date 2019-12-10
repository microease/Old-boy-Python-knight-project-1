from conf.settings import userinfo
def login():
    name = input('username : ')
    pawd = input('password : ')
    with open(userinfo,encoding='utf-8') as f:
        for line in f:
            usr,pwd,identify = line.strip().split('|')
            if usr == name and pawd == pwd:
                return {'result':True,'name':name,'id':identify}
        else:
            return {'result':False,'name':name}