import re

# # 简单的Python匹配
# pattern1 = 'cat'
# pattern2 = 'bird'
# string = 'dog runs to cat'
# print(pattern1 in string)
# print(pattern2 in string)
# # True
# # False

# # 用正则寻找匹配
# pattern1 = 'cat'
# pattern2 = 'bird'
# string = 'dog runs to cat'
# print(re.search(pattern1, string))
# print(re.search(pattern2, string))
# # <re.Match object; span=(12, 15), match='cat'>
# # None

# # 匹配多种可能 使用[]
# ptn = r"r[au]n"
# print(re.search(ptn, 'dog runs to cat'))
# # <re.Match object; span=(4, 7), match='run'>

# # 匹配更多种可能
# print(re.search(r"r[A-Z]n", "dog runs to cat"))
# print(re.search(r"r[a-z]n", "dog runs to cat"))
# print(re.search(r"r[0-9]n", "dog r2ns to cat"))
# print(re.search(r"r[0-9a-z]n", "dog runs to cat"))
# # 输出：
# # # None
# # # <re.Match object; span=(4, 7), match='run'>
# # # <re.Match object; span=(4, 7), match='r2n'>
# # # <re.Match object; span=(4, 7), match='run'>


# # 一、特殊种类匹配
# # 1.1数字
# # \d:所有数字形式
# print(re.search(r"r\dn", "dog runs r4n"))
# # \D:所有不是数字的，跟上面相对
# print(re.search(r"r\Dn", "dog runs r4n"))
# # 输出：
# # <re.Match object; span=(4, 7), match='run'>
# # <re.Match object; span=(0, 3), match='r\nn'>


# # 1.2 空白
# # \s:匹配任何空白符号[\t \n \r \f \v]
# print(re.search(r"r\sn", "r\nn r4n"))
# # \D:匹配任何不是空白符号
# print(re.search(r"r\Sn", "r\nn r4n"))
# # 输出：
# # <re.Match object; span=(0, 3), match='r\nn'>
# # <re.Match object; span=(4, 7), match='r4n'>
#
# print('r\na')
# # r
# # a
# print('r\ta')
# # r	 a


# # 1.3 所有字母数字和‘_’
# # \w:包括【a-z A-Z 0-9】
# print(re.search(r"r\wn","r\nn r4n"))
# # \W:除了上面说的之外
# print(re.search(r"r\Wn","r\nn r4n"))
# # 输出：
# # <re.Match object; span=(4, 7), match='r4n'>
# # <re.Match object; span=(0, 3), match='r\nn'>


# # 1.4 找字符周围有空白的
# # \b:前后分别一个空格
# print(re.search(r"\bruns\b","dog runsto cat"))
# # \B:前后只要有空白格都能匹配
# print(re.search(r"\B runs \B","dog  runs  to cat"))
# # 输出：
# # None
# # <re.Match object; span=(4, 10), match=' runs '>


# # 1.5 特殊字符 任意字符
# # \\:找返斜杠
# print(re.search(r"runs\\","runs\ to me"))
# # .:这个点可以代表任何东西
# print(re.search(r"r.n","r[ns to me"))
# # 输出：
# # <re.Match object; span=(0, 5), match='runs\\'>
# # <re.Match object; span=(0, 3), match='r[n'>


# # 1.6 句尾句首
# # ^:匹配句首
# print(re.search(r"^dog","dog runs to cat"))
# # $:匹配句末
# print(re.search(r"cat$","dog runs to cat"))
# # 输出：
# # <re.Match object; span=(0, 3), match='dog'>
# # <re.Match object; span=(12, 15), match='cat'>


# # 1.7 是否
# # ?:不管是否有都匹配
# print(re.search(r"Mon(day)?","Monday"))
# print(re.search(r"Mon(day)?","Mon"))
# # 输出：
# # <re.Match object; span=(0, 6), match='Monday'>
# # <re.Match object; span=(0, 3), match='Mon'>

# # 1.8 多行匹配
# 输出：
# None
# <re.Match object; span=(18, 19), match='I'>

# # 1.9 0或者多次
# # * ：出现0次或者更多次
# print(re.search(r"ab*","a"))    # a+b的0次或者更多次
# # 多行匹配，每段话都是新的一行
# print(re.search(r"ab*","abbbbb"))
# # 输出：
# # <re.Match object; span=(0, 1), match='a'>
# # <re.Match object; span=(0, 6), match='abbbbb'>


# # 1.10 1或者多次
# # + ：出现1次或者更多次
# print(re.search(r"ab+","a"))    # a+b的0次或者更多次
# # 多行匹配，每段话都是新的一行
# print(re.search(r"ab+","abbbbb"))
# # 输出：
# # None
# # <re.Match object; span=(0, 6), match='abbbbb'>


# # 1.11 可选次数
# # {n,m} ：出现n次到m次
# print(re.search(r"ab{2,10}","a"))
# # 多行匹配，每段话都是新的一行
# print(re.search(r"ab{2,10}","abbbbb"))
# # 输出：
# # None
# # <re.Match object; span=(0, 6), match='abbbbb'>


# # 1.12 group 组
# # \d :描述数字
# match = re.search(r"(\d+),Date:(.+)","ID: 021523,Date:Feb/12/2017")
# # 返回所有内容
# print(match.group())
# # 返回第一个括号里面的东西
# print(match.group(1))
# # 返回第二个括号里面的东西
# print(match.group(2))
# # 输出：
# # 021523,Date:Feb/12/2017
# # 021523
# # Feb/12/2017

# # group 组
# # 当里面括号很多时  用?P<里面是命名的名字>
# match = re.search(r"(?P<id>\d+),Date:(?P<date>.+)","ID: 021523,Date:Feb/12/2017")
# print(match.group('id'))
# print(match.group('date'))
# # 输出：
# # 021523
# # Feb/12/2017


# # 寻找所有匹配
# # 1.findall
# print(re.findall(r"r[ua]n","run ran ren"))
# # 输出：['run', 'ran']
#
# # 2.|:or
# print(re.findall(r"run|ran","run ran ren"))
# # 输出：['run', 'ran']
#
# # 3.替换
# # re.sub() replace
# print(re.sub(r"r[au]ns","catches","dog runs to cat"))
# # 把r【au】ns找到然后替换成catches
# # 输出：dog catches to cat
#
# # 3.分裂
# # re.split()
# print(re.split(r"[,;\.]","a;b,c.d;e"))  # \是转义
# # 输出：['a', 'b', 'c', 'd', 'e']
#
# # 4.compile  分部操作
# complied_re = re.compile(r"r[ua]n")
# print(complied_re.search("dog ran to cat"))
# # 输出：['a', 'b', 'c', 'd', 'e']
