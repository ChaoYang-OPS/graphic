"""去除字符串前导字符或后续字符"""
"""
  如果想去除字符串的前导字符串或后续字符串，可以调用以下方法：
1、lstrip: 去除字符串的前导字符串。
2、rstrip: 去除字符串的后续字符串。
3、strip: 去除字符串的前导字符串和后续字符串。
其中，默认的前导字符串和后续字符串都是空格字符串。
"""
s = '      Hello World     '
print(s.lstrip())  # Hello World
print(s.rstrip())  #    Hello World
print(s.strip())  # Hello World

"""
   调用以上三个方法时可以指定一个字符串，这样，
前导字符串指的是: 从左边第1个字符开始依次往后，直到某个字符不在指定的字符串中。
后续字符串指的是：从右边最后1个字符开始依次往前，直到某个字符不在指定的字符串中。
"""
s = 'www.example.com'
print(s.lstrip('cmowz.'))  # example.com
print(s.rstrip('cmowz.'))  # www.example
print(s.strip('cmowz.'))   # example