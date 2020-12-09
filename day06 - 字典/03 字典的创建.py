"""字典的创建"""
"""
  创建字典的常见方式有三种：
一、使用花括号
"""
print({'name': 'Jack', 'age': 18})  # {'name': 'Jack', 'age': 18}

# 空字典
print({})  # {}

"""
二、 调用内置函数dict(类dict的构造方法)
"""
print(dict({'name': 'Jack', 'age': 18}))  # {'name': 'Jack', 'age': 18}
print(dict(name='Jack', age=18))  # {'name': 'Jack', 'age': 18}
print(dict([('name', 'Jack'), ('age', 18)]))  # {'name': 'Jack', 'age': 18}
print(dict(zip(range(3), 'ABC')))  # {0: 'A', 1: 'B', 2: 'C'}

# 空字典
print(dict())  # {}

"""
三、调用dict的方法fromKeys
    调用该方法时通过参数指定所有的Key,所有value的默认值都为None。
"""
print(dict.fromkeys(['name', 'age']))  # {'name': None, 'age': None}
print(dict.fromkeys(('name', 'age')))  # {'name': None, 'age': None}
"""
   调用该方法时可以通过参数指定所有value的值。
"""
print(dict.fromkeys(['name', 'age'], 'N/A'))  # {'name': 'N/A', 'age': 'N/A'}



