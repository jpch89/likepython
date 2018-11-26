# 不定长参数
# 变长参数
# 可变长参数

def my_sum(*t):
    print(t, type(t))
    result = 0
    for v in t:
        print(v)
        result += v
    print(result)

my_sum(4, 5, 6, 7)
"""
(4, 5, 6, 7) <class 'tuple'>
4
5
6
7
22
"""
