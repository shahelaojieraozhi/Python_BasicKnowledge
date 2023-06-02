import multiprocessing
import time


# 进程锁
def process1(i, lock):
    with lock:
        print('hello:', i)
        time.sleep(3)
        print('end:', i)

# 信号量
def process2(i, sem):
    with sem:
        print('hello:', i)
        time.sleep(3)
        print('end:', i)


if __name__ == '__main__':
    # lock = multiprocessing.Lock()
    # for i in range(1, 5):
    #     multiprocessing.Process(target=process1, args=(i, lock)).start()

    # 进程的最大并发数为4
    sem = multiprocessing.Semaphore(4)
    for i in range(1, 20):
        multiprocessing.Process(target=process2, args=(i, sem)).start()

