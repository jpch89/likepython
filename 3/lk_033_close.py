def test():
    yield 1
    print('a')

    yield 2
    print('b')

    yield 3
    print('c')


g = test()

# 可以使用 next 函数、send 函数
# 可以调用 __next__ 方法、可以用 for in 遍历
print(g.__next__())
print(g.__next__())
print(g.__next__())
"""
1
a
2
b
3
"""

# print(g.__next__())  # 会报错
"""
c
Traceback (most recent call last):
  File "lk_033_close.py", line 27, in <module>
    print(g.__next__())  # 会报错
StopIteration
"""

# 使用 close 提前关闭生成器
g = test()
print(next(g))
"""
1
"""
g.close()
print(next(g))
"""
Traceback (most recent call last):
  File "lk_033_close.py", line 43, in <module>
    print(next(g))
StopIteration
"""
