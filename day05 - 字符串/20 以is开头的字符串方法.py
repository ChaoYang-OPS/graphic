"""以is开头的字符串方法"""
"""
    字符串的很多方法是以is开头的:
1、 isidentifier: 判断指定的字符串是否是合法的标识符。
"""
print('abc'.isidentifier())  # True
print('123'.isidentifier())  # False
"""
   可以调用模块keyword中的方法iskeyword判断一个字符串是否是关键字。
"""
import keyword

print(keyword.iskeyword('if'))  # True
print(keyword.iskeyword('iF'))  # False
"""
2、 isspace: 判断指定字符串是否全部由空白字符组成。
"""
print('\t \r  \n'.isspace())  # True
"""
3、isalpha: 判断指定字符串是否全部由字母组成。
4、isdecimal: 判断指定字符串是否全部由十进制的数字组成。
5、isnumeric: 判断指定字符串是否全部由数字组成。
6、isalnum: 判断字符串是否全部由字母和数字组成。
"""
print('abc'.isalpha())  # True
print('abc1'.isalpha())  # False
print('123'.isdecimal())  # True
print('123六VI'.isdecimal())  # False
print('123'.isnumeric())  # True
print('123abc'.isalnum())  # True
