"""获取对象的信息之内置函数dir()"""

"""
    对于制定的类对象或实例对象，可以调用内置函数dir()获得其所有可以访问的属性和方法（包括
从父类中继承的属性和方法）的列表。
    类对象与实例对象的结果是有区别的，类对象的结果中不包括实例属性。
"""

class MyClass(object):
    ca = "ca"

    def __init__(self):
        self.ia = "ia"

    def im(self):
        pass

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass

print(dir(MyClass))  # .... 'ca', 'cm', 'im', 'sm'

print(dir(MyClass()))  #  ... ca', 'cm', 'ia', 'im', 'sm'

