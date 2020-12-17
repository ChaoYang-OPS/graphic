"""函数的定义之文档字符串"""

"""
一、 什么是文档字符串
    对于函数、模块、类或方法，位于其第一行的字符串称为文档字符串，通常用三个引号表示。
    文档字符串用于对函数、模块、类或方法进行解释说明。
    之所以称为"文档"字符串，是因为可以使用工具根据文档字符串自动地生成文档。
    
    应该养成编写文档字符串的习惯，以提高程序的可读性。
    
    通过属性__doc__可以访问文档字符串。
    调用内置函数help()得到的帮助信息中会包含文档字符串。
"""
print(len.__doc__)
print(help(len))

"""
二、函数的文档字符串的常见内容和格式约定
    1、第一行简明扼要的总结
    2、第一行的首字母大写，第一行以句号结尾。
    3、如果文档字符串包含多行，第二行是空行，从第三行开始是详细的描述。 
    
    更多关于文档字符串的约定，可参考PEP 257: https://www.python.org/dev/peps/pep-0257/
"""


def form_complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part(default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    pass
