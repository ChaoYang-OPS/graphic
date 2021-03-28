"""自动创建与启动的父线程"""

"""
    任何进程都会自动创建并启动一个线程，该线程被称为父(主)线程。
    父(主)线程的默认名称是MainThread。
"""

import time, threading

# 方法current_thread()用于获得当前线程实例对象(自动创建与启动的父线程)

print('自动创建并启动了父(主)线程: {}' \
      .format(threading.current_thread().getName()))
time.sleep(20)
