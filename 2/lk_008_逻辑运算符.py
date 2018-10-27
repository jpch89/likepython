b = True

# not 非
print(b)
print(not b)

# and 与（并且）
# 规律：一假全假
# 注意：短路逻辑
print(True and False)

# or 或（或者）
# 规律：一真全真
# 注意：短路逻辑
print(True or False)

# 对于非布尔类型的判断：非零即真，非空即真
print(bool(1))
print(bool('0'))  # 这个也是真，因为字符串非空！

# 整个逻辑表达式的结果不一定只是True和False
print(100 or False)  # 返回第一个表达式的结果
print(1 and 3)  # 求值到哪个表达式，就返回该表达式的结果
print('哈哈哈' or 3)  # 得到 '哈哈哈'
print(0 or False)  # 得到 False
print(0 or False or 6)  # 得到 6

# and 和 or 可以不断往后写
