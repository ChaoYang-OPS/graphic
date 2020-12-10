"""不可变集合frozenset"""

"""
一、什么是frozenset
    顾名思义，frozenset的意思是"被冻结的set",也就是不可变的set。
    frozenset之于set就好比tuple之于list。
    
    因为frozenset是不可变类型，所以frozenset类型的对象:
1、 存在哈希值
2、 可以作为字典的key
3、 可以做为set中的元素
"""

"""
二、frozenset对象的创建
    可以调用内置函数frozenset（类frozenset的构造方法）创建frozenset对象。
"""
print(frozenset())  # frozenset()
print(frozenset(range(1, 6)))  # frozenset({1, 2, 3, 4, 5})
print(frozenset([3, 5, 9, 2, 6]))  # frozenset({2, 3, 5, 6, 9})
print(frozenset((3, 5, 9, 2, 6)))  # frozenset({2, 3, 5, 6, 9})
print(frozenset('35926'))  # frozenset({'6', '2', '5', '3', '9'})
print(frozenset({3, 5, 9, 2, 6}))  # frozenset({2, 3, 5, 6, 9})
