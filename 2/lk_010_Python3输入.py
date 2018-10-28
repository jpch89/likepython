# Python 3.x 中的 input 相当于 Python 2.x 中的 raw_input
content = input('请输入内容')
print(type(content))
print(content)

# 实现 Python 2.x 中的 raw_input 功能
content = input('请输入内容')
result = eval(content)
print(type(result))
print(result)
