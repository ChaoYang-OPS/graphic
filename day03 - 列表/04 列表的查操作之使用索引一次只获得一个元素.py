"""列表的"查"操作之使用索引一次只获得一个元素"""
"""
    可以索引获得列表中的元素，但是，一次只获得一个元素。
"""

L = [5, 3, 9, 4, 0, 6, 8, 1, 7, 2]

print(L[0])  # 5
print(L[-10])  # 5

print(L[6])  # 8
print(L[-4])  # 8

print(L[9])  # 2
print(L[-1])  # 2
"""
    如果指定的索引在列表中不存在，会抛出IndexError
"""
# print(L[10])  # IndexError: list index out of range
