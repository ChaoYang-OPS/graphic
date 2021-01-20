v = 56

_v = 56

def f():
    print('f被调用')

def _f():
    print('f被调用')
class SomeClass:
    pass

class _SomeClass:
    pass


print('模块的特殊属性__name__的值为:{}'.format(__name__))

"""
以下是测试代码
"""


def add_num(num1, num2):
    return num1 + num2


# 根据__name__的值判断是否执行模块中的测试代码。
if __name__ == '__main__':
    print('1 + 2 =', add_num(1, 2))
    print('3 + 5 = ', add_num(3, 5))
