"""自动创建与启动的过程"""

"""
    当在PyCharm中运行一个py文件时，PyCharm对应的进程会自动创建并启动一个新进程，其
默认名称为Python。当py文件运行结束时，自动创建并启动的新进程也随之结束。

    创建并启动子进程的进程称为父进程。
"""

import time, os
import multiprocessing

# getpid: get process id
print(os.getpid())  # 打印当前进程的ID

# getppid: get parent process id
print(os.getppid())  # 打印当前进程父进程的ID

# 方法current_process用于获得当前进程实例对象（自动创建并启动的进程）
print(multiprocessing.current_process().pid)
