def line_config(content, length):
    left = length // 2
    right = length - left
    def line():
        print('-' * left + content + '-' * right)
    return line

line1 = line_config('闭包', 30)
line1()
line2 = line_config('xxx', 20)
line2()
"""
---------------闭包---------------
----------xxx----------
"""
