"""Match对象的属性和方法"""

"""
    模块re的方法match()和search()在匹配成功时都会返回一个Match对象，该对象包含了很多关于此次匹配的信息，
可以通过访问Match对象提供的属性和方法来获取这些匹配信息。
"""

import re

match_obj = re.compile(r'(\d+)-(?P<sec>\d+)').match('025-3456abc', 1, 7)
# <re.Match object; span=(1, 7), match='25-345'>
print(match_obj)
# 025-3456abc
print(match_obj.string)
# re.compile('(\\d+)-(?P<sec>\\d+)')
print(match_obj.re)

# 
print(match_obj.pos)  # 1

print(match_obj.endpos) # 7

print(match_obj.lastindex)  # 2

print(match_obj.lastgroup)  # sec


print(match_obj.group(2))  # 345

print(match_obj.group('sec'))  # 345

print(match_obj.group(0))  # 25-345

print(match_obj.group())  # 25-345

print(match_obj.group(1, 'sec'))  # ('25', '345')

print(match_obj.groups())  # ('25', '345')

print(match_obj.groupdict())  # {'sec': '345'}

print(match_obj.start('sec'))  # 4

print(match_obj.start())  # 1


print(match_obj.end('sec'))  # 7

print(match_obj.end())  # 7

print(match_obj.span('sec'))  # (4, 7)