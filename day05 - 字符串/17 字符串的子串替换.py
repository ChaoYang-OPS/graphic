"""字符串的子串替换"""
"""
    如果想将字符串中的某个子串替换为指定的字符串，可以调用方法replace.
该方法的第1个参数指定被替换的子串，第2个参数指定替换子串的字符串。
该方法返回替换后得到的字符串，替换前的字符串不发现变化。
"""
s = 'Hello-Hello-Hello'
print(s.replace('Hello', 'Hi'))  # Hi-Hi-Hi
print(s)  # Hello-Hello-Hello
"""
  调用该方法时可以通过第3个参数指定最大替换次数。
"""
print(s.replace('Hello', 'Hi', 2))  # Hi-Hi-Hello
print(s)  # Hello-Hello-Hello
