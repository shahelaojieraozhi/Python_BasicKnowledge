

# b.判断闰年
def fb(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    return False

# c.判断某月的总天数
def fc(year, month):
    days = 31
    if month == 2:
        if fb(year):
            days = 29
        else:
            days = 28
    elif month in [4, 6, 9, 11]:
        days = 30
    return days

# d.计算 某年距离1900年1月1日的总天数
def fd(year):
    s = 0
    for i in range(1900, year):
        if fb(i):
            s += 366
        else:
            s += 365
    return s

# e.计算 某月距离当年1月1日的总天数
def fe(year, month):
    s = 0
    for i in range(1, month):
        s += fc(year, i)
    return s

# f. d+e
def ff(year, month):
    return fd(year) + fe(year, month)

# g.求星期几
def fg(year, month):
    s = ff(year, month)
    week = (s+1) % 7
    return week

# h.格式化输出
def fh(year, month):
    week = fg(year, month)
    print('week:', week)
    # 格式化输出
    print('星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六', sep='\t')
    # 先打印空格
    for i in range(week):
        print(' ', end='\t\t')

    # 再打印当月的每天的数字
    for i in range(1, fc(year, month)+1):
        print(i, end='\t\t')
        # 换行
        if (week + i) % 7 == 0:
            print()

# a.输入年月
def fa():
    year = int(input('输入年:'))
    month = int(input('输入月:'))

    fh(year, month)

fa()
