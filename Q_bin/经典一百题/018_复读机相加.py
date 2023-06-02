# **题目：**求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
num_input = int(input("请输入一个数字："))
a = num_input
times_input = int(input("请输入次数："))
list1 = [a]
print(a)
for i in range(0, times_input):
    num_input = num_input * 10 + a
    print(num_input)
    list1.append(num_input)
print('复读机相加：', sum(list1))
