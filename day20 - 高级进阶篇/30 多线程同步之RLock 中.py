"""多线程同步之RLock 下"""

"""
    在RLock的内部维护了一个Lock和一个计数器counter。counter记录了锁被acquire的次数。
    当线程第一次调用方法acquire()获得锁时，锁的拥有者被保存，同时计数器counter被初始化为1;
当再次调用方法acquire()时，首先判断调用者是否是锁的拥有者，如果是，计数器counter加1.
    方法acquire()的定义如下:
    def acquire(self, blocking=True, timeout=-1):
     me = get_ident()
        if self._owner == me:
            self._count += 1
            return 1
        rc = self._block.acquire(blocking, timeout)
        if rc:
            self._owner = me
            self._count = 1
        return rc
     当调用方法release()时，首先判断调用者是否是锁的拥有者，如果是，计数器counter减1；
如果计数器counter减1后变为0，则锁的拥有者设置为None，然后释放锁。
     方法release()的定义如下:
     def release(self):
        if self._owner != get_ident():
            raise RuntimeError("cannot release un-acquired lock")
        self._count = count = self._count - 1
        if not count:
            self._owner = None
            self._block.release()
            
    RLock相当于一个门，可以上多把锁，上多少把锁就得开多少把锁。
    因此方法acquire()和release()必须成对出现。如果在某个线程中调用了n次acquire(),必须调用
n次release()才能释放该线程所占用的锁。
     
"""

from threading import RLock

rlock = RLock()
rlock.acquire()
rlock.release()