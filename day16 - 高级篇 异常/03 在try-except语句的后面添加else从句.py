"""在try-except语句的后面添加else从句"""
"""
    可以在while语句或for-in语句添加后面添加else从句，这样，如果没有执行循环体中的break语句
从而提前退出循环，就会执行else从句。
    类似地，可以在try-except语句的后面添加else从句，其语法格式为:
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
"""

try:
    # result = 1 / 0
    result = 1 / 2
    # result = int('abc')
except ZeroDivisionError:
    print("0不能作为除数")
except TypeError:
    print("类型错误")
else:
    print(result)
print("结束")

while True:
    try:
        x = int(input('请输入一个整数:'))
    except ValueError:
        print('无效的输入,请再次输入:')
    else:
        print('输入的整数为: {}'.format(x))
        break

