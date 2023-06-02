
# 多线程爬取51job全部城市岗位，并分别保存到单独的以城市名为文件名的html中，如: 深圳.html
# url = "https://jobs.51job.com/"
# 正则提示:  '<div class="lkst">(.*?)</div>'

import os
import requests
import re
import threading

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

# 子线程
def city_thread(name, url):
    # 爬数据
    res = requests.get(url, headers=headers)
    content = res.content.decode('gbk')

    # 使用正则
    pattern = '<div class="detlist gbox">(.*?)<div class="dw_tlc">'
    result = re.findall(pattern, content, re.S)

    pattern2 = '<span class="title"><a title="(.*?)"'
    result2 = re.findall(pattern2, result[0], re.S)
    # if name == '深圳':
    #     print(name, len(result2))

    # 存入文件
    with open(f'citys/{name}.txt', 'w', encoding='utf-8') as fp:
        fp.write(str(result2))
        fp.flush()


if __name__ == '__main__':
    url = "https://jobs.51job.com/"

    res = requests.get(url, headers=headers)
    content = res.content.decode('gbk')
    # print(content)

    # 使用正则
    pattern = '<div class="lkst">(.*?)</div>'
    result = re.findall(pattern, content, re.S)[0]
    # print(result)

    pattern2 = '<a class="" href="(.*?)">(.*?)</a>'
    result2 = re.findall(pattern2, result, re.S)
    # print(result2)

    for city in result2:
        city_name = city[1]
        city_url = city[0]
        # print(city_name, city_url)

        # 创建线程
        t = threading.Thread(target=city_thread, args=(city_name, city_url))
        t.start()

