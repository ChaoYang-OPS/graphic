"""谁在说谎"""

"""
【问题描述】
    张三说李四在说谎，李四说王五在说谎，王五说张三和李四都在说谎。
    这三人中到底谁说的是真话，谁说的是假话？
【设计思路】
    张三说李四在说谎，说明：要么张三说的是真话李四说的是假话，要么张三说的是假话李四说的是真话
    李四说王五在说谎，说明：要么李四说的是真话王五说的是假话，要么李四说的是假话王五说的是真话
    王五说张三和李四都在说谎，说明： 要么王五说的是真话张三和李四说的都是假话，
    要么王五说的是假话张三和李四至少有一个说的是真话。
    
    设True表示某人说的是真话，False表示某人说的是假话。
    设lsZhang、isLi和isWang分别表示张三、李四和王五是否在说谎，则其取值范围都为[True, False]
    通过三重循环穷举lsZhang、isLi和isWang，在穷举的过程中，只要满足已知条件:
    isZhang == (not isLi)
        and isLi == (not isWang)
        and isWang == ((not isZhang) and (not isLi))
    即找到谁在说谎。
"""
#  设True表示某人说的是真话，False表示某人说的是假话
t = [True, False]
# 设lsZhang、isLi和isWang分别表示张三、李四和王五是否在说谎
#  通过三重循环穷举lsZhang、isLi和isWang

for isZhang in t:
    for isLi in t:
        for isWang in t:

            if isZhang == (not isLi) \
                    and isLi == (not isWang) \
                    and isWang == ((not isZhang) and (not isLi)):
                # 即找到谁在说谎
                print('张三:{zhang}, 李四:{li}, 王五:{wang}'
                      .format(zhang='真话' if isZhang == True else '假话', li='真话' if isLi == True else '假话',
                              wang='真话' if isWang == True else '假话'))

# 张三:假话, 李四:真话, 王五:假话
