# 10是否大于2，结果是布尔类型
result = 10 > 2
print(result)

# 不等于
result = 10 != 2
print(result)

# 大于或者等于
result = 10 <= 10
print(result)

# 是否相等
result = 10 == 10
print(result)

# 比对唯一标识
a = 10
# 查看 a 的唯一标识
print(id(a))
# == 比较值
# is 比较唯一标识
b = 10
print(id(b))
print(a is b)

a = [1]
b = [1]
print(a == b)
print(a is b)
print(id(a), id(b))

# 链式比较运算符
num = 10
# 其它语言的写法：
# num > 5 && num < 20
# Python的写法：
print(5 < num < 20)
