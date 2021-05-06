"""多进程同步之Event"""

"""
    标准库模块multiprocessing中提供了一个类对象Event，也可以实现多进程间的同步。Event实例对象管理着
一个内部标志，通过改变这个内部标志的值，可以让一个进程给其它处于阻塞状态的进程发送一个事件信号，
从而唤醒这些进程让它们转为运行状态。
    Event的方法如下:
    (1) set(self)
        将内部标志设置为True.
    (2) is_set(self)
        判断内部标志是否被设置为True。
    (3) clear(self)
        将内部标志设置为False.
    (4) wait(self, timeout=None)
        当内部标志为False时，调用该方法的进程会被阻塞。
        直到另外一个进程调用了方法set()将内部标志设置为True，被阻塞的进程才会转为运行状态。
"""

from multiprocessing import Process, Event, current_process

import time

event = Event()

print(event.is_set())  # False


def do_sth():
    print('{}开始等待'.format(current_process().pid))
    event.wait()
    print('{}结束等待'.format(current_process().pid))


for i in range(3):
    Process(target=do_sth).start()

time.sleep(2)
event.set()
