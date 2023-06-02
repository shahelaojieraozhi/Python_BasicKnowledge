''''''
''' 基础题 '''
# 1.已知字符串：“this is a test of Python”
# 	a.统计该字符串中字母s出现的次数: count()
# 	b.取出子字符串“test”, 用切片,不能数: 使用find(),len()
# 	c.采用不同的方式将字符串倒序输出: 切片，循环
# 	d.将其中的"test"替换为"exam" : replace
s = 'this is a test of Python'
print(s.count('s'))

sub_string = 'test'
i = s.find(sub_string)
print(s[i: i+len(sub_string)])

print(s[::-1])
l = ''.join(reversed(s))
print(l)
s2 = ''
for n in s:
    s2 = n + s2
print(s2)

print(s.replace('test', 'exam'))
print(s)  # this is a test of Python

# 2.去掉字符串123@zh@qq.com中的@;
# 提示: replace
s = '123@zh@qq.com'
print(s.replace('@', ''))

print(''.join(s.split('@')))


''' 进阶题 '''
# 1.已知字符串 s = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
# 	a.请将s字符串的大写改为小写，小写改为大写: swapcase()
# 	b.请将s字符串的数字取出，并输出成一个新的字符串: 循环，isdigit()
s = "aAsmr3idd4bgs7Dlsf9eAF"
print(s.swapcase())

s2 = ''
for c in s:
    if c.isdigit():
        s2 += c
print(s2)

# 	c.请统计s字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），
# 	    并输出成一个字典。 例 d = {'a':2,'s':1, 'm':1}
#       提示：循环,判断字符是否在字典中 'a' in d
s = "aAsmr3idd4bgs7Dlsf9eAF"
s2 = s.lower()

d = {}
for c in s2:
    if c.isalpha():
        if c in d:
            # 第二次或之后加入字典,将原来的次数+1
            d[c] = d[c] + 1
        else:
            # 第一次加入字典
            d[c] = 1
print(d)

# 	d.输出s字符串出现频率最高的字母, 如果有多个最高,将每个都输出: max(d.values()),再循环
max_count = max(d.values())
# print(max_count)
for k,v in d.items():
    if v == max_count:
        print(k)

# 	e.请判断'boy'字符串中的每一个字母，是否都出现在s字符串里。
# 	    如果出现，则输出True，否则，则输出False
s = "aAsmr3idd4bgs7Dlsf9eAF"
sub_s = 'boy'
for c in sub_s:
    if c not in s:
        print(False)
        break
else:
    print(True)

# 2.将字符串按照单词进行逆序，空格作为划分单词的唯一条件
#      如传入:”Welome to Beijing”改为 “Beijing to Welcome”
s = 'Welome to Beijing'
# split, reverse, join
l = s.split()
print(' '.join(l[::-1]))


''' 挑战题 '''
# 1.输入一个字符串，压缩字符串如下aabbbccccbbd变成a2b5c4d1
s = 'aabbbccccbbd'
#  a2b5c4d1
# count()
s2 = ''
for c in s:
    if c not in s2:
        s2 += c + str(s.count(c))
print(s2)


# 2,将字符中单词用空格隔开
#       已知传入的字符串中只有字母,每个单词的首字母大写，
#       请将每个单词用空格隔开，只保留第一个单词的首字母大写
#       传入:”HelloMyWorld”
#       返回:”Hello my world”

s = 'HelloMyWorld'
s2 = s[0]
for i in range(1, len(s)):
    c = s[i]
    if c.isupper():
        s2 += ' ' + c.lower()
    else:
        s2 += c
print(s2)


# 请写出你对今天授课内容最疑惑的地方(或者有困难的知识点)


