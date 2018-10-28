# -*- coding: utf-8 -*-
# Python 2.x

# 输出一个值
print 123

# 输出一个变量
num = 10
print num

# 输出多个变量
num2 = 66
print num, num2

# 格式化输出
name = '团子'
age = 18
# 我的名字是团子，年龄是18
print '我的名字是', name, '年龄是', age
print '我的名字是%s，年龄是%d' % (name, age)
# 注意：格式化输出不是隶属于print语句，而是属于字符串

# .format 方法，字符串是一个对象，可以调用对象的方法
print '我的名字是{0}，年龄是{1}'.format(name, age)
# 两个都找第0个值
print '我的名字是{0}，年龄是{0}'.format(name, age)

# 输出到文件中
f = open('test.txt', 'w')
# 重定向符号 >> 尖尖
print >> f, '测试字符串'

# 输出不自动换行
print '1',  # 不换行
print '2',
print '3',

# 输出的各个数据，使用分隔符分割
# 默认使用空格分隔
# 需求：使用-分割
print '-'.join(['a', 'b', 'c'])
