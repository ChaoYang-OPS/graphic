""" 函数的定义之使用**定义个数可变的关键字形参"""

""" 
    与"函数的定义之使用*定义个数可变的位置形参"进行对比学习
"""

"""
    定义函数时，可能无法事先确定传递的关键字实参的个数，在这种情况下，可以在形参前添加
两个**，将形参定义为个数可变的关键字形参，从而可以接收0个或任意多个关键字实参。这些关键字实参
会将个数可变的关键字形参初始化为一个字典。
"""


def f(**kwargs):
    print(kwargs)


f()  # {}
f(a=1)  # {'a': 1}
f(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
"""
    定义函数时，最多只能定义一个个数可变的关键字形参。
"""

# def fun(**kwargs1, **kwargs2):
#     print(kwargs1, kwargs2)
"""
    很多内置函数都定义了个数可变的关键字形参。例如，内置函数sorted()的定义为:
def sorted(*args, **kwargs):
"""
L = ['Python', 'Java', 'Swift']
print(sorted(L))  # ['Java', 'Python', 'Swift']
print(sorted(L, key=len))  # ['Java', 'Swift', 'Python']
print(sorted(L, key=len, reverse=True))  # ['Python', 'Swift', 'Java']
"""
    因为调用函数时，位置实参必须位于关键字实参之前，所以个数可变的位置形参必须位于
个数可变的关键字形参之前。
"""
# def fun(**kwargs, *args):
#     print(kwargs, args)

def fun(*args, **kwargs):
    print(kwargs, args)