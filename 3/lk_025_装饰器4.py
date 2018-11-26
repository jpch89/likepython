# 装饰器的叠加

def decorator_line(func):
    def inner():
        print('-' * 30)
        func()
    return inner

def decorator_star(func):
    def inner():
        print('*' * 30)
        func()
    return inner

@decorator_line
@decorator_star
def print_content():
    print('大家好，我是警察')

print_content()
"""
------------------------------
******************************
大家好，我是警察
"""

