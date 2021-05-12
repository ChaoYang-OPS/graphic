"""分组匹配"""

"""
    可以使用小括号()将正则表达式中的部分内容括起来，从而将该部分内容作为一个分组。
    从正则表达式的左边往右数，第一个左小括号表示第1个分组，第二个左小括号表示第2个分组, ....,
依次类推。因此，可以根据编号对分组进行引用。
"""

import re

matchobj = (re.match(r'(\d+)-(\d+)', '025-3456abc'))
# <re.Match object; span=(0, 8), match='025-3456'>
print(matchobj)

print(matchobj.group(1))  # 025

print(matchobj.group(2))  # 3456
# 第0个分组表示被匹配到的子串
print(matchobj.group(0))  # 025-3456

# 所有分组组成的元组
print(matchobj.groups())  # ('025', '3456')


"""
    可以给某个分组起一个别名，其语法格式为: ?P<别名>。 这样，就可以通过别名对分组进行引用了。
"""

matchobj = (re.match(r'(?P<fir>\d+)-(?P<sec>\d+)', '025-3456abc'))
# <re.Match object; span=(0, 8), match='025-3456'>
print(matchobj)

print(matchobj.group('fir'))  # 025

print(matchobj.group('sec'))  # 3456

"""
    在正则表达式中，也可以根据编号或别名对分组进行引用，其语法格式分别为:
\编号
?P=别名
    确切地说，是引用分有匹配到的子串。
"""
# <re.Match object; span=(0, 13), match='025-3456-3456'>
print(re.match(r'(\d+)-(\d+)-(\2)', '025-3456-3456'))
# <re.Match object; span=(0, 13), match='025-3456-3456'>
print(re.match(r'(\d+)-(?P<sec>\d+)-(?P=sec)', '025-3456-3456'))