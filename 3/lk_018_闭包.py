def test():
    a = 2
    def test2():
        print(a)
    return test2

new_func = test()
new_func()
"""
2
"""
