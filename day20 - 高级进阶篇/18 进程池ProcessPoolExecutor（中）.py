"""进程池ProcessPoolExecutor中"""

"""
    方法submit()的返回值是一个Future实例对象，表示子进程所调用的那个函数的执行(比如: do_sth())
可以调用Future的方法result()得到这个函数的返回值。
    方法result()是一个同步方法，也就是说，直到这个函数执行完毕之后方法result()才会返回。
"""
from concurrent.futures import ProcessPoolExecutor
import time

def do_sth(i):
    time.sleep(2)
    return i * i


if __name__ == '__main__':
    """
    with ProcessPoolExecutor(max_workers=3) as ppe:
        for i in range(1, 5):
            future = ppe.submit(do_sth, i)
            # 同步，需要等待do_sth执行完毕
            print(future.result())
    """
    with ProcessPoolExecutor(max_workers=3) as ppe:
        objs = []
        for i in range(1, 5):
            future = ppe.submit(do_sth, i)
            # 异步，无需等待do_sth执行完毕
            print(future)
            objs.append(future)

    for obj in objs:
        print(obj.result())


