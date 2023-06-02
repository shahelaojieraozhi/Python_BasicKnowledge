
#   进程：是操作系统分配的一个资源单位，一般一个程序至少有一个进程
#   一个进程中至少有一个线程

import multiprocessing
import os

# 创建进程
# 第1种方式
def process1(*args):
    print('子进程:', multiprocessing.current_process().name)
    print(args)

# 第2种方式：自定义进程
class MyProcess(multiprocessing.Process):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        print('子进程:', multiprocessing.current_process().name)
        print("子进程pid:", self.pid, os.getpid())
        print('父进程pid:', os.getppid())


if __name__ == '__main__':
    # MainProcess
    print('主进程:', multiprocessing.current_process().name)

    # 第1种方式
    # p = multiprocessing.Process(target=process1, args=(1, 2, 3))
    # p.start()

    # 第2种方式：自定义进程
    p2 = MyProcess('http://www.baidu.com')
    p2.start()
    print(p2.pid)  # 进程号

    print('主进程pid:', multiprocessing.current_process().pid)

