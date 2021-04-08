"""进程池Pool"""

"""
    如果并发的任务数过多，一次性创建并启动大量的进程会给计算机带来很大的压力，
那么就可以使用进程池对创建与启动的进程进行限制和管理。
    进程池中所能容纳的进程数目是固定的。
    标准库模块multiprocessing中提供了一个类对象Pool,用于表示进程池。进程池中所能容纳的进程数目
可以在创建Pool实例对象时进行指定;如果不指定，默认大小是CPU的核数。
"""

from multiprocessing import Pool
import time, random


def do_sth(i):
    print("子进程{}启动".format(i))
    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()
    print("子进程{}结束, 耗时{}秒".format(i, end - start))


if __name__ == '__main__':
    print("父进程启动")
    # 将进程池所能容纳的最大进程数指定为3

    pp = Pool(3)

    for i in range(1, 11):
        # 与方法start()类似，不同的是，创建并启动由进程池管理的子进程
        pp.apply_async(do_sth, args=(i,))

    # 调用方法join()之前必须先调用方法close()
    # 调用方法close()之后就不能让进程池再管理新的进程了
    pp.close()

    # 父进程被阻塞
    # 进程池管理的所有子进程执行完之后，父进程再从被阻塞的地方继续执行
    pp.join()

    print("父进程结束")

# 程序运行后会同时创建3个子进程，第4个子进程要等前面3个中的某一个执行结束后才会创建并启动
