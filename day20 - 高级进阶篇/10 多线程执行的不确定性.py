"""多线程执行的不确定性"""
"""
    默认情况下，多个线程的执行顺序和时间都是不确定的，完全取决于操作系统的调度。
"""

from threading import Thread, current_thread
import time


def do_sth():
    for i in range(5):
        print('%s: %d' % (current_thread().name, i))
        time.sleep(2)


if __name__ == '__main__':

    for i in range(3):
        Thread(target=do_sth).start()

    do_sth()
