"""字符串的查操作"""
"""
   因为字符串可以看做是字符的列表，所以字符串与列表的"查"操作是类似的，区别在于：
当获得字符串中指定子串的索引时，除了调用方法index,还可以调用方法find、rfind、rindex。
其中，子串的索引指的是子串中第一个字符的索引。
"""
"""
当字符串存在多个被查找的子串时，方法index和find返回第一个子串的索引，
方法rindex和rfind返回最后一个字串的索引。
"""
s = '5739182186'
print(s.index('18'))  # 4
print(s.find('18'))  # 4
print(s.rindex('18'))  # 7
print(s.rfind('18'))  # 7

"""
  当字符串中不存在指定的子串时，方法index和rindex抛出ValueError，方法find和rfind返回-1。
"""
# print(s.index('18', 1, 5))  # ValueError: substring not found
# print(s.rindex('18', 1, 5))  # ValueError: substring not found

print(s.find('18', 1, 5))  # -1
print(s.rfind('18', 1, 5))  # -1
