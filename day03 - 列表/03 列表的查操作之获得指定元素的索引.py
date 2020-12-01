""" 列表的查操作之获得指定元素的索引"""
"""
一、 列表中元素的索引
    列表中的每个元素都有两个整数类型的索引:
1、 第1个元素的索引是0，后面元素的索引依次递增1;
2、 最后一个元素的索引是-1，前面元素的索引依次递减1.

二、获得列表中指定元素的索引
如果想要获得列表中指定元素的索引，可以调用方法index,该方法只返回两个整数索引中大于0的那个
     
"""
L = [5, 3, 7, 9, 2, 1, 7, 6]
print(L.index(9))  # 3
"""
    如果列表中存在多个指定元素，方法index只返回第1个指定元素的索引值。
"""
print(L.index(7))  # 2

"""
  如果列表中不存在指定元素，方法index抛出ValueError
"""
# print(L.index(8))  # ValueError: 8 is not in list

"""
  调用方法index时还可以指定起始索引start和结束索引stop这两个参数。
"""
# 只指定起始索引start(不能只指定结束索引)
print(L.index(7, 3))  # 6

print(L.index(7, 3, 7))  # 6
# 指定起始索引start和结束索引stop
# print(L.index(7, 3, 5))  # ValueError: 7 is not in list
