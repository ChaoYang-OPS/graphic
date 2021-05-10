"""定时器线程Timer"""

"""
    如果想要在指定的时间片段之后再启动子线程，可以使用标准库模块threading提供的类对象Timer,
用于表示定时器线程。Timer是Thread的子类，也是通过调用方法start()来启动线程。
"""

"""

from threading import Timer

def do_sth():
    print('hello Timer!')

timer = Timer(2, do_sth)
timer.start()

"""

"""
    定时器只执行一次。如果需要每隔一段时间执行一次，则需要在子线程调用的函数内部再次创建与启动定时器线程。
   
"""

from threading import Timer
import time

def do_sth():
    print('hello Timer!')
    global  timer
    timer = Timer(3, do_sth)
    timer.start()

timer = Timer(2, do_sth)
timer.start()

time.sleep(10)
timer.cancel()
