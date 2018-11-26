# a, b 是形参，也就是变量
# 传递数据就是指给变量赋值
def test(a, b):
    print(a + b)

print(test)
print(id(test))
"""
<function test at 0x000001F982C11E18>
2171152178712
"""

# 函数本身也可以作为数据
# 传递给另外一个变量
test2 = test
test2(1, 2)
print(id(test2))
"""
3
2171152178712
"""

# 高阶函数：接收函数作为参数的函数
# sorted
li = [
    {'name': '团子', 'age': 18},
    {'name': '小明', 'age': 20},
    {'name': '大锤', 'age': 19}]

# result = sorted(li)
# print(result)
"""
TypeError: '<' not supported between instances of 'dict' and 'dict'
"""

def get_key(x):
    return x['age']

result = sorted(li, key=get_key)
print(result)
"""
[{'name': '团子', 'age': 18}, {'name': '大锤', 'age': 19}, {'name': '小明', 'age': 20}]
"""

# sorted 接收 get_key 作为参数，所以它是高阶函数
