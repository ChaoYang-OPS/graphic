"""原始字符串"""
"""
    如果不想让字符串的转义字符生效，可以在字符串的前面添加r或者R，
    从而将字符串声明为原始字符串。
"""
print(r'\tC:\\Program Files')  # \tC:\\Program Files
print(R'\tC:\\Program Files')  # \tC:\\Program Files
"""
  原始字符串最后一个字符不能是反斜杠（最后两个字符都是反斜杠除外）
"""
# print(r'Hello World\')
print(r'Hello World\\')  # Hello World\\
# 解释器不会把r'What\'看做是一个原始字符串，因为原始字符串不能以反斜杠结尾
print(r'What\'s you name')
# 解释器会把r'What\\' 看做是一个原始字符串，因为原始字符串可以以两个反斜杠结尾
# print(r'What\\'s you name')
