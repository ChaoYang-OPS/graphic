"""多进程同步之Semaphore"""


"""
    标准库模块multiprocessing中提供了一个类对象Semaphore，用于表示信号量，它可以帮助我们控制并发进程
的最大数量，从而实现多进程之间的同步。
    Semaphore也遵守了上下文管理协议，所以可以使用with语句对代码进行简化。
"""

from multiprocessing import Semaphore, Process
import time, random

sem = Semaphore(3)


class MyProcess(Process):
    def run(self):
        # sem.acquire()
        with sem:
            print('{}获得资源'.format(self.name))
            time.sleep(random.random() * 10)
        # sem.release()


for i in range(10):
    MyProcess().start()

"""
    如果调用release()的次数比调用acquire()的次数多，计数器当前值就会超过它的初始值。
为了确保能够及时检测到程序中的这种bug,可以使用BoundedSemaphore替代Semaphore，这样
一旦程序中出现这种bug，就会抛出异常ValueError。
    但是，官方文档中提到: On Mac OS X, this is indistinguishable from Semaphore。
"""
from multiprocessing import BoundedSemaphore

bsem = BoundedSemaphore(3)
bsem.acquire()
bsem.release()

