"""函数的定义之函数注解"""
"""
一、 什么是函数注解
    定义函数时，为了让形参或返回值的类型或作用，可以给形参或返回值添加函数注解，
从而对形参或返回值做解释说明，以帮助函数文档化。
    函数注解是可选的，可以添加也可以不添加。
    函数注解可以是任意的表达式。
    解释器会忽略函数注解，因此解释器并不会使用函数注解来检查实参的类型和返回值的类型。
    
    更多关于函数注解，可参考PEP 3107: https://www.python.org/dev/peps/pep-3107/
"""

"""
二、添加函数注解
    给形参添加函数注解的方式为: 在形参后面添加:和任意的表达式。
    给返回值添加函数注解的方式为: 在)的后面添加->和任意的表达式。
"""


def f(a: 'string type', b: int) -> 'join a with b':
    return a + str(b)


print(f('hello', 12.3))  # hello12.3

"""
三、访问函数注解
    通过属性__annotations__可以访问函数注解。
    调用内置函数help()得到的帮助信息中会包含函数注解
"""
# {'a': 'string type', 'b': <class 'int'>, 'return': 'join a with b'}
print(f.__annotations__)
print(help(f))
# f(a: 'string type', b: int) -> 'join a with b'
