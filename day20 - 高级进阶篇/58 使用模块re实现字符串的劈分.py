"""使用模块re实现字符串的劈分"""

"""
    当对字符串进行劈分时，借助模块re并通过正则表达式指定劈分符可以实现更强大的劈分功能。
模块re提供了实现字符串劈分的方法:
split(pattern, string[,maxsplit=0][,flags])
    该方法会根据参数pattern指定的劈分符对参数string指定的字符串进行劈分。
    其中，参数maxsplit用于指定最大劈分次数;默认值是0，表示不限制劈分次数。
    方法的返回值是劈分后的所有子串组成的列表。

"""
import re

# ['a', 'b', 'c', 'd']
print(re.split(r'\s+', 'a  b     c   d'))
# ['a', 'b', 'c   d']
print(re.split(r'\s+', 'a  b     c   d', 2))
# ['a', 'b', 'c', 'd', 'e']
print(re.split(r'[\s\,\;]+', 'a,  b;; c, ;d, e'))


"""
    除了直接调用模块re的方法split()之外，也可以调用模块re的方法compile()的返回值的方法:
split(string[,maxsplit])。
    模块re的方法split()中的参数pattern和flags被转移到了方法compile()中。
"""

pattern = re.compile(r'\s+')
# ['a', 'b', 'c', 'd']
print(pattern.split('a  b     c   d'))

# ['a', 'b', 'c   d']
print(pattern.split('a  b     c   d', 2))