def test():
    print('生成器启动')
    res1 = yield 1
    print(res1)

    res2 = yield 2
    print(res2)

    res3 = yield 3
    print(res3)


g = test()
print(g.__next__())
"""
生成器启动
1
"""

print(next(g))
"""
None
2
"""

print(g.send('略略略'))
"""
略略略
3
"""

g = test()
# g.send('会报错')
"""
Traceback (most recent call last):
  File "lk_032_send.py", line 33, in <module>
    g.send('会报错')
TypeError: can't send non-None value to a just-started generator
"""

g.send(None)  # 等价于 g.next()
"""
生成器启动
"""
