
# greenlet
'''
# greenlet需要安装
from greenlet import greenlet
import time


def fn1():
    print('协程1')
    time.sleep(2)
    g2.switch()  # 切换到协程g2

    print('飞流直下三千尺')
    time.sleep(2)
    g2.switch()

def fn2():
    print('协程2')
    time.sleep(3)
    g1.switch()

    print('疑是银河落九天')


if __name__ == '__main__':
    g1 = greenlet(fn1)
    g2 = greenlet(fn2)
    g1.switch()  # 切换到g1协程

'''


# gevent
'''
# gevent: 需要安装
import gevent

def fn1():
    gevent.sleep(4)
    print('协程1')

    gevent.sleep(7)
    print('疑是地上霜')

def fn2():
    gevent.sleep(3)
    print('协程2')

    gevent.sleep(2)
    print('窗前明月光')


if __name__ == '__main__':
    g1 = gevent.spawn(fn1)
    g2 = gevent.spawn(fn2)
    gevent.joinall([g1, g2])

'''


import gevent
from gevent import monkey  # 猴子补丁
monkey.patch_all()  # 自动切换协程

import requests

def fn(url):
    print('协程:', url)
    res = requests.get(url)
    print(url, len(res.text))

if __name__ == '__main__':
    url_list = [
        'http://www.qq.com',
        'http://www.360.com',
        'http://www.baidu.com',
        'http://www.4399.com',
    ]
    g_list = []
    for url in url_list:
        g = gevent.spawn(fn, url)
        g_list.append(g)
    gevent.joinall(g_list)

