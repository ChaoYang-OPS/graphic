"""类对象的特殊方法之__getattr__()"""
"""
    当访问实例对象的属性或方法时，如果指定的属性或方法不存在，就会抛出AttributeError。
"""


class MyClass(object):
    pass


mc = MyClass()
# print(mc.data)  # AttributeError: 'MyClass' object has no attribute 'data'
# mc.do_sth()  # AttributeError: 'MyClass' object has no attribute 'do_sth'
"""
    当访问实例对象的属性或方法时，为了避免指定的属性或方法不存在时抛出AttributeError,
可以在实例对象对应的类对象中实现特殊方法__getattr__()。这样，当指定的属性或方法不存在时，
会自动调用特殊方法__getattr__()。
"""


class SomeClass(object):
    def __getattr__(self, name):
        if name == "data":
            return 18
        elif name == "do_sth":
            return print
        raise AttributeError("'SomeClass' object as no attribute '{}'".format(name))


sc = SomeClass()
print(sc.data)  # 18
sc.do_sth(1, 2, 3)  # 1 2 3

# print(sc.score)  # AttributeError: 'SomeClass' object as no attribute score'
