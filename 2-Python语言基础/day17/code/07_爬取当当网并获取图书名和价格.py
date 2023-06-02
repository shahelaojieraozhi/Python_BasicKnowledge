import requests
import re

# 当当网图书, 使用正则表达式取出书籍标题，价格：
#    http://category.dangdang.com/pg1-cp01.01.02.00.00.00.html

url = 'http://category.dangdang.com/pg1-cp01.01.02.00.00.00.html'

res = requests.get(url)
result = res.text
print(result)

# 使用正则匹配，获取：书籍标题，价格


