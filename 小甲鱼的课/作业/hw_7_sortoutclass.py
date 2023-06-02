# 题目备忘：
# 按照 100 分制，90 分以上成绩为 A，80 到 90 为 B，60 到 80 为 C，60 以下为 D，
# 写一个程序，当用户输入分数，自动转换为 A B C D 的形式打印。
temp = input('请输入一个分数：')
while temp.isdigit() == 0:
    print("抱歉，输入不合法，", end='')
    temp = input("请输入一个整数：")
score = int(temp)
if 80 > score >= 60:
    print('C')
elif 90 > score >= 80:
    print('B')
elif 60 > score >= 0:
    print('D')
elif 100 >= score >= 90:
    print('A')
else:
    print('输入错误！，请输入0-100内的数')

# #题目备忘：
# #按照 100 分制，90 分以上成绩为 A，80 到 90 为 B，60 到 80 为 C，60 以下为 D，
# #写一个程序，当用户输入分数，自动转换为 A B C D 的形式打印。
# temp = input('请输入分数：')
# score = int(temp)
# if 80 > score >= 60:
#     print('C')
# elif 90 > score>= 80:
#     print('B')
# elif 100>=score>=90:
#     print('A')
# else:
#     print('D')
