"""列表生成式"""
"""
一、 什么是列表生成式
    如果想要生成列表[1, 4, 9, 16, 25, 36],可以使用for-in循环:
"""
L = []
for i in range(1, 7):
    L.append(i * i)
print(L)  # [1, 4, 9, 16, 25, 36]
"""
    上述的解决方案有更好的替代，那就是使用列表生成式。
    列表生成式的语法格式：[表示列表元素的表达式 for 自定义的变量 in 可迭代对象]
其中，"表示列表元素的表达式"中通常包含"自定义的变量"。
    列表生成式的使用场景： 凡是可以通过for-in循环创建的列表，都可以使用列表生成式来创建。
"""
L = [i * i for i in range(1, 7)]
print(L)  # [1, 4, 9, 16, 25, 36]

"""
二、在列表生成式中使用if语句
    可以在列表生成式的for-in循环后添加if语句。
"""
L = [i * i for i in range(1, 7) if not i % 2]
print(L)  # [4, 16, 36]

# 以上代码相当于:
L = []
for i in range(1, 7):
    if not i % 2:
        L.append(i * i)
print(L)

"""
三、在列表生成式中使用双重循环
"""
L = [(i, j) for i in range(1, 4) for j in range(1, 4)]
print(L)  # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
# 以上代码相当于:
L = []
for i in range(1, 4):
    for j in range(1, 4):
        L.append((i, j))
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
print(L)

L = [(i, j) for i in range(1, 4) for j in range(1, 4) if i != j]
print(L)  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

"""
四、 列表生成式支持嵌套
    可以在一个列表生成式中嵌套另一个列表生成式。
"""
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

L = [[row[i] for row in matrix] for i in range(4)]
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print(L)

# 以上代码相当于:
L = []
for i in range(4):
    L.append([row[i] for row in matrix])
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print(L)

# 以上代码相当于:
L = []
for i in range(4):
    l_row = []
    for row in matrix:
        l_row.append(row[i])
    L.append(l_row)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print(L)
