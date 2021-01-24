"""关闭文件"""

"""
    文件在使用完毕后必须要关闭，这是因为文件对象会占用操作系统的资源，并且操作系统在某一时刻
所能打开的文件数量也是有限的。
    读文件或写文件时都有可能发生异常，从而导致方法close()不会被调用。为了保证方法close()总能
被调用，可以把读文件或写文件的操作放在try语句块中，把方法close()的调用放在finally从句中，
伪代码如下:
打开文件
try:
    读文件或写文件
finally:
    调用方法close()关闭文件

    由于文件对象实现了特殊方法__enter__()和__exit__()，所以文件对象可以作为上下文管理器。
其中，特殊方法__enter__()返回打开的文件对象，特殊方法__exit__()中关闭打开的文件，因此，
上面的伪代码可以使用with语句来实现:

with 打开文件 as file:
    读文件或写文件
"""

file = open('myfile.txt', 'w')

try:
    file.write('hello')
finally:
    file.close()

with open('myfile.txt', 'a') as file:
    file.write('python')
