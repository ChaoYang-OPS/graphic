"""pass语句"""

"""
    pass语句什么都不做，它只是一个占位符，用在语法上需要语句的地方，例如:
1、if语句的条件执行体
2、for-in 语句的循环体
3、定义函数时的函数体
    有时候可能还没有想好上述相关语句该怎么写，就可以先使用pass语句作为占位符，以确保程序可以运行，
等想好了之后再把pass语句替换掉。
"""
age = 23

if age > 18:
    pass

for i in range(8):
    pass


def do_something():
    pass
