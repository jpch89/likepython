def test():
    for i in range(1, 9):
        yield i


g = test()
print(g)
"""
<generator object test at 0x000002027FDDA7D8>
"""

print(next(g))
"""
1
"""
print(g.__next__())
"""
2
"""
