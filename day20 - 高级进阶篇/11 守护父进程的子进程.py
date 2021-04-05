"""守护父进程的子进程"""
"""
    可以在调用进程实例对象的方法start()之前将属性daemon的值设置为True,从而将进程设置为守护进程。
    守护进程是为了守护父进程而存在的子进程。当父进程结束时，守护进程就没有存在的意义了，因此，
守护进程会随着父进程的结束而立刻结束。
"""
from multiprocessing import current_process
from multiprocessing import Process
import time

print("父进程启动%d" % current_process().pid)


class MyProcess(Process):
    def run(self):
        print("子进程启动%d" % current_process().pid)
        time.sleep(2)
        print("子进程结束%d" % current_process().pid)


if __name__ == '__main__':
    mp = MyProcess()
    mp.daemon = True
    mp.start()

    time.sleep(1)
    print("父进程结束%d" % current_process().pid)
