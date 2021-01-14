""" 类对象的特殊方法之__call__()"""
"""
    如果在类对象中实现了特殊方法__call__()，那么就可以调用函数一样直接调用这个类对象的
实例对象，从而会自动调用特殊方法__call__()。
"""


class MyClass(object):
    def __call__(self, *args, **kwargs):
        print(args, kwargs)


mc = MyClass()
mc()  # () {}
mc(1, 2, x=3, y=4)  # (1, 2) {'x': 3, 'y': 4}

"""
    内置函数callable用于判断指定对象是否是可调用的。
    除了函数对象是可调用的之外，对于实现了特殊方法__call__()的类对象，其实例对象也是可调用的。
"""
print(callable(print))  # True


def do_sth():
    pass


print(callable(do_sth))  # True

print(callable(MyClass()))  # True
