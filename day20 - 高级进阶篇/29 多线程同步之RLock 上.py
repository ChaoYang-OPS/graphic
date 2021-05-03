"""多线程同步之RLock"""

"""
    在同一线程中，当调用了Lock的方法acquire()之后，如果在调用方法release()之前再次调用了方法
acquire()，也会导致死锁。
"""
"""
from threading import Lock

lock = Lock()

lock.acquire()
print('获得锁')
lock.acquire()
print('获得锁')
lock.release()
print('释放锁')
lock.release()
print('释放锁')
"""

"""
    标准库模块threading中还提供了一个用于表示锁的类对象RLock(Reentrant Lock,可重入锁)。
与Lock相同的是: RLock也提供了用于获得锁的方法acquire()和用于释放锁的方法release()。
与Lock不同的是: 在同一个线程中，当调用了RLock的方法acquire()之后，可以在调用方法release()之前
多次调用方法acquire()而不会导致死锁。
"""
from threading import RLock

rlock = RLock()

rlock.acquire()
print('获得锁')
rlock.acquire()
print('获得锁')
rlock.acquire()
print('获得锁')
rlock.release()
print('释放锁')
rlock.release()
print('释放锁')
rlock.release()
print('释放锁')
