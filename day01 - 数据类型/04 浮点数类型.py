"""浮点数类型"""

"""
一、 什么是浮点数类型
   浮点数类型用于表示浮点数，也就是小数
"""

print(0.123456)  # 0.123456

"""
二、 浮点数的创建
    除了使用小数创建浮点数外，还可以调用内置函数float创建浮点数
    不传递任何参数时，返回浮点数0.0
    只传递一个参数时，将传递的参数转换为浮点数
"""
print(float())  # 0.0

print(float(118))  # 118.0

print(float(118.2))  # 118.2

print(float('118'))  # 118.0

"""
三、 用科学计数法表示浮点数
    很大或很小的浮点数可以用科学计数法来表示: men表示: m乘以10的n次方
"""

print(2.3e8)  # 230000000.0
print(2.3e-4)  # 0.00023

"""
四、浮点数存储的不精确性
   计算机采用二进制存储浮点数时是不精确的，可能会存在误差，因此对于浮点数的运算要格外小心
"""
print(1.1 + 2.2 - 3.3)  # 4.440892098500626e-16

print(1.1 + 2.2)  # 3.3000000000000003

"""
    解决方案: 导入模块decimal或fractions
    模块decimal用于处理十进制的浮点数，模块fractions用于处理分数
"""
from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2') - Decimal('3.3'))  # 0.0

from fractions import Fraction

print(Fraction(11, 10) + Fraction(22, 10) - Fraction(33, 10))  # 0
