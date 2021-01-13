"""类对象的特殊方法之__new__()"""

"""
   当使用"类名([实参])"创建实例对象时，Python解释器的主要处理过程包括两大步:
1. 调用特殊方法__new__()创建实例对象
    首先会查找该类对象是否实现了特殊方法__new__(), 如果没有实现，则去其父类中依次查找，
直到类对象object。
    特殊方法__new__()会返回创建的实例对象。
    
2. 调用特殊方法__init__()对创建的实例对象进行初始化
    __new__()返回的实例对象作为实参被自动传递给__init__()的第一个形参self。
"""


class Parent(object):
    def __new__(cls, *args, **kwargs):
        print("父类的__new__()被调用，其形参cls对应实参的id:{}".format(id(cls)))
        # 父类的__new__()被调用，其形参cls对应实参的id:140509787035152
        obj = super().__new__(cls)  # object的特殊方法知道如何创建实例对象
        print("创建的实例对象的id:{}".format(id(obj)))
        # 创建的实例对象的id:4360417488
        return obj


class Child(Parent):
    def __init__(self, name):
        print("子类的__init__()被调用,其形参self对应实参的id:{}".format(id(self)))
        # 子类的__init__()被调用,其形参self对应实参的id:4360417488
        self.name = name


print("父类的id:{}".format(id(Parent)))  # 父类的id:140509787031088
print("子类的id:{}".format(id(Child)))   # 子类的id:140509787035152

child = Child("Mike")
print("创建的实例对象的id:{}".format(id(child)))
# 创建的实例对象的id:4360417488



