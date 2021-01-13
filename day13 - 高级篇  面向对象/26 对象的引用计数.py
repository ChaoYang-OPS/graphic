"""对象的引用计数"""

"""
一、什么是对象的引用计数
    通常情况下，开发人员无需关心内存的分配和释放。当创建一个对象时，系统会自动分配一块内存
以存储该对象的信息。当该对象不再被使用时，系统会进行垃圾回收以自动释放掉其占用的内存。
    为了确保使用中的对象不会被销毁，Python使用引用计数来跟踪和计算内存中每个对象被引用的次数。
当对象的引用计数为0时，它才可以被多销毁。
"""

"""
二、对象的引用计数加1的情形
1. 对象赋值给变量
2. 引用对象的变量赋值给另一个变量
3. 对象作为容器(例如:列表、元组、集合等)中的元素
4. 对象作为函数调用时的实参
"""


class MyClass(object):
    pass


def do_sth(param):
    pass


# 引用计数加1，变为1
a = MyClass()

# 引用计数加1，变为2
b = a
# 引用计数加1，变为3
L = [1, 2, a]
# 在函数的执行过程中，引用计数加1，变为4
do_sth(a)
# 当函数执行后，对实参的引用会自动销毁，因此，引用计数减1，变为3

import sys

# 在函数的执行过程中，引用计数加1，变为4
print(sys.getrefcount(a))  # 4
# 当函数执行后，对实参的引用会自动销毁，因此，引用计数减1，变为3


"""
三、对象的引用计数减1的情形
1. 对象离开它的作用域，例如：对象所在的函数执行完毕
2. 对象的引用被显式销毁
3. 引用对象的变量被赋予新的对象
4. 从容器中删除对象，或对象所在容器被销毁
"""
# 引用计数加1，变为1
x = MyClass()

# 引用计数加1，变为2
y = x

# 引用计数减1，变为1
del x

# 引用计数加1，变为2
z = y
# 引用计数减1，变为1
y = 18

# 引用计数加1，变为2
l = [1, 2, z]
# 引用计数减1，变为1
del l
# 在函数的执行过程中，引用计数加1，变为2
print(sys.getrefcount(z))  # 2

# 当函数执行后，对实参的引用会自动销毁，因此，引用计数减1，变为1
