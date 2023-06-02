#  求输入数字的平方，如果平方运算后小于 50 则退出。

# # 错误示范：
# sq = 0
# while sq < 50:
#     i = int(input('请输入一个数：'))
#     sq = i**2
#     print(sq)

# while True:
#     i = int(input('请输入一个数：'))
#     sq = i**2
#     print(sq)
#     if sq < 50:
#         print('打破循环')
#         break


while True:
    try:
        n = float(input('输入一个数字：'))
    except:
        print('输入错误')
        continue
    dn = n ** 2
    print('其平方为：', dn)
    if dn < 50:
        print('平方小于50，退出')
        break
