"""线程池ProcessPoolExecutor"""

"""
    标准库模块concurrent.futures中提供了一个类对象ThreadPoolExecutor,也用于表示线程池。
与ThreadPool相比,ThreadPoolExecutor的功能和性能更加强大。
    类对象ThreadPoolExecutor遵守上下文管理协议，所以可以使用with语句，这样，在离开运行时上下文时会
自动调用方法shutdown(wait=True)。
"""

from concurrent.futures import ThreadPoolExecutor
import time, random


def do_sth(i):
    print("子线程{}启动".format(i))
    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()
    print("子线程{}结束, 耗时{}秒".format(i, end - start))


if __name__ == '__main__':
    print("父线程启动")
    """
    # 将线程池所能容纳的最大线程数指定为3

    tpe = ThreadPoolExecutor(max_workers=3)
    # 将需要线程池所处理的任务全部交给线程池，此后会创建并启动由线程池管理的子线程
    for i in range(1, 11):
        ppe.submit(do_sth, i)

    # 父线程被阻塞
    # 线程池管理的所有子线程执行完之后，父线程再从被阻塞的地方继续执行
    ppe.shutdown(wait=True)
    """

    with ThreadPoolExecutor(max_workers=3) as tpe:
        """
        for i in range(1, 11):
            ppe.submit(do_sth, i)
        """
        tpe.map(do_sth, range(1, 11))

    print("父线程结束")

# 程序运行后会同时创建3个子线程，第4个子线程要等前面3个中的某一个执行结束后才会创建并启动














