
# 多线程：多个线程并发执行的一种技术

import threading
import time
import random

def fn(name):
    time.sleep(random.uniform(1,3))
    print('子线程:', name)


if __name__ == '__main__':
    '''
    t1 = threading.Thread(target=fn, args=('袁隆平',))
    t1.start()
    # t1.join()  # 会暂停，会阻塞程序：会等待t1线程执行完成后才执行后面的代码

    t2 = threading.Thread(target=fn, args=('周恩来',))
    t2.start()
    # t2.join()

    t3 = threading.Thread(target=fn, args=('钱学森',))
    t3.start()
    # t3.join()
    '''

    # 异步：同时执行多个任务，多个线程同时在运行.
    # 同步：按顺序以此执行.

    # 其他方法：了解
    # print(t3.name, t3.getName())  # 线程名
    # print(t3.daemon)  # 是否为守护线程，False
    # print(t3.ident)  # 线程号
    # print(t3.is_alive())  # 是否在运行
    # print(threading.enumerate())  # 列举所有线程
    # print(threading.active_count())  # 正在运行的线程数量

    start = time.time()

    t_list = []
    for i in range(10):
        t = threading.Thread(target=fn, args=(f'马云{i}',))
        t.start()
        # t.join()  # 同步
        t_list.append(t)

    # 等待所有线程执行完成后，才执行后面的代码
    for t in t_list:
        t.join()

    end = time.time()
    print(end - start)

