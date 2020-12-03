"""列表的反转"""

"""
    如果想对列表中的所有元素进行反转，常见的方式有两种:
一、 调用方法reverse
"""
L = [1, 2, 3, 4, 5]
L.reverse()
print(L)  # [5, 4, 3, 2, 1]

"""
二、调用内置函数reversed
     内置函数reversed的返回值是一个迭代器对象，且被反转的列表不发生变化。
"""
L = [1, 2, 3, 4, 5]
iterator = reversed(L)
print(iterator)  # <list_reverseiterator object at 0x102e6c0d0>
print(list(iterator))  # [5, 4, 3, 2, 1]
print(L)  # [1, 2, 3, 4, 5]
