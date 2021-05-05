"""多进程同步之Condition"""

"""
    
"""

"""
    标准库模块multiprocessing中提供了一个类对象Condition，用于表示带触发条件的锁，以帮助我们处理多进程间复杂的同步问题。Condition允许一个或多个进程
等待触发条件，直到收到另外一个进程的通知。
"""

from multiprocessing import Process, Condition
import time

cond = Condition()


class MyProcess1(Process):
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


class MyProcess2(Process):
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


MyProcess1('Process1').start()
MyProcess2('Process2').start()
