# 1. 假设本周的上课时间为156789秒，
#   编程计算本周上课时间是多少天, 多少小时，多少分钟，多少秒；以‘XX天XX时XX分X秒’的方式表示出来。
n = 156789
day = n // (60*60*24)
hour = n // (60*60) % 24
minute = n // 60 % 60
second = n % 60
print(f'{day}天{hour}时{minute}分{second}秒')

# 2. 写出判断一个数是否能同时被3和7整除的条件语句, 并且打印对应的结果
n = 21
if n%3==0 and n%7==0:
    print(True)
else:
    print(False)

# 3. 写出判断一个数是否能够被3或者7整除，但是不能同时被3和7整除的条件语句， 并且打印对应的结果
n = 33
if (n%3==0 or n%7==0) and n%21!=0:
    print(True)
else:
    print(False)

# 4. 定义两个变量保存一个人的身高和体重，编程实现判断这个人的身材是否正常!
#     公式: `体重(kg)/(身高(m)的平方值)` 在18.5 ~ 24.9之间属于正常。
height = 1.8
weight = 75
if 18.5 <= weight/(height**2) <= 24.9:
    print("正常")
else:
    print("不正常")

