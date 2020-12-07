"""字符串的排序"""
"""
   与列表不同的是，字符串是不可变类型，因此，如果想对字符串的所有字符进行排序，
不存在方法sort，只能调用内置函数sorted。
"""

s = 'DBeFac'
print(sorted(s))  # ['B', 'D', 'F', 'a', 'c', 'e']
print(sorted(s, reverse=True))  # ['e', 'c', 'a', 'F', 'D', 'B']
"""
  调用内置函数sorted时，还可以指定参数key =  函数名 或  key = 类名.方法名,
这样会对字符串中的所有字符分别调用指定的函数或方法，然后按照函数或方法的返回值进行排序，
从而自定义排序规则。
"""
print(sorted(s, key=str.lower))  # ['a', 'B', 'c', 'D', 'e', 'F']

"""
  调用内置函数sorted时的参数key同样适用于列表和元组。
"""
L = ['Python', 'java', 'Swift']

print(sorted(L, key = len))  # ['java', 'Swift', 'Python']

print(sorted(L, key = str.lower))  # 'java', 'Python', 'Swift']

"""
   调用列表的方法sort时，也可以指定参数key。
"""
L = ['Python', 'java', 'Swift']
L.sort(key=len)
print(L)  # ['java', 'Swift', 'Python']
L.sort(key = str.lower)
print(L)  # ['java', 'Python', 'Swift']