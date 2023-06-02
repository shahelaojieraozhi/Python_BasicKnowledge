# #  a b c是关键字参数
# str1 = "{a} love {b}.{c}".format(a="I", b="FishC", c="com")
# print(str1)
# # I love FishC.com
#
# #   0 1 2是位置参数
# str2 = "{0} love {1}.{2}".format("I", "FishC", "com")
# print(str2)
# # I love FishC.com
#
# #   想要显示Pi = 3.14
# str3 = '{0}{1:.2f}'.format('Pi = ', 3.1415)
# print(str3)
# # Pi = 3.14

#   编写一个进制转换程序
#   重复执行程序：
q = True
while q:
    num = input('请输入一个整数(输入Q结束程序)：')
    if num != 'Q':
        num = int(num)
        print('十进制 -> 十六进制 : %d -> 0x%x' % (num, num))
        print('十进制 -> 八进制 : %d -> 0o%o' % (num, num))
        print('十进制 -> 二进制 : %d -> ' % num, bin(num))
    else:
        q = False
# 请输入一个整数(输入Q结束程序)：52
# 十进制 -> 十六进制 : 52 -> 0x34
# 十进制 -> 八进制 : 52 -> 0o64
# 十进制 -> 二进制 : 52 ->  0b110100
# 请输入一个整数(输入Q结束程序)：
