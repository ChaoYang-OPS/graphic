"""写文件"""
"""
    写文件之前，必须先打开文件。
    可以调用内置函数open()并以只写方式、追回方式或读写方式读写方式打开文件。这样，返回的文件对象有两个
用于写文件的方法:
1. write(text)
    用于将指定的字符串写入到文件中。调用后，会先将指定的字符串写入到缓存中，手动调用方法flush()或close()之后，
或者当写入的数据量大于等于缓存的容量时，缓存的字符串才会被写入到文件中。
    
    方法的返回值为写入的字符数，即指定的字符串的长度。
    
>>> file = open('myfile.txt', 'w')
>>> file.write('hello')
5
>>> file.write('python')
6
>>> file.flush()
>>> file.close()
>>> file = open('myfile.txt', 'a')
>>> file.write('hello')
5
>>> file.write('python')
6
>>> file.close()
  
2. writelines(seq) 
    用于将指定的字符串序列依次写入到文件中。
    调用后，会先将指定的字符串序列写入到缓存中，手动调用方法flush()或close()之后，
或者当写入的数据量大于等于缓存的容量时，缓存的字符串序列才会被写入到文件中。
>>> file = open('myfile.txt', 'w')
>>> file.writelines(['123\n', '456\n', '789'])
>>> file.close()
"""
