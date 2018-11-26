# 定义两个功能函数
def send_shuoshuo():
    print('发说说')

def send_pic():
    print('发图片')

# 相关的逻辑代码
btn_index = 1
if btn_index == 1:
    send_shuoshuo()
elif btn_index == 2:
    send_pic()

# 发说说，发图片的前提：必须要登录验证

# 方案1：直接在业务逻辑里面修改，添加验证操作
# 缺点：复用性差、冗余度大、难以维护

# 方案2：直接在功能函数里面修改
# 优点：方便代码重用
# 缺点：功能函数多的话，仍然有冗余，复用性差，难以维护

# 方案3：单独写一个验证函数，在功能函数中调用
# 优点：可维护性高，代码重用
# 缺点：违背了开发封闭原则，也违背了单一职责原则

# 方案4：单独写一个验证函数，把功能函数传递进来
# 缺点：业务逻辑发生改变

# 方案5：使用闭包
print('-' * 30)

def check_login(func):
    def inner():
        print('登录验证成功！')
        func()
    return inner

send_shuoshuo = check_login(send_shuoshuo)
send_pic = check_login(send_pic)

btn_index = 1
if btn_index == 1:
    send_shuoshuo()
elif btn_index == 2:
    send_pic()

"""
------------------------------
登录验证成功！
发说说
"""

# 方案6：语法糖写法
print('-' * 30)

def check_login(func):
    def inner():
        print('登录验证成功！')
        func()
    return inner

@check_login
def send_shuoshuo():
    print('发说说')
# 等价于
# send_shuoshuo = check_login(send_shuoshuo)

@check_login
def send_pic():
    print('发图片')
# 等价于
# send_pic = check_login(send_pic)

btn_index = 1
if btn_index == 1:
    send_shuoshuo()
elif btn_index == 2:
    send_pic()
"""
------------------------------
登录验证成功！
发说说
"""
