# # 1、insert str
# str = '饶治真他妈帅'
# str1 = str[:5] + '不' + str[5:]
# print('1、', end='')
# print(str1)
# # 1、饶治真他妈不帅


# # 2、 extract str
# str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
# str2 = str1[16:29]
# print('2、',end='')
# print(str2)
# # 负索引  str1[20:-36]
# # 输出：
# # 2、www.fishc.com

# # 3、str[起始位：结束位：步长]
# str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
# str2 = str1[::3]
# print('3、',end='')
# print(str2)
# # 3、ilovefishc.com


# #####################大题############################
# # 密码安全性检查代码
# #
# # 低级密码要求：
# #   1. 密码由单纯的数字或字母组成
# #   2. 密码长度小于等于8位
# #
# # 中级密码要求：
# #   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
# #   2. 密码长度不能低于8位
# #
# # 高级密码要求：
# #   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
# #   2. 密码只能由字母开头
# #   3. 密码长度不能低于16位
# scret = input('请输入需要检查的密码组合：')
# symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
# chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# nums = '0123456789'
# len_button2 = 0
# content_button = 0
# # if len(scret) < 8:
# #     len_button1 = 0
# if len(scret) >= 8:
#     len_button2 += 1
# if len(scret) >= 16:
#     len_button2 += 1
#
# for each in scret:
#     if each in nums:
#         print('包含数字')
#         content_button += 1
#         break
# for each in scret:
#     if each in chars:
#         print('包含字符')
#         content_button += 1
#         break
# for each in scret:
#     if each in symbols:
#         print('包含符号')
#         content_button += 1
#         if scret[0] in chars:
#             content_button += 1
#         break
# if content_button == 2 and len_button2 == 1:
#     print('你的密码安全级别评定为：中')
#     print("请按以下方式提升您的密码安全级别：\n\
#     \t1. 密码必须由数字、字母及特殊字符三种组合\n\
#     \t2. 密码只能由字母开头\n\
#     \t3. 密码长度不能低于16位")
# elif content_button == 4 and len_button2 == 2:
#     print('你的密码安全级别评定为：高')
#     print('请继续保持')
# else:
#     print('你的密码安全级别评定为：低')
#     print("请按以下方式提升您的密码安全级别：\n\
#     \t1. 密码必须由数字、字母及特殊字符三种组合\n\
#     \t2. 密码只能由字母开头\n\
#     \t3. 密码长度不能低于16位")


#      *********************参考答案************************
# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

passwd = input('请输入需要检查的密码组合：')

# 判断长度
length = len(passwd)

while (passwd.isspace() or length == 0):
    passwd = input("您输入的密码为空（或空格），请重新输入：")
    length = len(passwd)

if length <= 8:
    flag_len = 1
elif 8 < length < 16:
    flag_len = 2
else:
    flag_len = 3

flag_con = 0

# 判断是否包含特殊字符
for each in passwd:
    if each in symbols:
        flag_con += 1
        break

# 判断是否包含字母
for each in passwd:
    if each in chars:
        flag_con += 1
        break

# 判断是否包含数字
for each in passwd:
    if each in nums:
        flag_con += 1
        break

    # 打印结果
while 1:
    print("您的密码安全级别评定为：", end='')
    if flag_len == 1 or flag_con == 1:
        print("低")
    elif flag_len == 3 and flag_con == 3 and (passwd[0] in chars):
        print("高")
        print("请继续保持")
        break
    else:
        print("中")

    print("请按以下方式提升您的密码安全级别：\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位")
    break