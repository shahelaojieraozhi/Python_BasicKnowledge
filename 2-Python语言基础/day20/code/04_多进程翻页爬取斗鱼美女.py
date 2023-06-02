import os

import requests
import multiprocessing
from urllib import request


def douyu(page=1):
    url = f'https://www.douyu.com/gapi/rknc/directory/yzRec/{page}'

    # 获取url网址的数据
    res = requests.get(url)
    result = res.json()

    # 取出每个主播的 昵称nn 和 图片路径rs1
    rl = result['data']['rl']
    for meinv in rl:
        name = meinv['nn']
        img = meinv['rs1']
        # print(page, name, img)

        # 下载图片
        try:
            request.urlretrieve(img, f'douyu/{page}-{name}.png')
            request.urlcleanup()
        except Exception as e:
            print("出错了：", e)
            print("img:", img)

    print(f'第{page}页 下载完成!')


if __name__ == '__main__':
    # 如果没有“douyu”文件夹，则创建
    if not os.path.exists('douyu'):
        os.mkdir('douyu')

    for i in range(1, 6):
        multiprocessing.Process(target=douyu, args=(i,)).start()



