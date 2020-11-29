"""布尔运算符"""

"""
一、什么是布尔运算符
    布尔运算符用于对布尔值进行运算，运算结果仍然是一个布尔值
    布尔运算符包含如下三个:
1、 and
2、 or
3、 not
"""

"""
二、布尔运算符and
    当两个运算数都为True时，运算结果才为True
"""

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

"""
三、 布尔运算符or
    只要一个运算数为True，运算结果就为True
"""

print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

"""
四、布尔运算符not
    用于对运算数取反
        如果运算数为True，运算结果为False
        如果运算数为False，运算结果为True
"""

print(not True)  # False
print(not False)  # True
