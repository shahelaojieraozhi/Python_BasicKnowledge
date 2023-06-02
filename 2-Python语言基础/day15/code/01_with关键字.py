
# with关键字
#   1. 会自动关闭文件，我们不用写close()
#   2. 就算中间报错了，也会自动关闭文件
with open('a.txt', 'w', encoding='utf-8') as fp:
    fp.write('hello')


# with open('b.txt', 'r') as fp:
#     print(fp.read())

# 如果要防止打开文件时文件不存在而报错，则可以使用try-except
fp2 = None
try:
    fp2 = open('c.txt', 'r')
    a = 1/0
    print(fp2.read())
except:
    print('报错了')
finally:
    if fp2:
        print('关闭文件')
        fp2.close()

