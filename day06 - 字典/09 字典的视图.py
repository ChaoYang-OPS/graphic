"""字典的视图"""
"""
一、 得到字典相关视图的三个方法:
    1、 keys: 返回字典所有key的视图
    2、 values: 返回字典所有value的视图。
    3、 items: 返回字典所有key-value对的视图
"""
d = {'name': 'jack', 'age': 18}
keys = d.keys()
print(keys)  # dict_keys(['name', 'age'])
print(list(keys))  # ['name', 'age']
values = d.values()
print(values)  # dict_values(['jack', 18])
print(list(values))  # ['jack', 18]
items = d.items()
print(items)  # dict_items([('name', 'jack'), ('age', 18)])
print(list(items))  # [('name', 'jack'), ('age', 18)]
"""
二、 视图会随字典的变化而随之变化
"""
d.pop('age')
print(d)  # {'name': 'jack'}
print(keys)  # dict_keys(['name'])
print(values)  # dict_values(['jack'])
print(items)  # dict_items([('name', 'jack')])