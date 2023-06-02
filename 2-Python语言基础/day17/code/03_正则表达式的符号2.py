
import re

# 匹配数量
#   ? 表示前面字符可以出现0次或1次
#   * 表示前面字符可以出现0次或多次
#   + 表示前面字符可以出现1次或多次
#   {} 表示前面字符可以出现指定的次数范围

print(re.findall('go?gle', 'ggle'))
print(re.findall('go*gle', 'gooooooogle'))
print(re.findall('go+gle', 'ggle'))

print(re.findall('g\d+gle', 'g34234234gle'))
print(re.findall('g\w+gle', 'gabcDEF123_gle'))
print(re.findall('g.*g\d+le', 'gdfaksjf,$fsdjfl 234g888999le'))
print(re.findall('g\d?gle', 'g0gle'))

# {} : 表示前面字符可以出现指定的次数范围
# {3} 3次
# {3,} 至少3次
# {,3} 最多3次
# {1,3} 1-3次
print(re.findall('go{3}gle', 'gooogle'))
print(re.findall('go{3,}gle', 'gooooooogle'))
print(re.findall('go{,3}gle', 'gogle'))
print(re.findall('go{1,3}gle', 'gooogle'))

# 边界字符
#   ^ : 开头匹配
#   $ : 结尾匹配
#   ^$ : 完全匹配
print(re.search('^google', 'google123'))
print(re.search('google$', '123google'))
print(re.search('google', '12,$3google456,'))
print(re.search('^google$', '12,$3google456,'))  # None
print(re.search('^google$', 'googlegoogle'))  # None
print(re.search('^google$', 'google'))
print(re.search('^g\d+gle$', 'g3423423gle'))
print(re.search('g\d+gle', 'AAAAg3423423gleBBBB'))


# 贪婪模式: 尽可能多的匹配
print(re.findall('go?gle', 'gogle'))  # 非贪婪模式
print(re.findall('g\w*gle', 'gooooogle'))  # 贪婪模式
print(re.findall('go+gle', 'gooooogle'))  # 贪婪模式
print(re.findall('go{1,9}gle', 'gooooogle'))  # 贪婪模式

s = '''<ul class="nav-main fl" bossexpo="bg_dh_1">
    <li class="nav-item">
    <a href="http://news.qq.com/" target="_blank" bosszone="dh_1">新闻</a>
  </li>
    <li class="nav-item">
    <a href="http://v.qq.com/" target="_blank" bosszone="dh_2">视频</a>
  </li>
    <li class="nav-item">
    <a href="http://new.qq.com/ch/photo/" target="_blank" bosszone="dh_3">图片</a>
  </li>
    <li class="nav-item">
    <a href="https://new.qq.com/ch/milite/" target="_blank" bosszone="dh_4">军事</a>
  </li>
  </ul>'''

# () : 1整体，2分组
# pattern = '<a(.*)>'  # 贪婪，匹配到最后一个‘>’
# pattern = '<a(.*?)>'  # 非贪婪，匹配到最近一个‘>’
pattern = '<a.*?>(.*?)</a>'
print(re.findall(pattern, s, re.S))


#   \A : 开头匹配  了解
#   \Z : 结尾匹配
#   \A\Z : 完全匹配
'''
print(re.search('\Agoogle', 'google123'))
print(re.search('google\Z', '123google'))
print(re.search('\Agoogle\Z', 'googlegoogle'))  # None

# 和 ^$的区别
print(re.findall('\Agoogle', 'google is good\ngoogle is nice\ngoogle is cool', re.M))
# ['google']
print(re.findall('^google', 'google is good\ngoogle is nice\ngoogle is cool', re.M))
# ['google', 'google', 'google']
'''

# \b 单词边界，某单词是否以某内容(正则内容)结尾  了解
# \B 非单词边界
# print(re.search(r'google\b', 'abcgoogle123 abcgoogle google123'))
# print(re.search(r'google\B', 'abcgoogle123 abcgoogle google123'))

# \ 转义
print(re.search('go\.gle', 'go.gle'))

# | 或者
print(re.findall('ab|cd', 'ab666cd520ab1314'))
# 匹配身份证: 18位，最后一位可能是X
print(re.search('^\d{17}(\d|X)$', '33344420001122667X'))


