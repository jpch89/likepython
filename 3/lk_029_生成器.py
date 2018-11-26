# 这样获取迭代器并没有减少内存消耗
l = [i for i in range(10000000)]
it = iter(l)

g = (i for i in range(10000000) if i % 2 == 0)
print(g)
"""
<generator object <genexpr> at 0x0000019BF9EFA7D8>
"""

print(next(g))
print(next(g))
"""
0
2
"""

print(g.__next__())
"""
4
"""
