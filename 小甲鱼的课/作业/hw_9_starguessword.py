i = 3
# while True:
#         code = input('密码中不能出现' * ',你还有3次机会！请输入密码：')
while i:
    temp = input('请输入密码：')
    if temp == 'raozhizhenshuai':
        print('密码正确，进入程序......')
        break
    elif '*' in temp:
        print('密码中不能出现 "*" ,你还有', i, '次机会！', end='')
        continue
    else:
        print('密码输入有错误，你还有', i - 1, '次', end='')
    i -= 1
print('请耐心等待！！！')


count = 3
password = 'raozhizhenshuai'

while count:
    passwd = input('请输入密码：')
    if passwd == password:
        print('密码正确，进入程序......')
        break
    elif '*' in passwd:
        print('密码中不能含有"*"号！您还有', count, '次机会！', end=' ')
        continue
    else:
        print('密码输入错误！您还有', count - 1, '次机会！', end=' ')
count -= 1


#   0. 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内。
i = 3
scret = '饶治真帅'
while i:
    temp = input('请输入密码：')
    if temp == scret:
        print('太厉害了，程序启动中.....')
    elif '*' in temp:
        print('输入"*"不算，你还有', i, '次机会，', end='')
        temp == input('请重新输入：')
    else:
        print('输入错误，还有', (i - 1), '次机会')
print('机会用完了')
