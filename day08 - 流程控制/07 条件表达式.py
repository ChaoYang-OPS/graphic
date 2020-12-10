"""条件表达式"""
"""
    条件表达式是包含if-else语句的表达式，它类似于C语言中的三目条件运算符。
    条件表达式的语法格式:
x if 判断条件  else y
    对应的运算规则：
如果判断条件的布尔值为True,条件表达式的返回值为x；否则，条件表达式的返回值为y。
"""
score = 88
result = '及格了' if score >= 60 else '没及格'

print(result)  # 及格了

# 以上代码相当于:
if score >= 60:
    result = '及格了'
else:
    result = '没及格'

print(result)  # 及格了

"""
    在一个条件表达式内可以嵌套另一个条件表达式。
"""
a = 6
b = 8
print('a大于b' if a > b else ('a小于b' if a < b else 'a等于b'))
