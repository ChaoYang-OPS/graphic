"""贪婪匹配与勉强匹配"""

"""
    贪婪匹配: 在匹配正则表达式时，使用尽可能长的子串去匹配。
    勉强匹配: 在匹配正则表达式时，使用尽可能短的子串去匹配。
"""

import re

# <re.Match object; span=(0, 6), match='abbbbb'>
print(re.match(r'ab*', 'abbbbbc'))
# <re.Match object; span=(0, 1), match='a'>
print(re.match(r'ab*?', 'abbbbbc'))



# <re.Match object; span=(0, 6), match='abbbbb'>
print(re.match(r'ab+', 'abbbbbc'))
# <re.Match object; span=(0, 2), match='ab'>
print(re.match(r'ab+?', 'abbbbbc'))


# <re.Match object; span=(0, 2), match='ab'>
print(re.match(r'ab+?', 'abbbbbc'))
# <re.Match object; span=(0, 2), match='a'>
print(re.match(r'ab??', 'abbbbbc'))


# <re.Match object; span=(0, 4), match='abbb'>
print(re.match(r'ab{3}', 'abbbbbc'))
# <re.Match object; span=(0, 4), match='abbb'>
print(re.match(r'ab{3}?', 'abbbbbc'))


# <re.Match object; span=(0, 6), match='abbbbb'>
print(re.match(r'ab{3,}', 'abbbbbc'))
# <re.Match object; span=(0, 4), match='abbb'>
print(re.match(r'ab{3,}?', 'abbbbbc'))


# <re.Match object; span=(0, 6), match='abbbbb'>
print(re.match(r'ab{3,5}', 'abbbbbc'))
# <re.Match object; span=(0, 4), match='abbb'>
print(re.match(r'ab{3,5}?', 'abbbbbc'))