"""字符串是不可变类型"""
"""
  字符串没有"改操作"、"增"操作和"删"操作，因为字符串是不可变类型。
"""
s = 'Hello, World'
# s[5] = '!'  # TypeError: 'str' object does not support item assignment

print(s[:5] + '!' + s[6:])  # Hello! World
