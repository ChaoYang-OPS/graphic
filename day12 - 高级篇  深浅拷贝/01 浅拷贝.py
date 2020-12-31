"""浅拷贝"""

"""
    对于某个对象，如何创建它的拷贝呢？也就是说，如何创建与该对象具有相同值的另一个对象呢？
"""
"""
    所谓浅拷贝，指的是: 对于某个对象，虽然创建了与该对象具有相同值的另一个对象，但是，这两个对象
内部嵌套的对应子对象全都是同一个对象。简单地说，外部进行了拷贝，内部没有拷贝。
    以下方式得到的拷贝都是浅拷贝:
1、 切片操作[:]
2、 调用列表、字典、集合的方法copy()
3、 调用内置函数list()、dict()、set()
4、 调用标准库模块copy中的函数copy()
"""
L1 = [[3, 6], 8]
# L2 = L1[:]
# L2 = L1.copy()
# L2 = list(L1)
import copy  # 导入标准库模块copy
L2 = copy.copy(L1)  # 调用标准库模块copy中的函数copy()
print(L2)  # [[3, 6], 8]

print('id(L1):{}'.format(id(L1)))  # id(L1):4560360640
print('id(L2):{}'.format(id(L2)))  # id(L2):4560838016

print('id(L1[0]):{}'.format(id(L1[0])))  # id(L1[0]):4450251456
print('id(L2[0]):{}'.format(id(L2[0])))  # id(L2[0]):4450251456

print('id(L1[1]):{}'.format(id(L1[1])))
print('id(L2[1]):{}'.format(id(L2[1])))


L1[0][1] = 7
L1[1] = 9
print(L1)  # [[3, 7], 9]
print(L2)  # [[3, 7], 8]

"""
    对于没有嵌套子对象的不可变对象，例如:整数对象、字符串对象和元组对象等，不会进行拷贝，也就是说，
不会创建另一个对象。
"""

i = 18
ic1 = int(i)
print(ic1)  # 18
print('id(i):{}'.format(id(i)))  # id(i):4354686176
print('id(ic1):{}'.format(id(ic1)))  # id(ic1):4354686176

ic2 = copy.copy(i)
print(ic2)  # 18
print('id(ic2):{}'.format(id(ic2)))  # id(ic2):4354686176

t = (1, 2, 3)
tc1 = tuple(t)
print(tc1)  # (1, 2, 3)

print('id(t):{}'.format(id(t)))  # id(t):4512810176
print('id(tc1):{}'.format(id(tc1)))  # id(tc1):4512810176

tc2 = copy.copy(t)
print(tc2)
print('id(t):{}'.format(id(t)))  # id(t):4400313664
print('id(tc2):{}'.format(id(tc2)))  # id(tc2):4400313664