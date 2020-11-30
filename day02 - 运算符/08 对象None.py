"""对象None"""

"""
一、 什么是对象None
      对象None用于表示数据值的不存在。
      对象None是占据一定的内存空间的，它并不意味着"空"或"没有定义",
      也就是说，None是"something",而不是"nothing"。
"""
# 调用内置函数id查看对象None的内存地址
print(id(None))  # 4530626192

"""
二、 对象None的使用场景
      对象None经常用于变量的初始化，或将变量重置为"数据值不存在"状态.
"""

a = None
print(a)   # None

b = 18
print(b)   # 18
b = None
print(b)   # None