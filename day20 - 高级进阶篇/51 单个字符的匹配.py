# -*- coding: utf-8 -*-
"""单个字符的匹配"""

"""

"""

import re

# <re.Match object; span=(0, 3), match='c-8'>
print(re.match(r'...', 'c-8')) 

print(re.match(r'...', 'c\n8'))  # None
# <re.Match object; span=(0, 3), match='c\n8'>
print(re.match(r'...', 'c\n8', re.S)) 


print(re.match(r'\d\d\d', '123abc'))

print(type(re.match(r'\d\d\d', '123abc')))


print(re.match(r'\D\D\D', '123abc'))  # None
# <re.Match object; span=(0, 3), match='a-b'>
print(re.match(r'\D\D\D', 'a-b123'))  

# <re.Match object; span=(0, 3), match='c_8'>
print(re.match(r'\w\w\w', 'c_8###'))  
# <re.Match object; span=(0, 3), match='@-#'>
print(re.match(r'\W\W\W', '@-#c_8'))
# <re.Match object; span=(0, 6), match=' \t\r\n\x0c\x0b'>
print(re.match(r'\s\s\s\s\s\s', ' \t\r\n\f\vabc'))
# <re.Match object; span=(0, 3), match='c-3'>
print(re.match(r'\S\S\S', 'c-3 \t'))

# <re.Match object; span=(0, 1), match='b'>
print(re.match(r'[abc]', 'b'))
# <re.Match object; span=(0, 1), match='f'>
print(re.match(r'[^abc]', 'f'))
# <re.Match object; span=(0, 1), match='M'>
print(re.match(r'[a-zA-Z]', 'M'))
# <re.Match object; span=(0, 1), match='k'>
print(re.match(r'[a-n&h-t]', 'k'))