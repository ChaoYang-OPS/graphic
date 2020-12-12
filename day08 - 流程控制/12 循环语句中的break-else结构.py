"""循环语句中的break-else结构"""
"""
   在执行while语句或for-in语句时，如果循环正常结束，也就是说，如果没有执行循环体中的break
语句从而提前退出循环，有时可能想在循环正常结束后执行某些操作。
    为了判断循环是否正常结束，可以使用一个布尔值变量，在循环开始前将布尔值设置为False,
如果执行了循环体中的break语句从而提前退出循环，那就将布尔变量的值设置为True。
最后，在while语句或for-in语句的后面使用if语句判断布尔的变量的值，以判断循环是否是正常结束的。
 
"""
isBreak = False
n = 0
while n < 5:
    if n == 6:
        isBreak = True
        break
    n += 1
if not isBreak:
    print('循环正常结束，没有执行循环体中的break语句')




isBreak = False
for n in range(5):
    if n == 6:
        isBreak = True
        break
if not isBreak:
    print('循环正常结束，没有执行循环体中的break语句')

"""
    上述的解决方案还有更好的替代，Python为循环语句提供了break-else结构，也就是说
可以在while语句或for-in语句的后面添加else从句，这样，如果没有执行循环体中的break语句从而提前退出循环，就
会执行else从句。
"""

n = 0
while n < 5:
    if n == 6:
        break
    n += 1
else:
    print('循环正常结束，没有执行循环体中的break语句')

for n in range(5):
    if n == 6:
        break
else:
    print('循环正常结束，没有执行循环体中的break语句')

















