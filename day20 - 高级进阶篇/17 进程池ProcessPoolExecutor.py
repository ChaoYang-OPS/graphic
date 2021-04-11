"""进程池ProcessPoolExecutor"""

"""
    标准库模块concurrent.futures中提供了一个类对象ProcessPoolExecutor,也用于表示进程池。
与Pool相比,ProcessPoolExecutor的功能和性能更加强大。
    类对象ProcessPoolExecutor遵守上下文管理协议，所以可以使用with语句，这样，在离开运行时上下文时会
自动调用方法shutdown(wait=True)。
"""

from concurrent.futures import ProcessPoolExecutor
import time, random


def do_sth(i):
    print("子进程{}启动".format(i))
    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()
    print("子进程{}结束, 耗时{}秒".format(i, end - start))


if __name__ == '__main__':
    print("父进程启动")
    """
    # 将进程池所能容纳的最大进程数指定为3

    ppe = ProcessPoolExecutor(max_workers=3)
    # 将需要进程池所处理的任务全部交给进程池，此后会创建并启动由进程池管理的子进程
    for i in range(1, 11):
        ppe.submit(do_sth, i)

    # 父进程被阻塞
    # 进程池管理的所有子进程执行完之后，父进程再从被阻塞的地方继续执行
    ppe.shutdown(wait=True)
    """

    with ProcessPoolExecutor(max_workers=3) as ppe:
        """
        for i in range(1, 11):
            ppe.submit(do_sth, i)
        """
        ppe.map(do_sth, range(1, 11))

    print("父进程结束")

# 程序运行后会同时创建3个子进程，第4个子进程要等前面3个中的某一个执行结束后才会创建并启动














