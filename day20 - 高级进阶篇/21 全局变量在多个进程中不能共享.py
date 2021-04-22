"""全局变量在多个进程中不能共享"""

"""
    每个进程都有独立的内存空间，从而进程间是相互独立的。因此，全局变量在多个进程中不能共享。
"""

from multiprocessing import Process

num = 18

def do_sth():
    global num
    num += 1

if __name__ == '__main__':

    p = Process(target=do_sth)
    p.start()
    p.join()
    # 在子进程中修改全局变量对父进程中的全局变量没有影响
    # 因为子进程对父进程中的全局变量做了一份拷贝，子进程与父进程中的num是完全不同的两个变量
    print(num)  # 18

