"""字典的删操作"""
"""
    如果想要删除字典中的key-value对，常见的方式有四种:
一、 调用方法pop(一次只删除一个指定key的key-value对)
     该方法返回指定的key对应的value。
"""
d = {'name': 'jack', 'age': 18, 'gender': '男'}
print(d.pop('age'))  # 18
print(d)  # {'name': 'jack', 'gender': '男'}
"""
  如果指定的key不存在，抛出KeyError。
"""
"""
  为了防止指定的key不存在时抛出KeyError,可以通过参数指定一个默认返回的value。
"""
# d.pop('score')  # KeyError: 'score'
print(d.pop('score', 90))  # 90
# print(d.pop('score', '删除的key不存在'))  # 删除的key不存在
"""
二、 使用del语句(一次只删除一个指定key的key-value对)
"""
d = {'name': 'jack', 'age': 18, 'gender': '男'}
del d['age']
print(d)  # {'name': 'jack', 'gender': '男'}

"""
三、调用方法popitem(一次只删除一个任意的key-value对)
  该方法返回被删除的key-value对。
"""
d = {'name': 'jack', 'age': 18, 'gender': '男'}
print(d.popitem())  # ('gender', '男')
print(d)  # {'name': 'jack', 'age': 18}
"""
四、调用方法clear清空字典
"""
d = {'name': 'jack', 'age': 18, 'gender': '男'}
d.clear()
print(d)  # {}



