"""
应用场景：
    1、猜大小 ——》反复的猜
    2、消消乐 ——》反复充值
    3、用户登录 ——》登录多次

for 变量名 in 集合：
    语句
怎么用？

"""
# # 打印三次：
# for i in range(3):
#     print('hello!')

'''
吃馒头：在第三个馒头上抹了一点"鹤顶红"
for 里面加if语句
'''
# print('*'*30)
# name = '张无忌'
#
# for i in range(1, 6):
#     # 判断i的值是多少，i == 3别吃
#     if i == 3:
#         print('{}赶紧扔掉馒头3，有剧毒'.format(name))
#         # break
#     else:
#         print('{}很饿，正在吃第{}馒头'.format(name, i))
# print('{}说：终于吃饱啦！'.format(name))


'''
python 独有的：
for 。。。。。else
else：适用于for执行完或者没有循环数据时

语法：
for i in 范围:
    有数据执行的语句
else:
    没有数据执行的语句
'''
# name = '张无忌'
# num = int(input('请输入需要的馒头的数量：'))
# for i in range(num):
#     print('{}很饿，正在吃第{}馒头'.format(name, i+1))
# else:
#     print('还没给我馒头，{}饿哭了'.format(name))
# # for 执行完（集合里没数了）开始执行完、else....
# print('-----------')

'''
pass 空语句(占坑位，不让报错)
只要有缩进而缩进的内容还不确定的时候，此时为了保证语法的正确性，就可以使用pass占位
不会报出语法的错误
作用： 写伪代码时，先把架构写出来然后再往里面加东西
'''
# if 10 > 7:
#     print('10是大的')
# else:
#     pass
#
# print('----判断结束')

'''
break  关键字
使用背景：用户的账号密码登录而且只能登陆三次，如果三次未成功账户锁定

对于 for  else 结构：
break 直接跳出for的结构（跳出for -else 的结构）
'''
# for i in range(3):
#     username = input('请输入用户名：')
#     password = input('请输入密码：')
#     # 验证用户和密码
#     if username == 'raozhi' and password == '123':
#         print('登陆成功！！！')
#         print('-------------轻松购物吧-------------')
#         break   # 强制退出for，继续执行下方同级代码 （对齐）
#     else:
#         if i == 2:
#             print('账户被锁定，需要重新激活')
#         else:
#             print('用户名或者密码错误')

# # 对比一下：
# for i in range(3):
#     username = input('请输入用户名：')
#     password = input('请输入密码：')
#     # 验证用户和密码
#     if username == 'raozhi' and password == '123':
#         print('登陆成功！！！')
#         print('-------------轻松购物吧-------------')
#         break   # 强制退出for，继续执行下方同级代码 （对齐）
#     else:
#         print('用户名或者密码错误')
# else:
#     print('账户被锁定，需要重新激活')
#

for i in range(3):
    if i == 1:
        print('这家店是黑店，馒头有毒！等着关门吧')
        break
        print('abcd')   # 即使有语句也不会执行，干脆别写了
    else:
        print('这家店的馒头真香，要多吃几个呀！')
print('_____>进入消协大门')

# else:
#     print('dadadawdwadwa')
# range的范围正常执行完毕，而没有异常break跳出，就可以执行else， 只要有break
# 执行了就不会执行else.

