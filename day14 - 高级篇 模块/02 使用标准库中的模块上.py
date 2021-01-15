"""使用标准库中的模块"""

"""
    Python官方给我们提供了一个标准库，其中有非常多的模块可供我们使用，用以完成各种不同的任务
    MacOS系统中标准库的路径:
/Library/Frameworks/Python.framework/Versions/3.x/lib/python3.x/
    标准库中模块的源代码是极好的Python学习资料。
    如果想要使用标准库中模块，必须使用import语句进行导入。有两种导入方式:
 (1) 导入整个模块
 (2) 导入模块中的属性
"""

"""
一、导入整个模块
    导入整个模块的语法格式为: import [包名.]模块名。
    如果被导入的模块在一个包结构中，那么必须要通过其所有的父包导航到该模块:
顶层父包名.子包名.....子包名。

    导入整个模块之后，就可以访问模块中的属性了(包括: 变量、函数和类)，其语法格式为:
[包名.]模块名.属性名。

    当输入"[包名.]模块名."之后，在代码提示的列表中，变量用黄色的v(variable)表示，
函数用粉色的f(function)表示,类用蓝色的c(class)表示。
"""
# import os

# 操作系统中的所有环境变量
# print(os.environ)

# 操作系统中某个指定的环境变量
# print(os.getenv('PYTHON_HOME'))  # None
# MutableMapping 类
# print(os.MutableMapping)  # <class 'collections.abc.MutableMapping'>

import xml.dom.minidom

print(xml.dom.minidom.StringTypes)  # (<class 'str'>,)

"""
    导入整个模块时，可以给导入的模块起一个别名，其语法格式为:
import [包名.]模块名 as 模块的别名。
"""
import os as operationg_system

# 操作系统中的所有环境变量
print(operationg_system.environ)

# 操作系统中某个指定的环境变量
print(operationg_system.getenv('PYTHON_HOME'))

# MutableMapping 类
print(operationg_system.MutableMapping)  # <class 'collections.abc.MutableMapping'>

import xml.dom.minidom as md

print(md.StringTypes)  # (<class 'str'>,)
