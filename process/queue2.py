from multiprocessing import Process, Queue
import os
import time
import random

# ## 进程间通信 ## #


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for i in range(10):
        print('Put %d to queue: ' % i)
        q.put(i)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        val = q.get(True)
        print('Get %d from queue.' % val)


if __name__ == '__main__':
    # 父进程创建 Queue 并传递给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    # 启动子进程，写入：
    pw.start()
    # 启动子进程，读取：
    pr.start()

    # 等待写入进程结束
    pw.join()
    # 读取进程是死循环，无法等待其结束，强制终止
    pr.terminate()

