
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
url = "https://jobs.51job.com/"

res = requests.get(url, headers=headers)
content = res.content.decode('gbk')
print(content)


