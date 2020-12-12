"""并行遍历"""
"""
    有时可能需要同时遍历多个可迭代对象，也就是并行遍历。例如: 列表names中存放姓名,
列表ages中存放对应的年龄。如果想同时遍历这两个列表，打印出所有的姓名及对应的年龄，可以这样实现:
"""
names = ['Jack', 'Mike', 'Tom']
ages = [16, 32, 43]

for i in range(len(names)):
    print(names[i], '的年龄是:', ages[i])
'''
Jack 的年龄是: 16
Mike 的年龄是: 32
Tom 的年龄是: 43
'''

"""
    上述的解决方案有更好的替代。如果需要同时遍历多个可迭代对象，可以调用内置函数zip(类zip的构造方法)
将多个可迭代对象打包压缩成zip对象。
"""
print(zip(names, ages))  # <zip object at 0x10138cf00>
"""
    为了清楚地表示返回的zip对象所表示的内容，可以将zip对象转换成列表。
"""
# 列表中的元素都是元组，元组中的第i个元素来自调用zip时的第i个参数
print(list(zip(names, ages)))  # [('Jack', 16), ('Mike', 32), ('Tom', 43)]
"""
    既可以遍历zip对象转换后的列表，也可以直接遍历zip对象。
"""
for name, age in list(zip(names, ages)):
    print(name, '的年龄是:', age)

for name, age in zip(names, ages):
    print(name, '的年龄是:', age)

"""
    调用内置函数zip将多个可迭代对象进行打包压缩时，如果两个可迭代对象的长度不同，
那么较长的可迭代对象会截断。
"""
print(list(zip(range(3), range(5))))  # [(0, 0), (1, 1), (2, 2)]

"""
    可以使用*对zip对象解压缩
"""
x = [1, 2, 3]
y = [4, 5, 6]
print(list(zip(x, y)))  # [(1, 4), (2, 5), (3, 6)]

print(list(zip(*zip(x, y))))  # [(1, 2, 3), (4, 5, 6)]

x2, y2 = zip(*zip(x, y))
print(list(x2))  # [1, 2, 3]
print(list(y2))  # [4, 5, 6]