"""继承"""

"""
    子类只有一个直接父类时称为单继承，假设子类和父类分别为ChildClass和ParentClass,
子类继承父类的语法格式为:
class ChildClass(ParentClass):
    pass

    子类有多个直接父类时称为多继承，假设子类是ChildClass,直接父类是ParentClass1,
ParentClass2,....,ParentClassn,子类继承父类的语法格式为:
class ChildClass(ParentClass1, ParentClass2,..., ParentClassn):
    pass
"""

"""
    子类会继承所有父类（包括所有直接父类和所有间接父类）的所有属性和方法。
"""


class ParentClassA(object):
    ca = 18

    def im(self):
        print("im()被调用了")


class ParentClassB(object):
    __pca = 23

    def __pim(self):
        print("__pim()被调用了")


class ParentClassC(ParentClassA, ParentClassB):
    @classmethod
    def cm(cls):
        print("cm()被调用了")


class ParentClassD(object):
    @staticmethod
    def sm():
        print("sm()被调用了")


class ChildClass(ParentClassC, ParentClassD):
    pass


print(dir(ChildClass))

"""
    子类可以添加父类中没有属性和方法。
"""


class BaseClass(object):
    ca_base = 5

    def im_base(self):
        print("im_base()被调用了")


class SubClass(BaseClass):
    ca_sub = 8

    def im_sub(self):
        print("im_sub()被调用了")


print(dir(SubClass))  # 'ca_base', 'ca_sub', 'im_base', 'im_sub'
