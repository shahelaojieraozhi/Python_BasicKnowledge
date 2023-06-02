# **题目：**求100之内的素数。
# **程序分析：**用else执行for循环的奖励代码（如果for是正常完结，非break）。
# shift 加 tab 撤回一次缩进
target = 100
flag = 0
for j in range(2, target + 1):
    for i in range(2, target + 1):
        if j % i == 0:
            flag += 1
            if flag < 2:
                print("%d" % i)

