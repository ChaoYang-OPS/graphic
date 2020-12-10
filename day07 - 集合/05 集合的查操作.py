"""集合的查操作"""
"""
    可以使用运算符in(not in)检查集合中是否存在（不存在）指定的元素。
"""
s = {3, 4, 5, 6, 7}
print(5 in s)  # True
print(8 in s)  # False

print(5 not in s)  # False
print(8 not in s)  # True
