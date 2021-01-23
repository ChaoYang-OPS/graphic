"""自定义异常"""

"""
    尽管Python内置的异常类对象可以满足我们绝大部分的需求，但是有时候我们可能想要创建自定义的
异常类对象。
    正如所有内置异常类对象的基类是Exception，自定义异常类对象只需要继承Exception或其子类。
"""


class MyException(Exception):
    def __init__(self, msg1, msg2):
        self.msg1 = msg1
        self.msg2 = msg2


try:
    raise MyException('123', 'abc')
except MyException as err:
    print(err)
