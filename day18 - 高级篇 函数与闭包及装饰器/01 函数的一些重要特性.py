"""函数的一些重要特性"""

"""
    在Python中，一切皆为对象。所以，函数也是对象，从而函数可以被赋值给变量。
"""


def add(num1, num2):
    return num1 + num2


print(add)  # <function add at 0x1076125e0>

f = add
print(f(1, 2))  # 3

"""
    一个函数可以作为另一个函数的实参。
"""


def eval_square(x):
    return x * x


result = map(eval_square, [1, 2, 3, 4])
print(list(result))  # [1, 4, 9, 16]

"""
    一个函数可以作为另一个函数的返回值。
"""

def do_sth():
    return add

print(do_sth()(1, 2))  # 3

"""
    一个函数可以嵌套定义在另一个函数中。
"""

def outer():
    def inner():
        print("This is inner.")
    return inner

outer()()  # This is inner.
