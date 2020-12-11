"""带索引的序列遍历"""

"""
带索引的序列遍历
"""

L = ['java', 'Python', 'Swift', 'Kotlin']
"""
    如果在遍历序列的过程中需要访问元素的索引，有以下几种实现方式
一、第1种实现方式
"""
index = 0
for item in L:
    print('L[{}] = {}'.format(index, item))
    index += 1

"""
二、第2种实现方式
"""
for index in range(len(L)):
    print('L[{}] = {}'.format(index, L[index]))

"""
三、第3种实现方式
"""
index = 0
while index < len(L):
    print('L[{}] = {}'.format(index, L[index]))
    index += 1
"""
运行结果:
L[0] = java
L[1] = Python
L[2] = Swift
L[3] = Kotlin
"""
"""
四、 第4种实现方式
    可以调用内置函数enumerate(类enumerate的构造方法)将要遍历的序列转换为enumerate对象。
"""
print(enumerate(L))  # <enumerate object at 0x10cd76f40>
"""
    为了清楚地表示返回的enumerate对象所表示的内容，可以将enumerate对象转换为列表
"""
# [(0, 'java'), (1, 'Python'), (2, 'Swift'), (3, 'Kotlin')]
print(list(enumerate(L)))
"""
    在调用内置函数enumerate时，可以通过第二个参数来指定索引的起始值。
"""
# [(1, 'java'), (2, 'Python'), (3, 'Swift'), (4, 'Kotlin')]
print(list(enumerate(L, 1)))
"""
    既可以遍历enumerate对象转换后的列表，也可以直接遍历enumerate对象。
"""
for index, item in list(enumerate(L)):
    print('L[{}] = {}'.format(index, item))

for index, item in enumerate(L):
    print('L[{}] = {}'.format(index, item))
