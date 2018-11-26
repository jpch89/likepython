def test():
    a = 1
    def test2():
        print(a)
    a = 2
    return test2

new_func = test()
new_func()
"""
2
"""

# 并不会报错
# 因为 b 不是在定义的时候设置值的
def test():
    print(b)
print('说点什么')
"""
说点什么
"""
# 在调用函数的时候，才会去查找变量对应的值具体是什么
# test()
"""
NameError: name 'b' is not defined
"""

def test():
    funcs = []
    for i in range(1, 4):
        def test2():
            print(i)
        funcs.append(test2)
    return funcs

newfuncs = test()
print(newfuncs)

newfuncs[0]()
newfuncs[1]()
newfuncs[2]()
"""
[<function test.<locals>.test2 at 0x000001A6C95360D0>, <function test.<locals>.test2 at 0x000001A6C95361E0>, <function test.<locals>.test2 at 0x000001A6C9536268>]
3
3
3
"""

# 解决方案
def test():
    funcs = []
    for i in range(1, 4):
        def test2(num):
            def inner():
                print(num)
            return inner
        funcs.append(test2(i))
    return funcs

newfuncs = test()
print(newfuncs)

newfuncs[0]()
newfuncs[1]()
newfuncs[2]()
"""
[<function test.<locals>.test2.<locals>.inner at 0x0000021F79EA6378>, <function test.<locals>.test2.<locals>.inner at 0x0000021F79CD1E18>, <function test.<locals>.test2.<locals>.inner at 0x0000021F79EA6400>]
1
2
3
"""
