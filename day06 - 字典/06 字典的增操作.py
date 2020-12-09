"""字典的"增"操作"""
"""
    如果想要往字典中添加key-value对，常见的方式有两种:
一、为不存在的key赋予一个value值(一次只添加一个key-value对)
"""
d = {'name': 'Jack', 'age': 18}
d['gender'] = '男'
print(d)  # {'name': 'Jack', 'age': 18, 'gender': '男'}

"""
二、调用方法update(一次至少添加一个key-value对)
"""
d = {'name': 'Jack', 'age': 18}
# d.update({'gender': '男', 'score': 90})
# d.update([('gender', '男'), ('score', 90)])
d.update(gender= '男',  score = 90)
print(d)  # {'name': 'Jack', 'age': 18, 'gender': '男', 'score': 90}
