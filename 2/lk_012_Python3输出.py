# -*- coding: utf-8 -*-
# Python 3.x

# 输出一个值
print(123)

# 输出一个变量
num = 55
print(num)

# 输出多个变量
num2 = 44
print(num, num2)

# 格式化输出
name = '团子'
age = 18
# 我的名字是团子，年龄是18
# '我的名字是%s，年龄是%d' % (name, age)
# 上面那个整体就相当于是一个字符串
# % 是属于字符串拼接的范畴
print('我的名字是%s，年龄是%d' % (name, age))

# .format 方法，字符串是一个对象，可以调用对象的方法
print('我的名字是{0}，年龄是{1}'.format(name, age))
# format 还可以使用名称或者下标的形式，后面补充

# 输出到文件中
# 'w' 是操作权限符
f = open('test.txt', 'w')
print('测试内容', file=f)
# 默认情况下是标准输出，即输出到控制台
import sys
print('测试内容', file=sys.stdout)
f.close()

# 输出不自动换行
print('abc', end='')
print('def')

# 输出的各个数据，使用分隔符分割
# 默认使用空格分隔
# 需求：使用-分割
print('1', '2', '3', sep='=')

# flush 参数的说明
# print('请输入账号', end='')
print('请输入账号', end='', flush=True)
# 休眠 5s
# 睡眠的过程中什么都不做
from time import sleep
sleep(3)
