def check(func):
    print('装饰器 check 执行')
    def inner():
        print('登录验证操作...')
        func()
    return inner

@check
def send_message():
    print('发说说')

# 给发说说增加一些额外的功能：
# 1. 函数名字不能发生改变
# 2. 函数体内部的代码不能发生改变

# send_message = check(send_message)
send_message()
"""
装饰器 check 执行
登录验证操作...
发说说
"""

# 当我们写 @check 的时候，等同于
# send_message = check(send_message)
# 所以装饰器 check 已经被立即执行
