"""多线程同步之RLock 下"""

"""
    RLock也遵守上下文管理协议，所以可以使用with语句对代码进行简化。
"""

from threading import Thread, RLock

numa = 0
numb = 0

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
        numa += 1
    finally:
        rlock.release()
    """
    with rlock:
        numa += 1

def addb():
    global numb
    """
    rlock.acquire()
    try:
        numb += 1
    finally:
        rlock.release()
    """
    with rlock:
        numb += 1


t_list = []
for i in range(10):
    t = Thread(target=do_sth)
    t_list.append(t)
    t.start()

for item in t_list:
    item.join()

print(numa)
print(numb)
