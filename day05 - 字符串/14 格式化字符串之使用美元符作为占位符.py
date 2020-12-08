"""格式化字符串之使用美元符作为占位符"""
"""
    可以导入模块string中的类Template并使用美元符作为占位符，从而得到格式化字符串。
"""
from string import Template

price = 68.88
book = '<<数据结构与算法>>'
tmpl = Template('花了$p，买了一本书:$b')
"""
  1、调用方法substitute
"""
s = tmpl.substitute(p=price, b=book)
print(s)  # 花了68.88，买了一本书:<<数据结构与算法>>
s = tmpl.substitute({'p': price, 'b': book})
print(s)  # 花了68.88，买了一本书:<<数据结构与算法>>
"""
  当占位符没有匹配的实际值时，抛出KeyError。
"""
# tmpl.substitute(p = price)  # KeyError: 'b'

"""
  2、调用方法safe_substitute
     由方法名可知，safe_substitute比substitute更安全，当占位符没有匹配的实际值时，
  并不会抛出KeyError,而是使用占位符本身作为其实际值。
"""
s = tmpl.safe_substitute(p = price)
print(s)  # 花了68.88，买了一本书:$b