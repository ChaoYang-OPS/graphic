"""函数的定义之使用定义关键字形参"""

"""
    定义函数时，可以在所有形参的某个位置添加一个*,这样， * 后面的所有形参都被定义为
只能接收关键字实参的关键字形参。
"""


def f(a, b, *, c, d):
    print('a = {} b = {} c = {} d = {}'.format(a, b, c, d))


f(1, 2, c=3, d=4)  # a = 1 b = 2 c = 3 d = 4
# f(1, 2, 3, 4)  # TypeError: f() takes 2 positional arguments but 4 were given
