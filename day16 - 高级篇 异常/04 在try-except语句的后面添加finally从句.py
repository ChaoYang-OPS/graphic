"""在try-except语句的后面添加finally从句"""

"""
    可以在try-except语句的后面添加finnally从句,其语法格式为:

try:
    可能会产生异常的代码
except  异常类对象1:
    当前except子句处理异常的代码
except  异常类对象2:
    当前except子句处理异常的代码
...
except  异常类对象n:
    当前except子句处理异常的代码
finally:
    总会被执行的代码
    
    因为finally从句总会被执行，所以通常在finally从句中释放资源，例如: 关闭文件、关闭网络连接等。
"""
try:
    result = 1 / 0
    # result = 1 / 2
    # result = int('abc')
    print(result)
except ZeroDivisionError:
    print("0不能作为除数")
except TypeError:
    print("类型错误")
finally:
    print("释放资源")
print("结束")

"""
    可以在try-except语句的后面同时添加else从句和finally从句，其语法格式为:
try:
    可能会产生异常的代码
except  异常类对象1:
    当前except子句处理异常的代码
except  异常类对象2:
    当前except子句处理异常的代码
...
except  异常类对象n:
    当前except子句处理异常的代码
else:
    try语句块中没有产生异常时执行的代码
finally:
    总会被执行的代码
"""


try:
    result = 1 / 0
    # result = 1 / 2
    # result = int('abc')
except ZeroDivisionError:
    print("0不能作为除数")
except TypeError:
    print("类型错误")
else:
    print(result)
finally:
    print("释放资源")
print("结束")











