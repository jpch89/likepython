def change(num):
    print('id为：', id(num))
    print(num)

b = 10
print('id为：', id(b))
change(b)
"""
id为： 1984064832
id为： 1984064832
10
"""

def change(num):
    print('num重新赋值之前的id为：', id(num))
    num = 666
    print('num的id为：', id(num))
    print('num的值为：', num)

b = 10
change(b)
print('b的id为：', id(b))
print('b的值为：', b)
"""
num重新赋值之前的id为： 1984064832
num的id为： 1516629632112
num的值为： 666
b的id为： 1984064832
b的值为： 10
"""

def change(num):
    print('改变num之前的id为：', id(num))
    num.append(666)
    print('改变num之后的id为：', id(num))
    print('num的值为：', num)

b = [1, 2, 3]
change(b)
print('b的id为：', id(b))
print('b的值为：', b)
"""
改变num之前的id为： 2437526194376
改变num之后的id为： 2437526194376
num的值为： [1, 2, 3, 666]
b的id为： 2437526194376
b的值为： [1, 2, 3, 666]
"""
