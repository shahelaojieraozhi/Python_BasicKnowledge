import requests
import re

# 当当网图书, 使用正则表达式取出书籍标题，价格：
#    http://category.dangdang.com/pg1-cp01.01.02.00.00.00.html

url = 'http://category.dangdang.com/pg1-cp01.01.02.00.00.00.html'

res = requests.get(url)
result = res.text
# print(result)

# 使用正则匹配，获取：书籍标题，价格
pattern1 = '<ul class="bigimg" id="component_59">(.*?)</ul>'
result1 = re.findall(pattern1, result, re.S)[0]
# print(result1)

# 第一个图书
pattern2 = "<img src='(.*?)' alt='(.*?)' />.*?<span class=\"search_now_price\">&yen;(.*?)</span>"
result2 = re.findall(pattern2, result1, re.S)
# print(result2)

# 第2-60个图书
pattern3 = "<img data-original='(.*?)'.*?alt='(.*?)' />.*?<span class=\"search_now_price\">&yen;(.*?)</span>"
result3 = re.findall(pattern3, result1, re.S)
# print(result3)
# print(len(result3))

result4 = result2 + result3
# print(result4)
for r in result4:
    print(r)

