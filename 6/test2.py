import tools

# 查看模块对象
print(tools)
# <module 'tools' from 'D:\\code\\likepython\\6\\tools.py'>

# 查看内存地址
print('内存地址为', id(tools))
# 内存地址为 1511359636648

# 查看类型
print('类型为', type(tools))
# 类型为 <class 'module'>

# 查看模块对象的方法和属性
print('模块对象的方法和属性为', tools.__dict__)
