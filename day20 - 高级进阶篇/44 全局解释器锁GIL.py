"""全局解释器锁GIL"""

"""
    
"""

"""
def do_sth():
    while True:
        pass



do_sth()


# 单进程或单线程占满了八核CPU中的其中一核。

"""
"""
from multiprocessing import Process

def do_sth():
    while True:
        pass

Process(target=do_sth).start()
Process(target=do_sth).start()

do_sth()

# 三个进程或单线程占满了八核CPU中的其中三核。因此，多进程可以实现并行(同时处理多个任务)，从而发挥
多核CPU的最大功效。
"""

"""
from threading import Thread

def do_sth():
    while True:
        pass

Thread(target=do_sth).start()
Thread(target=do_sth).start()
do_sth()

# 三个线程并没有占满八核CPU中的其中三核，而只占满了其中一核，因此，多线程并不能实现并行（同时处理多个任务）
# 而只能实现并发(交替处理多个任务)

"""

"""
    我们编写的Python代码是通过Python解释器来执行的。通常使用的Python解释器官方提供的CPython。
CPython中有一个GIL (Global Interpreter Lock,全局解释器锁), 其作用相当于Lock,任何线程在执行前
必须先获得GIL，一个线程在获得GIL后其它线程就不能执行，直到线程释放GIL。因此，GIL保证了
同一时刻只有一个线程可以执行，从而导致Python中的多进程不能实现并行。
"""