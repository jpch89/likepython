# 返回函数
def get_func(flag):
    # 1. 再定义几个函数
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    # 2. 根据不同的 flag，返回不同的函数
    if flag == '+':
        return add
    elif flag == '-':
        return sub

result = get_func('+')
print(result, type(result))
"""
<function get_func.<locals>.add at 0x0000024D98AAFB70> <class 'function'>
"""

res = result(1, 7)
print(res)
"""
8
"""
