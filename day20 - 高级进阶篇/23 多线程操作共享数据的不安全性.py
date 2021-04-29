"""多线程操作共享数据的不安全性"""


"""
    由于多线程的执行是不确定的，导致多线程操作共享数据的结果是不可预期的，常被称为不安全的。
"""
from threading import Thread

num = 0


def do_sth():
    global num
    for i in range(1000000):
        # 相当于: num = num + 1
        # 首先计算 num + 1, 存入临时变量中，然后将临时变量的值赋给num
        num += 1


t1 = Thread(target=do_sth)
t2 = Thread(target=do_sth)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)