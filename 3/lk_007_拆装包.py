def my_sum(a, b, c, d):
    print(a + b + c + d)

def test(*args):
    print(args)
    # 拆包
    print(*args)
    my_sum(*args)

test(1, 2, 3, 4)
"""
(1, 2, 3, 4)
1 2 3 4
10
"""

def func(a, b):
    print(a)
    print(b)


def test2(**kwargs):
    print(kwargs)
    # 拆包
    func(**kwargs)

# 注意关键字参数的名字一定要对应
# test2(a=1, c=2) 会报错！
test2(a=1, b=2)
"""
{'a': 1, 'b': 2}
1
2
"""

