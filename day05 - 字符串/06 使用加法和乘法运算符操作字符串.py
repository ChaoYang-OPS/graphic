"""使用加法和乘法运算符操作字符串"""
"""
一、使用加法运算符操作字符串
     可以使用加法运算符连接后生成一个新字符串
"""
print('Hello,' + 'World!')  # Hello,World!
"""
   此外，把多个字符串常量放在一起就会自动连接然后生成一个新字符串。
"""
s = 'Hello' ',' 'World' '!'
print(s)  # Hello,World!
"""
  如果想把多个字符串常量写在多行中，可以在每行的末尾添加一个反斜杠。
"""
s = 'Hello' ','\
        'World' \
        '!'
print(s)  # Hello,World!

"""
二、 使用乘法运算符操作字符串
     可以使用乘法运算符将字符串中的字符重复n次后生成一个新字符串。
"""
print('Hello' * 3)  # HelloHelloHello
