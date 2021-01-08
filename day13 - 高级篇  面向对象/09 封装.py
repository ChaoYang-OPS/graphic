"""封装"""

"""
    封装是面向对象编程的三大特征之一。
    
    封装有两方面的含义:
1. 将数据(属性)和行为(方法)包装到类对象中。在方法内部对象属性进行操作，在类对象的外部调用方法。
这样，无需要关心方法内部的具体实现细节，从而隔离了复杂度。
2. 在类对象的内部通过访问控制把某些属性和方法隐藏起来，不允许在类对象的外部直接访问，而是在类对象
的内部对外提供公开的接口方法(例如getter和setter)以访问隐藏的信息。这样，就对隐藏的信息进行了保护。
"""


class Student(object):
    def __init__(self):
        self.__score = 90

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("成绩必须在0~100之间")


s = Student()

s.set_score(88)
print(s.get_score())  # 88

# s.set_score(123)  # ValueError: 成绩必须在0~100之间
