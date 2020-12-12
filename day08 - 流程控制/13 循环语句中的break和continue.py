""" 循环语句中的break和continue"""
"""
    在while语句或for-in语句的循环中，除了可以使用break语句之外，还可以使用continue语句，
两者的区别在于:
break表示"断路"，用于结束整个循环；
continue表示"短路"，用于结束整个循环中的当前迭代，继续下一个迭代。
"""
for i in range(1, 5):
    if i == 3:
        break
    print('i = ', i)
'''
i =  1
i =  2
'''
for i in range(1, 5):
    if i == 3:
        continue
    print('i = ', i)
'''
i =  1
i =  2
i =  4
'''
"""
    在嵌套的循环语句中，break和continue默认作用于当前循环。
"""

for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            break
        print('i=', i, 'j=', j)
'''
i= 2 j= 1
i= 3 j= 1
i= 3 j= 2
'''
for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            continue
        print('i=', i, 'j=', j)
'''
i= 1 j= 2
i= 1 j= 3
i= 2 j= 1
i= 2 j= 3
i= 3 j= 1
i= 3 j= 2
'''