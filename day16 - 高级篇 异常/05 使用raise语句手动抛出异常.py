"""使用raise语句手动抛出异常"""

"""
    对于前面课程中的示例，在发生异常时的异常实例对象都是被自动抛出的。
    我们可以使用raise语句手动抛出异常实例对象，其语法格式为:
raise 异常类对象[([参数])]
如果没有传入参数，可以省略掉小括号。
"""

# raise ZeroDivisionError('0不能作为除数')
# raise ZeroDivisionError()
# raise ZeroDivisionError


try:
    raise ZeroDivisionError('0不能作为除数')
except ZeroDivisionError as err:
    print(err)

"""
    如果在except语句块中不想对异常实例对象进行处理，可以使用关键字raise将其原样抛出。
"""
"""
try:
    raise ZeroDivisionError('0不能作为除数')
except ZeroDivisionError:
    raise
"""

"""
    如果在except语句块中不想对异常实例对象进行处理，还可以使用raise语句手动抛出另外一个异常害对象的实例对象。
"""

try:
    raise ZeroDivisionError('0不能作为除数')
except ZeroDivisionError:
    raise ValueError('输入错误')
