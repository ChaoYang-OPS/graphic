""" 遍历可迭代对象的内置函数map和filter"""
"""
一、遍历可迭代对象内置函数map
    第一个参数指定函数名，第二个参数指定可迭代对象。
    调用内置函数map后，会使用指定的函数名作用于指定的可迭代对象的每个元素，然后生成
新的可迭代对象。
"""
result = map(ord, 'abcd')
print(result)  # <map object at 0x10d795f10>
print(list(result))  # [97, 98, 99, 100]
# str.upper表示类str的方法upper，也就是字符串的方法upper
result = map(str.upper, 'abcd')
print(result)  # <map object at 0x10b383460>
print(list(result))  # ['A', 'B', 'C', 'D']

"""
二、用于遍历可迭代对象的内置函数filter
    第一个参数指定函数名，第二个参数指定可迭代对象。
    调用内置函数filter后，会使用指定的函数名作用于指定的可迭代对象的每个元素，过滤掉函数
返回值为False的相关元素，然后生成新的可迭代对象。
"""
result = filter(str.isalpha, '123abc')
print(result)  # <filter object at 0x10ec060d0>
print(list(result))  # ['a', 'b', 'c']
