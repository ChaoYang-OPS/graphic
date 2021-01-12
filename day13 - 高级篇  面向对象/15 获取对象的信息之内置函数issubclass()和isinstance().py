"""获取对象的信息之内置函数issubclass()和isinstance()"""

"""
    内置函数issubclass()用于判断类对象与类对象之间的关系。
    内置函数isinstance()用于判断实例对象与类对象之间的关系。
"""

"""
    内置函数issubclass接收两个实参，
        第一个实参是类对象，
        第二个实参是类对象或由类对象组成的元组。
    当第二个实参是类对象时，如果第一个实参是第二个实参的子类，那么返回True。
    当第二个实参是类对象组成的元组时，如果第一个实参是第二个实参中任意一个类对象的子类，返回True。
"""


class A(object):
    pass


class B(object):
    pass


class C(object):
    pass


class D(A):
    pass


print(issubclass(D, A))  # True

print(issubclass(D, B))  # False

print(issubclass(D, (B, A, C)))  # True
print(issubclass(D, (B, C)))  # False

print(issubclass(bool, int))  # True
print(issubclass(bool, str))  # False

print(issubclass(bool, (str, int, dict)))  # True

print(issubclass(bool, (str, list, dict)))  # False


"""
    内置函数isinstance接收两个实参，
        第一个实参是实例对象，
        第二个实参是类对象或由类对象组成的元组。
    当第二个实参是类对象时，如果第一个实参是第二个实参的实例对象，或者第一个实参是第二个实参的
子类的实例对象，那么返回True。
    当第二个实参是类对象组成的元组时，如果第一个实参是第二个实参中任意一个类对象或其子类的实例对象，
那么返回True。
"""


print(isinstance(D(), D))  # True

print(isinstance(D(), A))  # True

print(isinstance(D(), (B, A, C)))  # True

print(isinstance(D(), (D, B, C)))  # True

















