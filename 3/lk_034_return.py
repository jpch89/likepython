def test():
    yield 1
    print('a')
    yield 2
    print('b')
    return '一则消息'


g = test()
print(next(g))
"""
1
"""

print(next(g))
"""
a
2
"""

# print(next(g))
"""
b
Traceback (most recent call last):
  File "lk_034_return.py", line 21, in <module>
    print(next(g))
StopIteration: 一则消息
"""

print('-' * 20)

def test():
    yield 1
    print('a')
    yield 2
    print('b')
    yield 3
    print('c')


g = test()
for i in g:
    print(i)
print('-' * 20)
for i in g:
    print(i)
"""
1
a
2
b
3
c
--------------------
"""
