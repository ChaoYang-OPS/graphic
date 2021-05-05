"""多线程同步之Semaphore上"""

"""
    标准库模块threading中提供了一个类对象Semaphore，用于表示信号量，它可以帮助我们控制并发线程
的最大数量，从而实现多线程之间的同步。
    Semaphore也遵守了上下文管理协议，所以可以使用with语句对代码进行简化。
"""

from threading import Semaphore, Thread
import time, random

sem = Semaphore(3)


class MyThread(Thread):
    def run(self):
        # sem.acquire()
        with sem:
            print('{}获得资源'.format(self.name))
            time.sleep(random.random() * 10)
        # sem.release()


for i in range(10):
    MyThread().start()

"""
    如果调用release()的次数比调用acquire()的次数多，计数器当前值就会超过它的初始值。
为了确保能够及时检测到程序中的这种bug,可以使用BoundedSemaphore替代Semaphore，这样
一旦程序中出现这种bug，就会抛出异常ValueError。
"""
from threading import BoundedSemaphore

bsem = BoundedSemaphore(3)
bsem.acquire()
bsem.release()
# bsem.release()  # ValueError: Semaphore released too many times
