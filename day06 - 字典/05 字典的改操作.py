"""字典的改操作"""
"""
  如果想要修改字典中指定的key对应的value，常见的方式有两种:
一、 为已经存在的key赋予一个新的value值(一次只修改一个key对应的value)
"""
d = {'name': 'jack', 'age': 18, 'gender': '男'}
d['age'] = 20
print(d)  # {'name': 'jack', 'age': 20, 'gender': '男'}
"""
二、调用方法update(一次至少修改一个key对应的value)
"""
# d.update({'name': 'Mike', 'age': 20})
# d.update([('name', 'Mike'), ('age', 20)])
d.update(name='Mike', age=20)
print(d)  # {'name': 'Mike', 'age': 20, 'gender': '男'}
