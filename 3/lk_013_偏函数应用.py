num_string = '100010'
result = int(num_string, base=2)
print(result)
"""
34
"""

# 在往后的一段时间里
# 我都需要把一个二进制的字符串，转换成对应的十进制数据
from functools import partial
int2 = partial(int, base=2)
result = int2(num_string)
print(result)
"""
34
"""
