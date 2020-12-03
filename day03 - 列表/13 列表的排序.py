"""列表的排序"""
"""
   如果想对列表中的所有元素进行排序，常见的方式有两种

一、 调用方法sort
      调用方法sort后，列表中的所有元素默认按照从小到大的顺序进行排序
"""

L = [5, 3, 8, 1, 6]
L.sort()
print(L)  # [1, 3, 5, 6, 8]

"""
  调用方法sort时，可以指定参数reverse = True，从而按照逆序进行排序
"""
L.sort(reverse=True)
print(L)  # [8, 6, 5, 3, 1]

"""
二、 调用内置函数sorted
     内置函数sorted的返回值是排序后生成的新列表，且被排序的列表不发生变化。
"""
L = [5, 3, 8, 1, 6]

print(sorted(L))  # [1, 3, 5, 6, 8]
print(L)  # [5, 3, 8, 1, 6]

"""
        调用内置函数sorted时，可以指定参数reverse = True，从而按照逆序进行排序
"""
print(sorted(L, reverse=True))  # [8, 6, 5, 3, 1]
print(L)  # [5, 3, 8, 1, 6]
