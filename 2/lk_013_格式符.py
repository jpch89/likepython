# 格式化输出
name = '团子'
age = 18

# 我的名字是...，年龄是...
print('我的名字是%s，年龄是%d' % (name, age))

# %[(name)][flags][width][.precision]typecode

# typecode 类型码，就是 s， d 这种

# [] 可以省略的

# (name)
# 表示根据指定的名称(key)，查找对应的值，格式化到字符串中
math = 60
english = 100
print('我的数学成绩是%d, 英文成绩是%d' % (math, english))
# 需求，调换两个分数
# 方法1：直接在后面调换
print('我的数学成绩是%d, 英文成绩是%d' % (english, math))
# 方法2：借助(name)
print('我的数学成绩是%(math)d, 英文成绩是%(en)d' % {'en': english, 'math': math})
# jpch89：字符串里面写%(key)类型码，格式符%后面跟着字典（字典外面不用加括号！）

# width表示占用的宽度
print('%10d' % math)
# flag表示对齐方式，默认右对齐，用空格填充
# - 表示左对齐
print('%-10d' % math)
# 空格 这样写可以对齐负数
print('% d' % -math)
print('% d' % math)
# 写两个空格还是一个空格
print('%  d' % math)

mini = 5
sec = 8
print('%02d:%02d' % (mini, sec))

score = 59.6
print('%d' % score)  # 59，截取整数部分，类似于 int 类型转换的效果
print('%f' % score)  # 默认小数点后6喂
print('%.2f' % score)

# 类型码 typecode
# i/d 整数、浮点数变成十进制整数
print('%i' % score)
print('%i' % 0b11)
print('%d' % 0o10)
print('%d' % 0x10)

# o 转换成八进制数表示
print('%o' % 8)

# x 转换成十六进制数表示

# e 科学记数法，E 大写E的科学记数法
print('%e' % 16)

# g，G
print('%d' % 101.1)  # 无法转换成 101.1
print('%g' % 101.1)
print('%g' % 101)
print('%g' % 1111111)  # 超过6位自动转换成科学记数法

# c
print('%c' % 97)

# 需求：输出 num%
num = 99
print('%d%%')  # %% 表示百分号

# 注意：没有 %b！
print('%b' % 10)  # 不支持！
