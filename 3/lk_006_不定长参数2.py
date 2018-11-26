def my_sum(**kwargs):
    print(kwargs, type(kwargs))

my_sum(name='团子', age=12)
"""
{'name': '团子', 'age': 12} <class 'dict'>
"""
