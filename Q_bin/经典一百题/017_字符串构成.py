# **题目：**输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
str_input = input("输入一行字符：")
int_count = 0
str_count = 0
space_count = 0
other_count = 0

for i in str_input:
    # 判断是否为数字
    if i.isdigit():
        int_count += 1
    # 判断是否为字母
    elif i.isalnum():
        str_count += 1
    # 判断是否为空格
    elif i.isspace():
        space_count += 1
    # 判断为其他字符
    else:
        other_count += 1
print('数字 = %d, 字母 = %d，空格 = %d，其他 = %d' % (int_count, str_count, space_count,other_count))
# 输入一行字符：打卡机多久4234 wtu……*￥*￥
# 数字 = 4, 字母 = 8，空格 = 1，其他 = 6


# # 参考
# string = input("输入字符串：")
# alp = 0
# num = 0
# spa = 0
# oth = 0
# for i in range(len(string)):
#     if string[i].isspace():
#         spa += 1
#     elif string[i].isdigit():
#         num += 1
#     elif string[i].isalpha():
#         alp += 1
#     else:
#         oth += 1
# print('space: ', spa)
# print('digit: ', num)
# print('alpha: ', alp)
# print('other: ', oth)
