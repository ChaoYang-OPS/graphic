"""字典生成式"""
"""
一、 什么是字典生成式
"""

items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 83]
"""
    如果想要生成字典{'FRUITS': 96, 'BOOKS': 78, 'OTHERS': 83}，可以使用for-in循环:
"""
d = {}
for item, price in zip(items, prices):
    d[item.upper()] = price
print(d)  # {'FRUITS': 96, 'BOOKS': 78, 'OTHERS': 83}

"""
    上述的解决方案有更好的替代，那就是使用字典生成式。
    字典生成式的语法格式:
{表示字典key的表达式: 表示字典value的表达式
    for 自定义的表示key的变量，自定义的表示value的变量 in 可迭代对象}
其中, "表示字典key的表达式"中通常包含"自定义的表示key的变量"，"表示字典value的表达式"中
通常包含"自定义的表示value的变量"
    字典生成式的使用场景: 凡是可以通过for-in循环创建的字典，都可以使用字典生成式来创建。
"""
d = {item.upper(): price for item, price in zip(items, prices)}
# {'FRUITS': 96, 'BOOKS': 78, 'OTHERS': 83}
print(d)

"""
二、在字典生成式中使用if语句
    可以在字典生成式的for-in循环后添加if语句.
"""
d = {item.upper(): price
     for item, price in zip(items, prices)
     if price > 80}
print(d)  # {'FRUITS': 96, 'OTHERS': 83}

"""
三、在字典生成式中使用双重for-in循环
"""
d = {i: j for i in range(1, 4) for j in range(1, 4)}
print(d)  # {1: 3, 2: 3, 3: 3}

# 以上代码相当于:
d = {}
for i in range(1, 4):
    for j in range(1, 4):
        d[i] = j
print(d)  # {1: 3, 2: 3, 3: 3}

# 即使用双重for-in循环，又使用if语句
d = {i: j for i in range(1, 4) for j in range(1, 4) if i != j}
print(d)  # {1: 3, 2: 3, 3: 2}
