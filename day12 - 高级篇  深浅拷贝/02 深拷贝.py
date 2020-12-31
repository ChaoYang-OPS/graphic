"""深拷贝"""
"""
    可以调用标准库模块copy中的函数deepcopy()实现深拷贝
"""
import copy

i = 18
ic = copy.deepcopy(i)
print(ic)
print('id(i):{}'.format(id(i)))  # id(i):4480806112
print('id(ic):{}'.format(id(ic)))  # id(ic):4480806112

t = (1, 2, 3)
tc = copy.deepcopy(t)
print(tc)
print('id(t):{}'.format(id(t)))  # id(t):4483659072
print('id(tc2):{}'.format(id(tc)))  # id(tc2):4483659072
"""
    所谓深拷贝,指的是: 对于某个对象，创建与该对象具有相同值的另一个对象，同时，这两个对象
内部嵌套的对应可变子对象全都不是同一个对象。简单地说，外部和内部都进行了拷贝。
"""
L1 = [[3, 6], 8]
L2 = copy.deepcopy(L1)
print(L2)

print('id(L1):{}'.format(id(L1)))
print('id(L2):{}'.format(id(L2)))

print('id(L1[0]):{}'.format(id(L1[0])))
print('id(L2[0]):{}'.format(id(L2[0])))

print('id(L1[1]):{}'.format(id(L1[1])))
print('id(L2[1]):{}'.format(id(L2[1])))

L1[0][1] = 7
L1[1] = 9
print(L1)  # [3, 7], 9]
print(L2)  # [[3, 6], 8]
"""
    如果不可变对象内部又嵌套的可变子对象，深拷贝之后，会创建一个与该不可变对象具有相同值的另一个对象。
"""

t1 = ([3, 6], 8)
t2 = copy.deepcopy(t1)
print(t2)

print('id(t1):{}'.format(id(t1)))  # id(t1):4455928448
print('id(t2):{}'.format(id(t2)))  # id(t2):4455923136

print('id(t1[0]):{}'.format(id(t1[0])))  # id(t1[0]):4455949440
print('id(t2[0]):{}'.format(id(t2[0])))  # id(t2[0]):4455950272

print('id(t1[1]):{}'.format(id(t1[1])))  # id(t1[1]):4452383648
print('id(t2[1]):{}'.format(id(t2[1])))  # id(t2[1]):4452383648