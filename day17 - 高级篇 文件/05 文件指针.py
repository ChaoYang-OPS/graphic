"""文件指针"""

"""
一、 什么是文件指针
    任何文件对象都有一个文件指针，指向文件中的某个位置。
    读写文件时，是从文件指针的当前位置开始读写的，在读写的过程中，文件指针会随之往后移动。

二、打开文件后文件指针的位置 
    以追回方式打开文件后，文件指针指向文件的结尾位置；以其它方式打开文件后，文件指针指向文件的起始位置；
    可以调用文件对象的方法tell(),返回文件指针的当前位置。  
"""

with open('myfile.txt', 'r') as file:
    print(file.tell())  # 0
with open('myfile.txt', 'a') as file:
    print(file.tell())  # 11

"""
三、读写文件时文件指针的移动过程
"""
with open('myfile.txt', 'r') as file:
    print(file.tell())  # 0

    file.read(3)
    print(file.tell())  # 3

    file.read(4)
    print(file.tell())  # 7

    file.read()
    print(file.tell())  # 11

with open('myfile.txt', 'a') as file:
    print(file.tell())  # 11
    file.write('hello')
    print(file.tell())  # 16

with open('myfile.txt', 'w') as file:
    print(file.tell())  # 0
    file.write('hello')
    print(file.tell())  # 5

"""
四、自由移动文件指针
    可以调用文件对象的方法seek(offset[,whence]),将文件指针自由移动到参数指定的位置，其中:
参数offset表示偏移量，可以为负数; 参数whence是可选的，表示相对偏移位置，有三种取值:
1. os.SEEK_SET: 相对文件的起始位置，值为0，默认值
2. os.SEEK_CUR: 相对文件的起始位置，值为1
3. os.SEEK_END: 相对文件的结尾位置，值为2

    以文件方式打开的文件，只支持相对文件的起始位置。
"""
import os

with open('myfile2.txt', 'rb') as file:
    print(file.tell())  # 0

    # file.seek(3, os.SEEK_SET)
    # file.seek(3, 0)
    file.seek(3)
    print(file.tell())  # 3

    file.seek(4, os.SEEK_CUR)
    print(file.tell())  # 7

    file.seek(-2, os.SEEK_END)
    print(file.tell())  # 8

with open('myfile2.txt', 'r+') as file:
    print(file.tell())  # 0
    file.seek(3)
    print(file.tell())  # 3

    file.write('Python')
    print(file.tell())  # 9
