"""守护父线程的子线程"""
"""
    在创建线程实例对象时，可以将参数daemon指定为True，从而将创建的线程设置为守护线程。此时，
也可以调用线程的实例对象的方法start()之前调用线程实例对象的方法setDaemon(True)或将属性daemon的值设置为True,
从而将线程设置为辅守护线程。
    守护线程是为了守护父线程而存在的子线程。当父线程结束时，守护线程就没有存在的意义了，因此，
守护线程会随着父线程的结束而立刻结束。
"""
from threading import Thread
from threading import current_thread
import time

print("父线程启动%s" % current_thread().getName())


class MyThread(Thread):
    def run(self):
        print("子线程启动%s" % current_thread().getName())
        time.sleep(2)
        print("子线程结束%s" % current_thread().getName())


if __name__ == '__main__':
    mt = MyThread()
    # mt.daemon = True
    mt.setDaemon(True)
    mt.start()

    time.sleep(1)
    print("父线程结束%s" % current_thread().getName())
