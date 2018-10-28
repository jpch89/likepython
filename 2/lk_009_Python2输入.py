# -*- coding: utf-8 -*-
# Python 2.x 版本

# 函数：封装了一些功能，只需要写一个函数名字，就可以使用这些功能
content = raw_input('请输入内容')  # 把输入的内容当作字符串处理
print type(content)
print content

content = input('请输入内容')  # 把输入的内容当作代码处理。
print type(content)
print content

# input 相当于 raw_input + eval
content = raw_input('请输入内容')
result = eval(content)
print type(content)
print content
