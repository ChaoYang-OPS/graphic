"""字符串的大小写转换"""
"""
  如果想要对字符串中某些字符的大小写进行转换，可以调用字符串的以下方法:
1、 upper: 把所有字符全部转换为大写。
2、 lower: 把所有字符全部转换为小写。
3、 swapcase: 把所有小写字符转换为大写，把所有大写字符转换为小写。
4、 capitalize: 把第一个字符转换为大写，把其余字符转换为小写。
5、 title: 把每个单词的第一个字符转换为大写，把每个单词的剩余字符转换为小写。
"""

s = 'he is learning PYTHON'
print(s.upper())  # HE IS LEARNING PYTHON
print(s.lower())  # he is learning python
print(s.swapcase())  # HE IS LEARNING python
print(s.capitalize())  # He is learning python
print(s.title())  # He Is Learning Python

"""
   如果想要判断字符串中某些字符的大小写，可以调用字符串的以下方法:
1、 isupper: 是否所有字符全为大写。
2、 islower: 是否所有字符全为小写。
3、 istitle: 是否每个单词的第一字符为大写并且每个单词的剩余字符为小写。
"""
print(s.isupper())  # False
print(s.upper().isupper())  # True
print(s.islower())  # False
print(s.lower().islower())  # True
print(s.istitle())  # False
print(s.title().istitle())  # True
