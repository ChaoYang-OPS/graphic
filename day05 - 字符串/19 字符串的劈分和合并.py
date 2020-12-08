"""字符串的劈分和合并"""
"""
一、调用方法split或rsplit劈分字符串
    方法split从字符串的左边开始劈分，方法rsplit从字符串的右边开始劈分。
    默认的劈分符是空格字符串。
    这两个方法的返回值都是一个列表。
"""
s = 'Python     Swift    Kotlin'
print(s.split())  # ['Python', 'Swift', 'Kotlin']
print(s.rsplit())  # ['Python', 'Swift', 'Kotlin']
"""
  可以通过参数sep指定劈分字符串时的劈分符。
"""
s = 'Python|Swift|Kotlin'
print(s.split(sep='|'))  # ['Python', 'Swift', 'Kotlin']
print(s.rsplit(sep='|'))  # ['Python', 'Swift', 'Kotlin']
"""
  可以通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次数劈分后，剩余的子串
会单独作为一部分。此时，方法split和rsplit就有区别了。
"""
s = 'Python   Swift  Kotlin java '
print(s.split(maxsplit=2))  # ['Python', 'Swift', 'Kotlin java ']
print(s.rsplit(maxsplit=2))  # ['Python   Swift', 'Kotlin', 'java']

"""
二、调用方法partition或rpartition劈分字符串。
   方法partition从字符串的左边开始劈分，方法rpartition从字符串的右边开始劈分。
   调用这两个方法时都必须指定劈分符。
   方法partition在指定的劈分符第一次出现的地方(方法rpartition在指定的劈分符最后一次出现的地方)，将字符串
劈分为三部分：
1、劈分前面的部分
2、劈分符
3、劈分符后面的部分
   这两个方法的返回值都是一个元组
"""
s = 'Hello-World-!'
print(s.partition('-'))  # ('Hello', '-', 'World-!')
print(s.rpartition('-'))  # ('Hello-World', '-', '!')

s = 'HelloWorld-'
print(s.partition('-'))  # ('HelloWorld', '-', '')
print(s.rpartition('-'))  # ('HelloWorld', '-', '')
"""
   如果字符串不存在指定的劈分符，方法partition返回的元组中的三个元素依次为:
1、 字符串本身
2、 空字符串
3、 空字符串
   如果字符串不存在指定的劈分符，方法rpartition返回的元组中的三个元素依次为:
1、 空字符串
2、 空字符串
3、 字符串本身
"""
s = 'HelloWorld'
print(s.partition('-'))  # ('HelloWorld', '', '')
print(s.rpartition('-'))  # ('', '', 'HelloWorld')

"""
三、 调用方法join合并多个字符串
"""
# 字符串之间用'|'进行分隔
s = '|'.join(['Python', 'Swift', 'Kotlin'])
print(s)  # Python|Swift|Kotlin

s = '|'.join(('Python', 'Swift', 'Kotlin'))
print(s) #  Python|Swift|Kotlin

s = ''.join(['Python', 'Swift', 'Kotlin'])
print(s)  # PythonSwiftKotlin
# 可以把字符串看做是字符的列表
s = '|'.join('Python')
print(s)  # P|y|t|h|o|n
