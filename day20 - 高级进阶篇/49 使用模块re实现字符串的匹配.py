"""使用模块re实现字符串的匹配"""

"""
   如果想要判断给定的字符串和正则表达式是否是匹配的，可以使用模块re提供的方法:
match(pattern, string[, flags])
    该方法会根据参数string指定的字符串与参数pattern指定的正则表达式进行匹配。
    其中，
        参数pattern是一个正则表达式，或对正则表达式预编译之后得到的对象。
        参数flags是一个标志位，用于控制正则表达式的匹配方法，如： 是否区分大小写、多行匹配等。
            如果需要同时使用多个标志位，可以使用|对标志位进行分隔。
    
    该方法会从参数string指定的字符串的开头开始，一直向后尝试匹配参数pattern指定的正则表达式，
在到达pattern的末尾前，如果遇到了无法匹配的字符或到达了string的末尾，都表示匹配失败，从而返回None。 
否则，当到达pattern的末尾时，如果所有的字符都是匹配成功的，则表示匹配成功，从而终止匹配，不再对
string向后匹配，同时，返回一个Match对象。

    根据方法match()返回值可知,常见的判断方式为:
if re.match(正则表达式，被匹配的字符串):
    print('匹配成功')
else:
    print('匹配失败')
"""

import re



print(re.match(r'...', 'a\nc'))  # None


print(re.match(r'...', 'ab'))  # None

print(re.match(r'...', 'abc'))  # <re.Match object; span=(0, 3), match='abc'>

print(re.match(r'...', 'abcdef'))  # <re.Match object; span=(0, 3), match='abc'>



print(re.match(r'[a-z]{7}', 'aBCdefG', re.I))
# <re.Match object; span=(0, 7), match='aBCdefG'>

print(re.match(r'...[a-z]{7}', 'a\ncaBCdefG', re.I|re.S))
# <re.Match object; span=(0, 10), match='a\ncaBCdefG'>

