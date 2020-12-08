"""字符串的对齐"""
"""
  如果想要设置字符串的对齐方式，可以调用字符串的以下方法:
1、 center: 中心对齐
2、 ljust: 左对齐
3、 rjust: 右对齐
这三个方法都可以接收两个参数，其中，
第1个参数指定字符串的宽度。如果指定的宽度小于等于字符串的长度，返回字符串本身。
第2个参数指定填充字符，且第2个参数是可选的，其默认值是空格。
"""
print('HelloWorld'.center(18, '*'))  # ****HelloWorld****
print('HelloWorld'.center(18))  #   HelloWorld
print('HelloWorld'.center(8))  # HelloWorld
print('---------'.center(18, '*'))
print('HelloWorld'.ljust(18, '*'))  # HelloWorld********
print('HelloWorld'.ljust(18))  # HelloWorld
print('HelloWorld'.ljust(8))  # HelloWorld
print('#'.format(18, '#'))
print('HelloWorld'.rjust(18, '*'))  # ********HelloWorld
print('HelloWorld'.rjust(18))  #           HelloWorld
print('HelloWorld'.rjust(8))  #  HelloWorld

"""
4、 zfill: 右对齐，左边用0填充
该方法只接收一个参数，用于指定字符串的宽度。如果指定的宽度小于等于字符串的长度，返回字符串本身。
"""
print('578'.zfill(6))  # 000578
print('-578'.zfill(6))  # -00578
print('578'.zfill(2))  # 578
print('-578'.zfill(3))  # -578

