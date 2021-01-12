"""MRO"""

"""
    MRO的全称是Method Resolution(方法解析顺序), 它指的是对于一颗类继承，当调用
最底层类对象所对应实例对象的方法时，Python解释器在类继承树上搜索方法的顺序。
    对于一颗类继承树，可以调用最底层类对象的方法mro()或访问最底层类对象的特殊属性__mro__，
获得这棵类继承树的MRO。
"""
"""

class A(object):
    def f(self):
        print("A.f")


class B(A):
    def f(self):
        print("B.f")


class C(A):
    def f(self):
        print("C.f")


class D(B, C):
    def f(self):
        print("D.f")



print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
#  <class '__main__.A'>, <class 'object'>]
d = D()
d.f()  # D.f

print(D.__mro__)

# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
#  <class '__main__.A'>, <class 'object'>)
"""
"""
    在子类重写后的方法中通过super()调用父类中被被重写的方法时，在父类中搜索方法的顺序基于
以该子类为最底层类对象的类继承树的MRO。
    如果想调用指定父类中被重写的方法，可以给super()传入两个实参: super(a_type, obj)，其中
第一个实参a_type是个类对象，第二个实参obj是实例对象，这样，被指定的父类是:
obj所对应类对象的MRO中，a_type后面那个类对象。
"""


class A(object):
    def f(self):
        print("A.f")


class B(A):
    def f(self):
        print("B.f")


class C(A):
    def f(self):
        print("C.f")


class D(B, C):
    def f(self):
        # super(B, self).f()  # C.f
        super(C, self).f()   # A.f
        # super().f()


d = D()  # B.f
d.f()
