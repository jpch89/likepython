def test(a, b, c, d=1):
    print(a + b + c + d)

def test2(a, b, c, d=2):
    test(a, b, c, d)

test2(1, 2, 3)
"""
8
"""

from functools import partial
# c 偏爱 5
new_func = partial(test, c=5)
print(new_func, type(new_func))
"""
functools.partial(<function test at 0x0000018054D81E18>, c=5) <class 'functools.partial'>
"""

new_func(1, 2)
"""
9
"""
