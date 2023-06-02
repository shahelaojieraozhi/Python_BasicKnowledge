import requests
import re
import time
import multiprocessing

# 当当网图书, 使用正则表达式取出书籍标题，价格：
#    http://category.dangdang.com/pg1-cp01.01.02.00.00.00.html


def dangdang(page=1):
    url = f'http://category.dangdang.com/pg{page}-cp01.01.02.00.00.00.html'
    res = requests.get(url)
    result = res.text

    # 使用正则匹配，获取：书籍标题，价格
    pattern1 = '<ul class="bigimg" id="component_59">(.*?)</ul>'
    result1 = re.findall(pattern1, result, re.S)[0]
    # 第一个图书
    pattern2 = "<img src='(.*?)' alt='(.*?)' />.*?<span class=\"search_now_price\">&yen;(.*?)</span>"
    result2 = re.findall(pattern2, result1, re.S)
    # 第2-60个图书
    pattern3 = "<img data-original='(.*?)'.*?alt='(.*?)' />.*?<span class=\"search_now_price\">&yen;(.*?)</span>"
    result3 = re.findall(pattern3, result1, re.S)

    result4 = result2 + result3
    for r in result4:
        # 写入文件
        with open('dangdang.txt', 'a', encoding='utf-8') as fp:
            s = f'第{page}页: {str(r)}\n'
            fp.write(s)
            fp.flush()

    print(f'第{page}页 下载完成!')


if __name__ == '__main__':

    start = time.time()

    # 异步：进程, 大约消耗2秒
    t_list = []
    for i in range(1, 21):
        t = multiprocessing.Process(target=dangdang, args=(i,))
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()

    end = time.time()
    print("耗时：", end-start)


