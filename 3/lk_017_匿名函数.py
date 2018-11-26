# 匿名函数
result = (lambda x, y: x + y)(1, 2)
print(result)
"""
3
"""

func = lambda x, y: x + y
print(func(4, 5))
"""
9
"""

# 应用场景
li = [
    {'name': '团子', 'age': 18},
    {'name': '小明', 'age': 20},
    {'name': '大锤', 'age': 19}]
result = sorted(li, key=lambda x: x['age'])
print(result)
"""
[{'name': '团子', 'age': 18}, {'name': '大锤', 'age': 19}, {'name': '小明', 'age': 20}]
"""

# 更好的写法
from operator import itemgetter
result = sorted(li, key=itemgetter('age'))
print(result)
"""
[{'name': '团子', 'age': 18}, {'name': '大锤', 'age': 19}, {'name': '小明', 'age': 20}]
"""
