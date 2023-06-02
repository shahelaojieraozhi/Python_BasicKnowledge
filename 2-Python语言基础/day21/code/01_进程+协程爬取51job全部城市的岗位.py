
# 进程+协程爬取51job全部城市岗位

import gevent
from gevent import monkey
monkey.patch_all()

import os
import requests
import re
import multiprocessing

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

# 1.获取所有城市信息
def get_all_city():
    url = "https://jobs.51job.com/"

    res = requests.get(url, headers=headers)
    content = res.content.decode('gbk')

    # 使用正则
    pattern = '<div class="lkst">(.*?)</div>'
    result = re.findall(pattern, content, re.S)[0]

    pattern2 = '<a class="" href="(.*?)">(.*?)</a>'
    result2 = re.findall(pattern2, result, re.S)

    sem = multiprocessing.Semaphore(4)

    for city in result2[:2]:
        city_name = city[1]
        city_url = city[0]
        # print(city_name, city_url)

        # 创建进程
        p = multiprocessing.Process(target=city_process, args=(city_name, city_url, sem))
        p.start()


# 2.进程：处理每一个城市的岗位
#   处理翻页
def city_process(name, url, sem):
    with sem:
        g_list = []
        for i in range(1, 3):
            url2 = f'{url}p{i}/'

            # 协程: 每一页用一个协程来爬取
            g = gevent.spawn(page_coroutine, name, url2)
            g_list.append(g)
        gevent.joinall(g_list)


# 3.协程：爬取每一页
def page_coroutine(name, url):
    # 爬数据
    res = requests.get(url, headers=headers)
    content = res.content.decode('gbk')

    # 使用正则
    pattern = '<div class="detlist gbox">(.*?)<div class="dw_tlc">'
    result = re.findall(pattern, content, re.S)

    pattern2 = '<span class="title"><a title="(.*?)".*?class="name".*?>(.*?)</a>.*?class="location">(.*?)</span>'
    result2 = re.findall(pattern2, result[0], re.S)

    # 存入文件: 岗位名称，公司名称，薪资
    for job in result2:
        with open(f'citys/{name}.txt', 'a', encoding='utf-8') as fp:
            fp.write(f'{str(job)} \n')
            fp.flush()

        print(f'{name}: {job} 爬取成功!')


if __name__ == '__main__':
    get_all_city()

