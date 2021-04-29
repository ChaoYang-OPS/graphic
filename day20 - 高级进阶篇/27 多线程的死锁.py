"""多线程的死锁(上)"""

"""
    如果有多个共享数据，在多个线程操作这多个共享数据时，如果两个线程分别通过加锁占有一部分共享数据，
并且同时等待对方释放锁，这样就会导致两个线程永远相互等待而产生死锁。
    要避免程序中出现死锁的情况。在避免死锁的算法中最有代表性的算法是Dijkstra提出的银行家算法。
"""

from threading import Thread, Lock, current_thread

numa = 0
numb = 0

locka = Lock()
lockb = Lock()


def do_sth():
    fun1()
    fun2()


def fun1():
    global numa, numb

    locka.acquire()
    try:
        print('%s---fun1()----locka' % current_thread().getName())
        numa += 1
        lockb.acquire()
        try:
            print('%s---fun1()----lockb' % current_thread().getName())
            numb += 1
        finally:
            lockb.release()
    finally:
        locka.release()


def fun2():
    global numa, numb

    locka.acquire()
    try:
        print('%s---fun2()----lockb' % current_thread().getName())
        numb += 1
        locka.acquire()
        try:
            print('%s---fun2()----lockb' % current_thread().getName())
            numa += 1
        finally:
            locka.release()
    finally:
        lockb.release()


t_list = []
for i in range(100):
    t = Thread(target=do_sth)
    t_list.append(t)
    t.start()

for item in t_list:
    item.join()


print('父线程结束')
