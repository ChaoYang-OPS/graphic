"""对象的布尔值"""
"""
    所有对象都有一个布尔值，可以调用内置函数bool(类bool的构造方法)得到任何对象的布尔值。
    
    以下对象的布尔值为False: False、数值零、None、空字符串、空列表、空元组、空字典、空集合。
>>> bool(False)
False
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool('')
False
>>> bool("")
False
>>> bool([])
False
>>> bool(list())
False
>>> bool(())
False
>>> bool(tuple())
False
>>> bool({})
False
>>> bool(dict())
False
>>> bool(set())
False
>>> bool(frozenset())
False
>>> bool(18)
True
>>> bool('Python')
True
>>> bool(0)
False
>>> bool(1)
True
>>> bool([1, 2, 3, 4])
True
>>> bool((1, 2, 3, 4))
True
>>> bool({'a': 18, 'b': 56})
True
>>> bool({1, 2, 3, 4, 5})
True

"""

"""
    所有对象都可被直接用作布尔值，解释器会自动调用内置函数bool进行转换。
"""
if 18:
    print(18, True)  # 18 True

if 'Python':
    print('Python', True)  # Python True
