temp = input('请输入一个年份：')
while not temp.isdigit():
    temp = input("抱歉，您的输入有误，请输入一个整数：")
year = int(temp)
if year % 400 == 0:
    print(temp + '年为闰年')
else:
    if (year%4 == 0) and (year%100 != 0):
        print(temp + '年为闰年')
    else:
        print(temp + '年不是闰年')
# 请输入一个年份：2021
# 2021年不是闰年
