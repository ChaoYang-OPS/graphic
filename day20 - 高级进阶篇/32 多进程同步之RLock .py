"""多进程同步之RLock"""

"""
    RLock也遵守上下文管理协议，所以可以使用with语句对代码进行简化。
"""

from multiprocessing import Process, RLock, Value

numa = Value('i', 0)
numb = Value('i', 0)

rlock = RLock()


def do_sth():
    """  """
    """
    rlock.acquire()
    try:
        adda()
        addb()
    finally:
        rlock.release()
    """
    with rlock:
        adda()
        addb()


def adda():
    global numa
    """
    rlock.acquire()
    try:
        numa.value += 1
    finally:
        rlock.release()
    """
    with rlock:
        numa.value += 1


def addb():
    global numb
    """
    rlock.acquire()
    try:
        numb.value += 1
    finally:
        rlock.release()
    """
    with rlock:
        numb.value += 1


p_list = []
for i in range(10):
    p = Process(target=do_sth)
    p_list.append(p)
    p.start()

for item in p_list:
    item.join()

print(numa.value)
print(numb.value)
