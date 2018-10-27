# Python 是个强类型的语言
# 不同数据类型不能运算
num = '6'
print(type(int(num)))
print(4 + int(num))
print(str(4) + num)

# 为什么要进行类型转换？
# 因为有时候无法控制数据的类型
score = input('请输入一个数字：')
print(type(score))
print(int(score) + 6)

# 不能随意转换类型
num = '123'
result = int(num)
print(result)
# num = '123a' 这样就不能进行 int(num) 转换
