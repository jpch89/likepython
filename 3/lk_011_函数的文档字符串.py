def calculate(a, b=1):
    """
    计算两数之和与两数之差。
    :param a: 数值1，数值类型，不可选，没有默认值
    :param b: 数值2，数值类型，可选，默认值：1
    :return: 返回计算结果，元组：(和, 差)
    """
    return (a + b, a - b)

print(help(calculate))
"""
Help on function calculate in module __main__:

calculate(a, b=1)
    计算两数之和与两数之差。
    :param a: 数值1，数值类型，不可选，没有默认值
    :param b: 数值2，数值类型，可选，默认值：1
    :return: 返回计算结果，元组：(和, 差)

None
"""
