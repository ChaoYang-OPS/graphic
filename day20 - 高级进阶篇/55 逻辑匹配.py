"""逻辑匹配"""

"""
    在正则表达式中可以使用|进行逻辑匹配，其匹配规则是:
先尝试匹配左边的表达式，如果匹配成功，则跳过匹配右边的表达式；如果匹配不成功，再匹配右边的表达式。
    如果|没有被包括在()中，则它的作用范围是整个正则表达式。
"""
import re

# <re.Match object; span=(0, 3), match='123'>
print(re.match(r'123|12', '123'))

# <re.Match object; span=(0, 2), match='12'>
print(re.match(r'abc|12', '123'))
# <re.Match object; span=(0, 6), match='Python'>
print(re.match(r'P(ython|erl)', 'Python'))
# <re.Match object; span=(0, 4), match='Perl'>
print(re.match(r'P(ython|erl)', 'Perl'))