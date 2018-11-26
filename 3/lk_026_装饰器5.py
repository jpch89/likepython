def dec(func):
    def inner(*args, **kwargs):
        print('-' * 30)
        func(*args, **kwargs)
    return inner

@dec
def pnum(num):
    print(num)

pnum(10)

@dec
def pnum2(num1, num2):
    print(num1, num2)

pnum2(1, 4)
"""
------------------------------
10
------------------------------
1 4
"""
