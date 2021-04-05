"""多进程执行的不确定性"""
"""
    默认情况下，多个进程的执行顺序和时间都是不确定的，完全取决于操作系统的调度。
"""

from multiprocessing import Process, current_process
import time


def do_sth():
    for i in range(5):
        print('%s: %d' % (current_process().name, i))
        time.sleep(2)


if __name__ == '__main__':

    for i in range(3):
        Process(target=do_sth).start()

    do_sth()
