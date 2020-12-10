"""集合间的关系"""
"""
一、 两个集合是否相等
     可以使用运算符==和!=进行判断
"""
s1 = {1, 3, 5, 7, 9}
s2 = {3, 7, 9, 5, 1}
print(s1 == s2)  # True
print(s1 != s2)  # False
"""
二、一个集合是否是另一个集合的子集
   可以调用方法issubset进行判断。
"""
s1 = {1, 3, 5, 7, 9}
s2 = {2, 3, 6, 7, 10}
s3 = {1, 3, 5, 6, 7, 9}
print(s1.issubset(s2))  # False
print(s1.issubset(s3))  # True
"""
三、 一个集合是否是另一个集合的超集
     可以调用方法issuperset进行判断
"""
print(s2.issuperset(s1))  # False
print(s3.issuperset(s1))  # True

"""
四、 两个集合是否没有交集
    可以调用方法isdisjoint进行判断
"""
s1 = {1, 3, 5, 7, 9}
s2 = {2, 3, 6, 7, 10}
s3 = {2, 4, 6, 8, 10}
print(s1.isdisjoint(s2))  # False
print(s1.isdisjoint(s3))  # True