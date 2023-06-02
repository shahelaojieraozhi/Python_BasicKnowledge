import re

# 分组：()
# 捕获：获取分组中的内容

pattern = '((\d{4})-(\d{8}))'
s = '0755-88886666'
# r = re.search(pattern, s)
# print(r)
# print(r.group(1))  # 第一个分组：‘0755’
# print(r.group(2))  # 第二个分组：‘88886666’
# print(r.groups())  # 所有分组 ('0755', '88886666')

# findall()
print(re.findall(pattern, s))  # [('0755-88886666', '0755', '88886666')]

# 扩展：分组别名
# pattern = '(?P<abc>\d{4})-(?P<def>\d{8})'
# s = '0755-88886666'
# r = re.search(pattern, s)
# print(r.group(1))
# print(r.group('def'))

# 非捕获性分组: (?: )
pattern = '(?:\d{4})-(\d{8})'
s = '0755-88886666'
print(re.findall(pattern, s))


# 正则的其他方法
# 编译正则: 提高正则的匹配效率
# 先编译
com = re.compile('(\d{4})-(\d{8})')
# 再匹配
print(com.findall(s))


# finditer() ： 了解
ret = re.finditer('(\d{4})-(\d{8})', s)
# print(ret)
for i in ret:
    print(i.span(), i.group())

# split(): 拆分  了解
print(re.split('\d', 'abc1def2ghi3jkl4haha'))
# ['abc', 'def', 'ghi', 'jkl', 'haha']

# sub()  替换 了解
# subn()  替换
s = '10.hello,20.haha,30.你好'
print(re.sub('\d+', '#', s))  # '#.hello,#.haha,#.你好'
print(re.subn('\d+', '#', s))  # ('#.hello,#.haha,#.你好', 3)

