# 带参装饰器

def dec_line(func):
    def inner():
        print('-' * 30)
        func()
    return inner

def dec_equal(func):
    def inner():
        print('=' * 30)
        func()
    return inner

def dec_start(func):
    def inner():
        print('*' * 30)
        func()
    return inner

@dec_line
def func():
    print('666')

func()

# 分析：
# 每个装饰器代码结构差不多
# 可以给装饰器传入一个字符参数
# 让它根据字符参数打印不同的分隔线

# 给一个参数 char
# 返回一个新的装饰器

print('-' * 30)

def get_dec(char):
    def dec_char(func):
        def inner():
            print(char * 10)
            func()
        return inner
    return dec_char

@get_dec('呵')
def func():
    print('说点什么')

func()

"""
------------------------------
呵呵呵呵呵呵呵呵呵呵
说点什么
"""
