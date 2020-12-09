"""为字典中指定的key设置默认的value值"""
"""
    为了确保字典中指定的key总是存在的，可以调用方法setdefault，这样，
1、如果字典中存在指定的key,该方法返回指定的key对应的value，字典不发生变化。
2、如果字典中不存在指定的key，该方法返回指定的默认value值，字典中添加一个key-value对:
"指定的key: 指定的默认value值"。此时，调用方法setdefault相当于语句: if ...not in ...。
"""
d = {'name': 'Jack'}
print(d.setdefault('name', 'defaultName'))  # Jack
print(d)  # {'name': 'Jack'}

d = {}
print(d.setdefault('name', 'defaultName'))  # defaultName
print(d)  # {'name': 'defaultName'}
# if 'name' not in d:
#     d['name'] = 'defaultName'
