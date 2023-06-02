#
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
scret = input('请输入需要检查的密码组合：')
symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

len_button = 0
content_button = 0

if len(scret)<=8:
    len_button = 0

if len(scret)>=8:
    len_button +=1

if len(scret)>=16:
    len_button +=2

for each in scret:
    if each in nums:
        print('包含数字')
        content_button +=1
        break

for each in scret:
    if each in chars:
        print('包含字符')
        content_button +=1
        break

for each in scret:
    if each in symbols:
        print('包含符号')
        content_button +=1
        if scret[0] in chars:
            content_button += 1
        break


if content_button ==2 and len_button == 1:
    print('你的密码安全级别评定为：中')
    print("请按以下方式提升您的密码安全级别：\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位")

if content_button ==3 and len_button == 2:
    print('你的密码安全级别评定为：高')
    print('请继续保持')
    
else:
    print('你的密码安全级别评定为：低')
    print("请按以下方式提升您的密码安全级别：\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位")



