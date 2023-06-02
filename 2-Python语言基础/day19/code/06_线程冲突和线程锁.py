
# 线程冲突：当多个线程同时使用1个资源时可能造成的问题
# 解决方式：线程锁

import threading

n = 0

'''
def fn():
    global n
    for i in range(1000000):
        n += 1
    print(n)
'''


# 线程锁：一次只让一个线程访问资源
lock = threading.Lock()

# 死锁：多个线程访问多个资源时，可能会造成需要使用对方资源，但是对方一直占有而造成相互等待的现象
#      线程1           线程2
#    正在用A资源    正在使用B资源
#    还需要B资源    还需要A资源
# 重用锁：解决死锁
# rlock = threading.RLock()

def fn():
    # lock.acquire()  # 加锁

    with lock:  # 自动加锁和解锁
        global n
        for i in range(1000000):
            n += 1
        print(n)

    # lock.release()  # 解锁


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=fn)
        t.start()
        # t.join()  # 同步





