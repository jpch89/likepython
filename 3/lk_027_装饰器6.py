def dec(func):
    def inner(*args, **kwargs):
        print('-' * 30)
        result = func(*args, **kwargs)
        return result
    return inner

@dec
def add(num1, num2):
    return num1 + num2

print(add(1, 2))
"""
------------------------------
3
"""

# 注意：
# inner 样式要与被装饰函数保持一致
# 被装饰函数有参数 -- inner 要带参数
# 被装饰函数有返回值 -- inner 要有返回值

