"""进程间通信之管道"""

"""
    如果想要实现进程之间的通信，管道也是常见的实现方式之一。
"""

from multiprocessing import Process, Pipe
import os
import time, random


# 发送数据的子进程执行的代码
def send_data(conn):
    print('发送数据的子进程{}启动'.format(os.getpid()))
    for obj in list(range(1, 10)):
        print('发送数据:{}'.format(obj))
        conn.send(obj)
        time.sleep(random.random() * 3)

    print('发送数据: None')
    conn.send(None)
    print('发送数据的子进程{}结束'.format(os.getpid()))


# 接收数据的子进程执行的代码
def recv_data(conn):
    print('接收数据的子进程{}启动'.format(os.getpid()))

    while True:
        item = conn.recv()
        if item is None:
            print('接收数据:None')
            break
        print('接收数据:{}'.format(item))
        time.sleep(random.random() * 3)
    print('接收数据的子进程{}结束'.format(os.getpid()))


print('父进程{}开始'.format(os.getpid()))

cr, cs = Pipe(False)
ps = Process(target=send_data, args=(cs,))
pr = Process(target=recv_data, args=(cr,))

ps.start()
pr.start()

ps.join()
pr.join()
print('父进程{}结束'.format(os.getpid()))
