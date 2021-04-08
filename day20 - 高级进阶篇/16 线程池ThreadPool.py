"""线程池ThreadPool"""

"""
    如果并发的任务数过多，一次性创建并启动大量的线程会给计算机带来很大的压力，
那么就可以使用线程池对创建与启动的线程进行限制和管理。
    线程池中所能容纳的线程数目是固定的。
    # pip3 install threadpool
    在第三方库threadpool中提供了一个类对象ThreadPool,用于表示线程池。线程池中所能容纳的线程数目
可以在创建ThreadPool实例对象时进行指定;如果不指定，默认大小是CPU的核数。
"""

from threadpool import ThreadPool, makeRequests
import time, random


def do_sth(i):
    print("子线程{}启动".format(i))
    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()
    print("子线程{}结束, 耗时{}秒".format(i, end - start))


if __name__ == '__main__':
    print("子线程启动")
    args_list = []
    for i in range(1, 11):
        args_list.append(i)
    # 将线程池所能容纳的最大进程数指定为3

    tp = ThreadPool(3)
    # 创建需要线程池处理的任务
    requests = makeRequests(do_sth, args_list)

    # 将需要线程池处理的任务全部交给线程池，从此会创建并启动由线程池所管理的子线程
    for req in requests:
        tp.putRequest(req)


    # 父线程被阻塞
    # 线程池管理的所有子线程执行完之后，父线程再从被阻塞的地方继续执行
    tp.wait()

    print("父线程结束")

# 程序运行后会同时创建3个子线程，第4个子线程要等前面3个中的某一个执行结束后才会创建并启动
