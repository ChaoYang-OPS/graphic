"""函数的各种参数大总结"""


def f1(a, b=5, *args, **kwargs):
    print('a = {} b= {} args= {} kwargs= {}'.format(a, b, args, kwargs))


f1(2, 6, 7, 8, c=9)  # a = 2 b= 6 args= (7, 8) kwargs= {'c': 9}

f1(2)  # a = 2 b= 5 args= () kwargs= {}


def f2(a, b=5, *, c, **kwargs):
    print('a = {} b= {} c= {} kwargs= {}'.format(a, b, c, kwargs))


f2(*(3, 6), **{'c': 8, 'd': 10})  # a = 3 b= 6 c= 8 kwargs= {'d': 10}
f2(3, c=8, d=10)  # a = 3 b= 5 c= 8 kwargs= {'d': 10}
