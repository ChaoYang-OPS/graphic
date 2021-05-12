"""使用模块re实现字符串的替换"""

"""
    当在字符串中替换指定的子串时，借助模块re并通过正则表达式指定被替换的子串可以实现功能更加强大
的替换功能。
    模块re提供了两个用于实现字符串替换的方法:
一、sub(pattern, repl, string[,count][,flags])
    该方法会将参数string指定的字符串中所有匹配参数pattern的子串替换为参数repl指定的字符串。
    其中，参数count用于指定最大替换次数；默认值是0，表示替换所有的匹配。
    方法的返回值是替换后得到的字符串。
"""

import re

# -888-888-888-
print(re.sub(r'\d+', '888', '-123-56-89-'))
# -888-888-89-
print(re.sub(r'\d+', '888', '-123-56-89-', 2))

"""
    参数repl除了可以指定为替换的字符串之外，还可以指定为一个函数。通过该函数，可以把每次匹配
对应的Match对象作为函数的输入(参数)，在函数体中对匹配到的子串进行处理，函数的输出(返回值)
作为替换的字符串。
"""
def add1(match):
    val = match.group()
    num = int(val) + 1
    return str(num)


# -124-57-90-
print(re.sub(r'\d+',add1, '-123-56-89-'))

"""
    当替换字符串为空字符串时，可以实现字符串中子串的删除。
"""
# HLL wrld
print(re.sub(r'[aeiou]', '', 'HELLO world', flags=re.I))

"""
二、 subn(pattern, repl, string, [,count][,flags])
    返回值是包含两个元素的元组:(对应的方法sub()的返回值,替换次数)
"""

# ('-124-57-90-', 3)
print(re.subn(r'\d+', add1, '-123-56-89-'))

"""
    除了直接调用模块re的方法sub()和subn()之外，也可以调用模块re的方法compile()的返回值的方法
sub(repl,string[, count])
subn(repl,string[, count])
    模块re的方法sub()和subn()中参数pattern和flags被转移到了方法compile()中。
"""

pattern = re.compile(r'\d+')
# -888-888-888-
print(pattern.sub('888', '-123-56-89-'))
# -124-57-90-
print(pattern.sub(add1, '-123-56-89-'))
# ('-124-57-90-', 3)
print(pattern.subn(add1, '-123-56-89-'))