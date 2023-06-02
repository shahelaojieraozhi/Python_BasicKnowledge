
import threading
import _thread
import time


# 创建线程
# 第1种方式
def thread1(*args):
    print('子线程:', threading.current_thread().name)
    print(args)

# 第2种方式
def thread2(*args):
    print('子线程:', threading.current_thread().name)
    print(args)

# 第3种方式
import requests
class MyThread(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    # 重写run方法：子线程执行的函数
    def run(self):
        print('子线程:', threading.current_thread().name)

        res = requests.get(self.url)
        print(f'{self.url}: {len(res.text)}')


if __name__ == '__main__':
    print('主线程:', threading.current_thread().name)  # MainThread

    # 第1种方式: 重点掌握
    # t = threading.Thread(target=thread1, name='美国', args=('纽约','洛杉矶'))
    # t.start()

    # 第2种方式：了解
    # 守护线程：主线程结束，则子线程会立刻结束
    #       主公死了，游戏结束了，忠诚也死了
    # _thread.start_new_thread(thread2, ('hello', 'halo'))
    # time.sleep(0.1)

    # 第3种方式：掌握
    MyThread('http://www.qq.com').start()
    MyThread('http://www.ifeng.com').start()
    MyThread('http://www.baidu.com').start()

    # time.sleep(0.1)
    print('ok')

