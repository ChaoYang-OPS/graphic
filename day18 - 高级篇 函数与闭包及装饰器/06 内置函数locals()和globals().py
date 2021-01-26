"""内置函数locals()和globals()"""

"""
    命名空间指的是某个作用域内所有名字和值的映射，用字典来表示。
    
    内置函数locals()可以返回其所在局部作用域的命名空间。
    内置函数globals()可以返回其所在全局作用域的命名空间。
"""


def outer(a):
    b = 8

    def inner(c):
        d = 3

    print(locals())


outer(5)  # {'a': 5, 'b': 8, 'inner': <function outer.<locals>.inner at 0x10ffdb670>}

g = 2


class MyClass(object):
    pass


print(globals())
"""
    locals()并没有返回实际的命名空间，而是返回值的拷贝，所以，通过locals()修改某个名字对应的值，
对于实际的命名空间是没有影响的；但是，可以通过locals()向实际的命名空间中添加一个名字和值的映射。
"""


def f():
    x = 8
    print(locals())  # {'x': 8}
    locals()['x'] = 9

    locals()['y'] = 10

    print(locals())  # {'x': 8, 'y': 10}


f()

"""
    globals()返回的是实际的命名空间，所以，对globals()所做的任何修改，其实就是对实际命名空间的修改。
"""
globals()['g'] = 6
globals()['gg'] = 66
print(globals())

"""
    可以在局部作用域或嵌套作用域中通过globals()访问全局作用域中被屏蔽的全局变量。
"""
def do_sth():
    g = 123
    print(globals()['g'])


do_sth()  # 6


"""
    对于内置函数vars()，查看其帮助信息可知:
    vars([object]) -> dictionary
    Without arguments, equivalent to locals().
    With an argument, equivalent to object.__dict__.
"""