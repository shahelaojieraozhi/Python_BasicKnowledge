
import threading
import time, random


# 信号量：控制线程的最大并发数
sem = threading.Semaphore(4)

def fn(n):
    with sem:
        print(n)
        time.sleep(random.uniform(1, 5))
        print(n, "finish")


if __name__ == '__main__':
    for i in range(1, 21):
        threading.Thread(target=fn, args=(i,)).start()
