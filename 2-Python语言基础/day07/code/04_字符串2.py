
# 字符串功能
s = 'hello'
# 查找子字符串在长字符串中出现的次数
print(s.count('l'))  # 2

# 大小写
print('hello'.upper())  # 变成大写 HELLO
print('HELLOabc123'.lower())  # 变成小写 helloabc123
# print('luhan LIKE football'.title())  # 标题化,每个单词首字母大写,其他小写. Luhan Like Football
# print('luhan LIKE football'.capitalize())  # 整句话首字母大写,其他小写. Luhan like football
# print('luhan LIKE football'.swapcase())  # 切换大小写. LUHAN like FOOTBALL

# 判断: 一般常用于对单个字符的判断
print('110'.isdigit())  # 是否为数字
print('abcD'.isalpha())  # 是否为字母
print('abcD1234'.isalnum())  # 是否为字母或数字
print('abc'.islower())  # 是否为小写
print('ABC'.isupper())  # 是否为大写
# print('Abc Def'.istitle())  # 是否标题化
print('        '.isspace())  # 是否为空白

# 查找
# find(): 从左往右,找到指定子字符串在长字符串中第一次出现的下标,如果不存在则返回-1
# rfind(): 从右往左,找到指定子字符串在长字符串中第一次出现的下标,如果不存在则返回-1
# index(): 了解, 和find类似,但是如果子字符串不存在则报错
# rindex(): 了解, 和rfind类似,但是如果子字符串不存在则报错
s = 'luhan is a very handsome very happy very good'
print(s.find('very'))  # 11
print(s.find('very2'))  # -1
print(s.rfind('very'))  # 36
# print(s.find('very', 12, 36))  # 25
# print(s.index('very2'))  # 报错,不推荐使用

# 拆分,分割
# split() : 得到的一定是列表
s = 'luhan      is a very handsome very happy very good'
print(s.split())  # 默认按空格拆分(按单词拆分)
# print(s.split(' '))
print(s.split('very'))  # ['luhan      is a ', ' handsome ', ' happy ', ' good']
print(s.split('good'))  # ['luhan      is a very handsome very happy very ', '']
print(s.split('o'))  # ['luhan      is a very hands', 'me very happy very g', '', 'd']
print(s.split('aaaaa'))  # ['luhan      is a very handsome very happy very good']
# print(s.split('very', 2))  # ['luhan      is a ', ' handsome ', ' happy very good']

# splitlines() 按行拆分
s = '''木兰诗
唧唧复唧唧
木兰当户织
不闻机杼声
唯闻女叹息'''

print(s.splitlines())  # ['木兰诗', '唧唧复唧唧', '木兰当户织', '不闻机杼声', '唯闻女叹息']
# print(s.splitlines(True))  # ['木兰诗\n', '唧唧复唧唧\n', '木兰当户织\n', '不闻机杼声\n', '唯闻女叹息']
print(s.split('\n'))  # ['木兰诗', '唧唧复唧唧', '木兰当户织', '不闻机杼声', '唯闻女叹息']

# 合并
l = ['a', 'b', 'c']
print(''.join(l))  # 'abc'
print('++'.join(l))  # 'a++b++c'

# 替换
s = 'luhan is a very handsome very happy very good'
print(s.replace('very', 'little'))
# print(s.replace('very', 'little', 2))  #  只替换前2个

# 对齐
# print('中澳矛盾升级'.center(60))
# print('中澳矛盾升级'.center(60, '-'))
# print('中澳矛盾升级'.ljust(60, '+'))
# print('中澳矛盾升级'.rjust(60, '*'))
# print('中澳矛盾升级'.zfill(60))

# strip(): 去除首尾指定字符,默认去除空格
# print('    张飞    赵子龙     关羽    '.strip())
# print('----张飞----赵子龙-----关羽----'.strip('-'))
# print('----张飞----赵子龙-----关羽----'.lstrip('-'))
# print('----张飞----赵子龙-----关羽----'.rstrip('-'))

# 编码和解码
#   编码: encode()  将字符串 => 二进制
#   解码: decode()  将二进制 => 字符串
s = 'hello 鹿晗'
b = s.encode()  # 编码,默认是utf-8
b = s.encode('GBK')  # 编码
b = s.encode('utf-8')  # 编码
print(b)

print(b.decode())  # 解码

# 首尾匹配
print('hello world'.startswith('hel'))  # 是否以指定字符串开头
print('hello world'.endswith('rld'))  # 是否以指定字符串结尾

# ASCII码 转换
print(chr(98))  # 'b'
print(ord('b'))  # 98

# eval(): 将字符串中的内容当作表达式运算
print(eval('1+3'))  # 4
print(eval('[1,2,3]'))  # [1, 2, 3] list

# 转义: \ 或 r'' 作用是将原本有语义的字符变成没有语义,原样输出
print('印度\n美国')
print('印度\\n美国')
print(r'C:\Users\tjeff\nesktop\Python2103')

# 简单加密
# t = str.maketrans("aco","123")
# str2 = "today is a good day"
# print(str2.translate(t))  # t3d1y is 1 g33d d1y

