"""比较运算符"""

"""
一、什么是比较运算符
    比较运算符用于比较两个运算数，比较结果是一个布尔值
    
    比较运算符包括如下几个:
1. <
2. <=
3. >
4. >=
5. == 
    ==用于比较两个运算数是否相等，也就是说，==用于"相等性"测试
6. !=
7. is
    is用于比较两个运算数是否是同一个对象，也就是说，is用于"同一性"测试
8 is not
"""
print(6 < 8)  # True
print(6 <= 8)  # True
print(8 > 6)  # True
print(8 >= 6)  # True
print(8 == 8.0)  # True
print(8 != 8.0)  # False

a = b = [1, 2, 3]
c = [1, 2, 3]
print(a == b)  # True
print(a == c)  # True
print(a is b)  # True
print(a is c)  # False

"""
二、不可变类型对象的is比较
    对于不可变类型的对象，其内存可能会被重用，比如说数值较小的整数对象
    可以调用内置函数id进行验证。内置函数id用于返回对象的唯一标识（对象在内存中的地址）
"""

a = 18
b = 18
print(id(a))  # 4450655456
print(id(b))  # 4450655456
print(a is b)  # True

"""
三、 比较运算符可用于链式比较
"""
age = 18
print(0 < age < 100)  # True
# 以上语句相当于
# print(0 < age and age < 100)  # True

print(1 == 2 < 3)  #
# 以上语句相当于:
print(1 == 2 and  2 < 3) # False
