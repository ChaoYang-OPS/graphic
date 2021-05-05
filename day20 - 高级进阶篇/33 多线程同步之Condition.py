"""多线程同步之Condition 上"""

"""
    标准库模块threading中提供了一个类对象Condition，用于表示带触发条件的锁，以帮助我们处理多线程间复杂的同步问题。Condition允许一个或多个线程
等待触发条件，直到收到另外一个线程的通知。
"""

from threading import Thread, Condition
import time

cond = Condition()


class MyThread1(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        cond.acquire()

        print('{}说:1'.format(self.name))
        cond.notify()
        cond.wait()

        # 思考两秒之后再说
        time.sleep(2)
        print('{}说:11'.format(self.name))
        cond.notify()
        cond.wait()

        time.sleep(2)
        print('{}说:111'.format(self.name))
        cond.notify()
        cond.release()


class MyThread2(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        time.sleep(1)
        cond.acquire()
        # 思考两秒之后再说
        time.sleep(2)
        print('{}说:2'.format(self.name))
        cond.notify()
        cond.wait()

        time.sleep(2)
        print('{}说:22'.format(self.name))
        cond.notify()
        cond.wait()

        time.sleep(2)
        print('{}说:222'.format(self.name))
        cond.release()


MyThread1('Thread1').start()
MyThread2('Thread2').start()
