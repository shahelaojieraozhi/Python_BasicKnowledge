
import re

# 表示单个字符

# . 表示匹配除了换行以外的其他任意单个字符
print(re.search('go.gle', 'google'))
print(re.search('go.gle', 'go9gle'))
print(re.search('go.gle', 'go,gle'))
print(re.search('go.gle', 'go\ngle'))  # None
print(re.search('go.gle', 'go\ngle', re.S))
print(re.search('google', 'Google'))  # None
print(re.search('google', 'Google', re.I))
# re.S : 让.可以匹配换行
# re.I : 忽略大小写

# [] : 匹配单个字符的范围
# [abc] : 匹配a或b或c
# [a-z] : 小写字母，匹配a到z中间的某一个
# [A-Z] : 大写字母
# [a-zA-Z] : 字母
# [0-9] : 数字
# [0-9a-zA-Z_] : 数字字母下划线
print(re.search('go[abco]gle', 'google'))
print(re.search('go[a-z]gle', 'google'))
print(re.search('go[a-x]gle', 'google'))
print(re.search('go[A-Za-z]gle', 'goUgle'))
print(re.search('go[a-zABCU]gle', 'goUgle'))

# [^abc] : 对范围取反
# print(re.search('go[^a-z]gle', 'go,gle'))

# \d : 数字，等价于[0-9]
# \D (了解): 非数字，等价于[^0-9]
# \w : 数字字母下划线，等价于[0-9a-zA-Z_]
# \W (了解): 非数字字母下划线，等价于[^0-9a-zA-Z_]
# \s : 空格，换行符\n,制表符\t,换页符\f,回车符\r
# \S (了解) : 表示非空格
print(re.search('go\dgle', 'go6gle'))  # 重要
# print(re.search('go\Dgle', 'go,gle'))
print(re.search('go\wgle', 'goAgle'))  # 重要
# print(re.search('go\Wgle', 'go,gle'))
# print(re.search('go\sgle', 'go gle'))
# print(re.search('go\Sgle', 'go gle'))














