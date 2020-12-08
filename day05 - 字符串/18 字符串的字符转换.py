"""字符串的字符转换"""
"""
  如果想对字符串中的某些字符进行转换，可以调用方法maketrans和translate。
首先调用方法maketrans创建一个转换表，然后把创建的转换表作为参数传给方法translate。
"""
table = str.maketrans('bcd', '234')
# table = str.maketrans({'b': '2', 'c': '3', 'd': '4'})
# table = str.maketrans({98: 50, 99: 51, 100: 52})
print(table)  # {98: 50, 99: 51, 100: 52}
print(ord('b'))  # 98
print(ord('2'))  # 50
print(ord('c'))  # 99
print(ord('3'))  # 51
print(ord('d'))  # 100
print(ord('4'))  # 52

s = 'incredible'
print(s.translate(table))  # in3re4i2le
"""
  在调用方法maketrans创建转换表时，还可以指定要删除的所有字符。
"""
table = str.maketrans('bcd', '234', 'ie')
print(table)  # {98: 50, 99: 51, 100: 52, 105: None, 101: None}

print(s.translate(table))  # n3r42l

# 不转换，只指定要删除的所有字符
table = str.maketrans('', '', 'ie')
print(table)  # {105: None, 101: None}
print(s.translate(table))  # ncrdbl
