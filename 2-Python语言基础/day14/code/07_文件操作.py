
# 文件操作：
#   1.打开文件
#   2.操作文件：读read,写write
#   3.关闭文件

# 1. 打开文件
#  mode: 打开模式
#   r : read 只读，如果文件不存在则报错 （默认）
#   rb : 只读二进制，如果文件不存在则报错

#   w : write 清空写，如果文件不存在则创建
#   wb : 清空写二进制，如果文件不存在则创建

#   a : append 追加写，如果文件不存在则创建
#   ab : 追加写二进制，如果文件不存在则创建

#   r+ / rb+: 读+写

# fp: 文件句柄
# fp = open('a.txt')
# fp = open('a.txt', 'r', encoding='utf-8')
# fp = open('a.txt', 'rb')

# fp = open('a.txt', 'w')
# fp = open('b.txt', 'wb')

fp = open('a.txt', 'a')
# fp = open('a.txt', 'ab')

# 2. 操作文件
# 读
'''
# print(fp.read())  # 读取所有数据
# print(fp.read(3))  # 读取接下来的3个
# print(fp.read(7))  # 读取接下来的7个

# print(fp.readline())  # 读取1行
# print(fp.readline())  # 读取1行
# print(fp.readline())  # 读取1行

# print(fp.readlines())  # 读取所有行，列表
'''

# 写
# fp.write('hello\nabc\n')
fp.write('我'.encode())


# 3.关闭文件
fp.close()


# r+ 不推荐
# fp = open('a.txt', 'r+', encoding='utf-8')
# print(fp.read())
# fp.write('hhhh')
# fp.close()

