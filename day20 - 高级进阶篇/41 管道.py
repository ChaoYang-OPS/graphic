"""管道"""

"""
    Python中的管道有两种工作方式:
    (1) 单向(半双工)
        一端只能发送数据，另一端只能接收数据。
    (2) 双向(全双工)
        两端即能发送数据又能接收数据，一端发送的数据只能由另一端接收。
    标准库模块multiprocessing中提供了一个函数Pipe()，其返回值是一个元组，元组中包含两个对象，
分别表示管道两端连接。
    调用函数Pipe()时，如果不传入参数或传入的参数为True，管道的工作方式为双向(全双工)；
如果传入的参数为False，管道的工作方式为单向(半双工)，其中，对于返回的元组，第一个连接对象只能接收数据
第二个连接对象只能发送数据。
    对于管道两端的连接对象，主要由两个方法:
 (1) send(self, obj)
    用于将参数obj指定的对象发送到管道。
 (2) recv(self)
    用于从管道中接收对象。
"""

from multiprocessing import Pipe


conn1, conn2 = Pipe()

conn1.send('conn1第一次发送的数据')
conn1.send('conn1第二次发送的数据')

conn2.send('conn2第一次发送的数据')
conn2.send('conn2第二次发送的数据')

print(conn1.recv())  # conn2第一次发送的数据
print(conn1.recv())  # conn2第二次发送的数据

print(conn2.recv())  # conn1第一次发送的数据
print(conn2.recv())  # conn1第二次发送的数据

c1, c2 = Pipe(False)

c2.send('c2发送的数据')
print(c1.recv())  # c2发送的数据

# c1.send('c1发送的数据')  # OSError: connection is read-only