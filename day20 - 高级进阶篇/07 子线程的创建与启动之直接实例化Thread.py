"""子线程的创建与启动之直接实例化Thread"""

"""
    标准库模块threading提供了一个类对象Thread，用于表示线程。
    使用类对象Thread创建并启动子线程的第1种方式为:
(1) 根据类对象Thread创建线程实例对象；
(2) 调用线程实例对象的方法start()启动线程。
    调用方法start()后， 会自动调用方法run()，方法run()会自动调用target指定的函数。
    Thread的特殊方法__init__定义如下:
    __init__(self, group=None, target=None, name=None,args=(), kwargs=None, *, daemon=None):
    调用特殊方法__init__()时必须指定关键字实参，其中，
(1) 参考group用于指定线程实例对象所属的线程组，默认不属于任何线程组；
(2) 参数target用于指定被方法run()调用的函数，默认没有函数被调用；
(3) 参数name用于指定创建的线程实例对象的名称, 第n个子线程的默认名称为'Thread-n'
(4) 参数args用于指定target接收的位置参数，用元组表示，默认不接收位置参数;
(5) 参数kwargs用于指定target接收的关键字参数，用字典表示，默认不接收关键字参数;
(6) 参数daemon用于指定线程实例对象是否是守护线程，默认不是守护线程。
"""

from threading import Thread, current_thread

import time

print('父线程{}启动'.format(current_thread().getName()))

def do_sth(arg1, arg2):
    print('子线程{}启动'.format(current_thread().getName()))
    time.sleep(20)
    print("arg1={}, arg2={}".format(arg1, arg2))
    print('子线程{}结束'.format(current_thread().getName()))




process = Thread(target=do_sth, args=(5, 8), name='mythread')

process.start()

time.sleep(25)



print('父线程{}结束'.format(current_thread().getName()))


