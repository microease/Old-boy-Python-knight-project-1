__all__ = ['name','read1']
name = 'alexsb'

def read1():
    print('in read1')

def read2():
    print('in read2',name)

print('in mymodule')
if __name__ == '__main__':
    print('in mymodule')
    print('__name__ : ',__name__)
    # 函数的调用
