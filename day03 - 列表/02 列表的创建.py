"""列表的创建"""
"""
    创建列表的常见方式有两种:
一、 使用中括号
      当把列表赋值给变量时，变量名不要取名为list或l,因为list是列表对应的类名
l容易被误读或误写为阿拉伯数字1.
"""
L = ['Python', 18, True]
print(L)  # ['Python', 18, True]

# 空列表

print([])  # []

"""
二、 调用内置函数list(类list的构造方法)
"""
print(list(range(1, 6)))  # [1, 2, 3, 4, 5]
print(list(L))    # ['Python', 18, True]

# 空列表
print(list())     # []
