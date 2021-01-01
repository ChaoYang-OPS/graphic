""" 定义类对象和创建实例对象"""

"""
一、定义类对象
    定义类对象的语法格式:
class 类名(object):
    # 属性和方法
其中，
1. 类名由一个或多个单词组合而成，每个单词的首字母大写且其余字母全部小写,例如: SomeClass。
2. (object)表示该类对象继承自Python内置的类对象object，Python中所有的类对象都继承自
一个统一的基类:object。
"""


class SomeClass(object):
    pass


"""
二、创建实例对象
    根据类对象创建实例对象的语法格式为: 类名([实参])。
    
    为了在创建实例对象后对其进行初始化（例如: 给实例对象绑定一些属性），可以在类对象中定义一个
名为__init__的特殊方法(以双下划线__开头和结尾的方法)。这样，创建实例对象后就会自动调用
特殊方法__init__。
    方法就是定义在类对象中的函数。方法与函数的区别在于:
1. 定义方法时，方法的第一个形参表示调用该方法的实例对象，第一个形参的名称通常是self,也可以是
其它名称。
2. 调用方法时，系统自动将调用该方法的实例对象作为实参传递给第一个形参。第一个实参会传递给第二个
形参，第二个实参会传递给第三个形参，依次类推。
    如果没有定义特殊方法__init__，或者定义了特殊方法__init__但是没有定义除self之外的形参，
那么根据类对象创建实例对象时就不需要传入实参。
    如果在类对象中定义了特殊方法__init__，那么对于"类名([实参])"，会执行两大步:
1. 创建实例对象
2. 自动调用创建的实例对象的特殊方法__init__(创建的实例对象会作为实参被自动传递给特殊方法__init__
的第一个形参self)。

"""

sc = SomeClass()
print(sc)  # <__main__.SomeClass object at 0x108c85670>


class SomeClass1(object):
    def __init__(self):
        self.data = 18


sc1 = SomeClass1()
print(sc1)  # <__main__.SomeClass1 object at 0x10452c460>

class SomeClass2(object):
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2


sc2 = SomeClass2(5, 8)
print(sc2)  # <__main__.SomeClass2 object at 0x10d4b82b0>
