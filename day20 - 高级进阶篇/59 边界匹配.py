"""边界匹配"""

"""
    边界匹配主要用于匹配字符串的边界或字符串中单词的边界。
"""

import re

# ['12', '3', '45', '6', '78', '9']
print(re.findall(r'\d+', '12-3\n45-6\n78-9\n'))
# ['12']
print(re.findall(r'^\d+', '12-3\n45-6\n78-9\n'))

# ['12', '45', '78']
print(re.findall(r'^\d+', '12-3\n45-6\n78-9\n', re.M))
# ['12']
print(re.findall(r'\A\d+', '12-3\n45-6\n78-9\n', re.M))

# ['9']
print(re.findall(r'\d+$', '12-3\n45-6\n78-9\n'))
# ['3', '6', '9']
print(re.findall(r'\d+$', '12-3\n45-6\n78-9\n', re.M))  
# []
print(re.findall(r'\d+\Z', '12-3\n45-6\n78-9\n', re.M))  
# ['9']
print(re.findall(r'\d+\Z', '12-3\n45-6\n78-9', re.M))
# ['py']
print(re.findall(r'\bpy\b', 'ab py cd' ))
# ['py']
print(re.findall(r'\bpy\b', 'ab#py@cd' ))
# ['py', 'py']
print(re.findall(r'\bpy\b', 'py cd py' ))
# ['pybc']
print(re.findall(r'\Bpy\w+', 'apy apybc pyb' ))
