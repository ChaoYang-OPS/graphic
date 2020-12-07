"""使用比较运算符比较两个字符串"""
"""
    除了使用比较运算符对两个列表或元组进行比较，还可以使用如下比较运算符对两个字符串进行比较:
>
>=
<=
<
==
!=
    比较规则为： 首先比较两个字符串的第一个字符，如果相等则继续比较下一个字符，依次比较下去，
直到两个字符串中的字符不相等时其比较结果就是两个字符串比较结果，
两个字符串中的所有后续字符将不再被比较。
    两个字符进行比较时，比较的是其ordinal value。调用内置函数ord可以得到指定字符的
ordinal value。与内置函数ord对应的是内置函数chr，调用内置函数chr时指定ordinal value
可以得到其对应的字符。
"""
print(ord('a'))  # 97
print(chr(97))   # a
print(ord('b'))  # 98
print(chr(98))   # b
print(ord('A'))  # 65
print(chr(65))   # A

print('a' < 'b')  # True
print('a' > 'A')  # True
print('cbadf' > 'cbAeg')  # True

"""
    还可以使用is对两个字符串进行比较。
    ==与is的区别: ==是"相等性"测试， is是"同一性"测试
    字符串常量会被缓存和重用。
"""
a = b = 'Hello'
c = 'Hello'
print(a == b)  # True
print(a == c)  # True
print(a is b)  # True
print(a is c)  # True