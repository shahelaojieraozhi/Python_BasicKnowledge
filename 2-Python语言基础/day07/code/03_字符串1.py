
# 字符串: str   String
#   使用引号包裹的就是字符串

# 基本操作
# 1.创建字符串
s = '亲,买房吗'

# 2.索引
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[-1])

# 3.长度
print(len(s))

# 4.遍历
for c in s:
    print(c)
for i in range(len(s)):
    print(i)
for i,c in enumerate(s):
    print(i, c)

# 5.切片
s = 'helloworld'
print(s[2:7])
print(s[::-1])

# 6.合并
print("hello" + " 印度")

# 7.重复
print(s * 3)

# 8.成员
print("llo" in s)

# 9.删除
#   字符串是不可变的
s = 'hello'
s = s + '你好'
print(s)

# del s[0]
# s[0] = 'a'
