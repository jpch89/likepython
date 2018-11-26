def test():
    num = 10
    def test2():
        num = 666
        print(num)
    print(num)
    test2()
    print(num)
    return test2

result = test()
"""
10
666
10
"""

def test():
    num = 10
    def test2():
        nonlocal num
        num = 666
        print(num)
    print(num)
    test2()
    print(num)
    return test2

result = test()
"""
10
666
666
"""
