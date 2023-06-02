''''''

'''
【以下功能都使用函数封装】
提示: 涉及到要返回的题目,请使用return
'''

''' 基础题 '''
# 1.封装函数，计算从1到某个数以内所有奇数的和并返回
def fn1(n):
    return sum(range(1, n+1, 2))

# 2.封装函数，判断某个数是否是偶数，返回结果(True或False)
def fn2(n):
    return n%2==0

# 3.封装函数，交换某两个变量的值, 并返回结果
def fn3(a, b):
    return b, a

# x = fn3(2, 3)
# print(x, type(x))
x, y = fn3(4, 5)  # x, y = (5, 4)
print(x, y)  # x=5, y=4

# 4,封装函数，将某个字符串中的大写字母转换为小写，小写字母转换为大写，将新的字符串返回【参数设置为默认参数】
# swapcase()
def fn4(s='fsafQeERWEFDdfs'):
    return s.swapcase()


''' 进阶题 '''
# 1.封装函数，比较某两个数的大小，返回较大的一个

# 2.封装函数，判断某个数是否是素数，返回结果(True或False)

# 3.封装函数，计算2-100之间素数的个数，返回结果


''' 挑战题 '''
# 1,封装函数，实现如下要求
# 	例如：输入2，5，则求 2+22+222+2222+22222的和
def fun1(a, n):
    s = 0
    temp = 0
    for i in range(n):
        temp = temp*10 + a
        s += temp
    return s

result = fun1(2, 5)
print(result)
# fun1(3, 4)


# 2,已知千锋邮箱的用户名只能由数字字母下划线组成，域名为@1000phone.com,
#    封装函数 is_legal_email，判断一个字符串是否是千锋邮箱，是返回True，不是返回False。
#      mail@1000phone.com  是
#      $mail@1000phone.com  不是
#      mail@1000phone.comp  不是
#
# 提示：先找出所有False的情况
#      最后剩下的情况就是True

def is_legal_email(s):
    list1 = s.split('@')
    # print(list1)  # ['mail', '1000phone.com']
    if len(list1) != 2:
        return False

    if list1[1] != '1000phone.com':
        return False

    s2 = list1[0]  # 'mail'
    for c in s2:
        if c.isalnum() or c=='_':
            continue
        return False

    return True


result = is_legal_email('ma123_i_l@1000phone.com')
print(result)

# 请写出你对今天授课内容最疑惑的地方(或者有困难的知识点)










