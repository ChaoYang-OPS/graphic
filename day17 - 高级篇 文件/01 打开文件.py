"""打开文件"""

"""
    把数据存储以文件中是数据存储的方式之一。
    如何将数据写入文件，并将写入到文件中的数据读取出来呢？
    
    读写文件之前，必须先打开文件。
    内置函数open()用于打开文件，
        第一个参数是文件的路径，必须要指定。既可以指定绝对路径，也可以指定相对路径。
        第二个参数是文件的打开方式，默认值是'r',表示以只读方式打开。
        其它参数都是带默认值的，可参考官方文档。
        函数的返回值是一个文件对象，通过该对象就可以操作文件了，例如: 读文件、写文件、关闭文件等。
"""

# file = open('myfile.txt')
# file = open('myfile.txt', 'r')

# file = open('myfile.txt', 'w')
# file = open('myfile2.txt', 'w')
# file = open('myfile.txt', 'a')

# file = open('myfile.txt', 'x')
# file = open('myfile.txt', 'r+')