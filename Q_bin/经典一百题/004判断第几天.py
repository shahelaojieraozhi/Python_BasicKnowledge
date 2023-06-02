# # **题目4：**输入某年某月某日，判断这一天是这一年的第几天？
date = int(input('请输入日期(格式为19980302)：'))
year = int(date/10000)
print(year)
day = date % 100
mouth_day = date % 1000
mouth = mouth_day // 100
print(mouth)
print(day)
mouth_sum = 0
if (year/4) == int(year/4) and (year/400) == int(year/400):
     # 2月有29天
     daysum = (31,29,31,30,31,30,31,31,30,31,30,31)
     for i in range(mouth-1):
        mouth_sum = mouth_sum + daysum[i]
        sum = mouth_sum + day
    print('这一天是这一年的第：'+str(sum)+'天')
else:
     daysum = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
     for i in range(mouth - 1):
        mouth_sum = mouth_sum + daysum[i]
     sum = mouth_sum + day
     print('这一天是这一年的第：',sum,'天')

# 有问题