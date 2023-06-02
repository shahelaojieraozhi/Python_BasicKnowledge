# 找水仙花数：
for number in range(100, 1000):
    x = number // 100 % 10  # x = number//100%10表示x取number的百位数
    y = number // 10 % 10
    z = number // 1 % 10
    if (x ** 3 + y ** 3 + z ** 3) == number:
        print(number)
    else:
        number += 1
print('在范围内没了')


for i in range(100, 10000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp % 10) ** 4
        temp //= 10  # 注意这里要使用地板除哦~
    if sum == i:
        print(i)
    # #水仙花数：四位的就要4次方幂的和
    # 我估计你感到困惑的应该是里面的while循环
    # while temp:
    #         sum = sum + (temp%10) ** 3
    #         temp //= 10
    #
    # temp % 10 得到的是temp这个值的个位数字，比如 111 % 10 == 1，234 % 10 == 4
    # (temp % 10) ** 3 表示这个数字的三次方，比如 2 ** 3 == 2 * 2 * 2 == 8
    # temp //= 10 表示temp右移1位，比如 123 // 10 == 12，234 // 10 == 23，地板除的意思是整除，只取整数部分而去掉小数部分
    # **********************************************************
    # 所以整个while循环的操作就是，拿temp=543举个例子
    # 第一次循环
    # sum = 0 + 3 ** 3 = 9
    # temp = 54
    # 第二次循环
    # sum = 9 + 4**3 = 9 + 64 = 73
    # temp = 5
    # 第三次循环
    # sum = 73 + 5**3 = 73 + 125 = 198
    # temp = 0
    # 第四次循环条件判定失败，跳出while循环，最终sum == 198
    # 后续的判定中sum ！= 543
    # 所以543不是水仙花数
