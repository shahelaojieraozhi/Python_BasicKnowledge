# **题目：**将一个整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# 错误
# number = int(input("输入你要分解的整数："))
# temp = number
# list1 = []
# for i in range(1, number):
#     if temp % (number - i) == 0:
#         list1.append(number - i)
#         temp = temp / (number - i)
#         print(number - i)
#         for j in range(1, temp):
#             if temp % (number - i) == 0:
#                 list1.append(number - i)
#                 temp = temp / (number - i)
#                 print(number - i)
#                 if temp % (number - i) == 0:
#                     list1.append(number - i)
#                     temp = temp / (number - i)
#                     print(number - i)
#
#     else:
#         i += 1


# 持续输出
target = int(input('输入一个整数：'))
print(target, '= ', end='')

if target < 0:
    target = abs(target)
    print('-1*', end='')

flag = 0
if target <= 1:
    print(target)
    flag = 1

while True:
    if flag:
        break
    for i in range(2, int(target + 1)):
        if target % i == 0:
            print("%d" % i, end='')
            if target == i:
                flag = 1
                break
            print('*', end='')
            target /= i
            break

