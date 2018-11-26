# 生成器的创建方式
def test():
    print('生成器开始')
    yield 1
    print('a')

    yield 2
    print('b')


g = test()
print(g)
"""
<generator object test at 0x0000022D30B9A7D8>
"""

# 带有 yield 语句的函数叫做生成器函数
# 调用生成器函数，返回一个生成器

print(next(g))
"""
生成器开始
1
"""
print(next(g))
"""
a
2
"""
print(next(g))
"""
b
Traceback (most recent call last):
  File "lk_030_生成器3.py", line 30, in <module>
    print(next(g))
StopIteration
"""
