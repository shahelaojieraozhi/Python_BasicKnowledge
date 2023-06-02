﻿
"""[00:03.50]传奇
[00:19.10]作词：刘兵 作曲：李健
[00:20.60]演唱：王菲
[00:26.60]
[04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼
[04:49.00]
[02:47.44][00:43.69]再也没能忘掉你容颜
[02:54.83][00:51.24]梦想着偶然能有一天再相见
[03:02.32][00:58.75]从此我开始孤单思念
[03:08.15][01:04.30]
[03:09.35][01:05.50]想你时你在天边
[03:16.90][01:13.13]想你时你在眼前
[03:24.42][01:20.92]想你时你在脑海
[03:31.85][01:28.44]想你时你在心田
[03:38.67][01:35.05]
[04:09.96][03:39.87][01:36.25]宁愿相信我们前世有约
[04:16.37][03:46.38][01:42.47]今生的爱情故事 不会再改变
[04:24.82][03:54.83][01:51.18]宁愿用这一生等你发现
[04:31.38][04:01.40][01:57.43]我一直在你身旁 从未走远
[04:39.55][04:09.00][02:07.85]
"""



import time

music_lrc_str = """[00:03.50]传奇
[00:19.10]作词：刘兵 作曲：李健
[00:20.60]演唱：王菲
[00:26.60]
[04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼
[04:49.00]
[02:47.44][00:43.69]再也没能忘掉你容颜
[02:54.83][00:51.24]梦想着偶然能有一天再相见
[03:02.32][00:58.75]从此我开始孤单思念
[03:08.15][01:04.30]
[03:09.35][01:05.50]想你时你在天边
[03:16.90][01:13.13]想你时你在眼前
[03:24.42][01:20.92]想你时你在脑海
[03:31.85][01:28.44]想你时你在心田
[03:38.67][01:35.05]
[04:09.96][03:39.87][01:36.25]宁愿相信我们前世有约
[04:16.37][03:46.38][01:42.47]今生的爱情故事 不会再改变
[04:24.82][03:54.83][01:51.18]宁愿用这一生等你发现
[04:31.38][04:01.40][01:57.43]我一直在你身旁 从未走远
[04:39.55][04:09.00][02:07.85]
"""

# 1.先按行拆分
music_lrc_list = music_lrc_str.splitlines()
# print(music_lrc_list)

# 2.遍历每一行
lrc = []
for music_lrc in music_lrc_list:
    # print(music_lrc)  # '[04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼'
    # 3.将歌词时间和歌词内容拆开
    lrc_list = music_lrc.split(']')
    # print(lrc_list)  # ['[04:40.75', '[02:39.90', '[00:36.25', '只是因为在人群中多看了你一眼']
    # 4.取出歌词内容
    lrc_content = lrc_list.pop()
    # print(lrc_content)  # '只是因为在人群中多看了你一眼'
    # print(lrc_list)  # ['[04:40.75', '[02:39.90', '[00:36.25']
    # 5.取出歌词时间
    for lrc_time in lrc_list:
        lrc_time2 = lrc_time[1:]  # 去掉左中括号[
        # print(lrc_time2)  # '04:40.75'

        # 6.将每句歌词时间和对应的歌词内容,以字典的形式存储到列表中
        lrc.append({'time': lrc_time2, 'content': lrc_content})

# 7.排序:sort(key=)
lrc.sort(key=lambda d: d['time'])

# 查看
for d in lrc:
    print(d['time'], d['content'])
    time.sleep(1)

# 考虑按照指定的时间输出.














