"""获取对象的信息之特殊属性__dict__"""

"""
    对于指定的类型或实例对象，可以访问特殊属性__dict__获得该类对象或实例对象所绑定的
所有属性和方法的字典。其中，字典中的键为属性名或方法名。
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


MyClass.ca2 = "ca2"
print(MyClass.__dict__)

mc = MyClass()
mc.ia2 = "ia2"
print(mc.__dict__)  # {'ia': 'ia', 'ia2': 'ia2'}
