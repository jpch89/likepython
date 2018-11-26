def test():
    a = 1
    print(a)
    print(locals())
    print(globals())

test()

# 迟绑定
a = 1

def test():
    print(a)
    print(b)

b = 2
test()
"""
1
2
"""
# 个人理解：
# 迟绑定就是调用时取值，而不是定义时取值。

c = 1

def test():
    print(c)
    print(d)

test()
d = 2
"""
1
Traceback (most recent call last):
  File "lk_036_变量.py", line 31, in <module>
    test()
  File "lk_036_变量.py", line 29, in test
    print(d)
NameError: name 'd' is not defined
"""
