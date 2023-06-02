
# 正则表达式： Regular Expression
#   作用：对字符串进行匹配和提取

import re

# match(): 匹配字符串是否以指定正则表达式内容开头,如果匹配成功则返回Match对象,否则返回None
print(re.match('\w+', 'hello,123'))
print(re.match('\w+', ',hello,123'))  # None

# search(): 匹配字符串是否包含指定正则表达式内容,如果匹配成功则返回Match对象,否则返回None
print(re.search('\w+', 'hello,123'))
print(re.search('\w+', ',hello,123'))
print(re.search('\w+', ',.#'))  # None

# findall(): 返回匹配的所有内容组成的列表
print(re.findall('\w+', 'hello,123'))  # ['hello', '123']
print(re.findall('\w+', ',.#'))  # []



