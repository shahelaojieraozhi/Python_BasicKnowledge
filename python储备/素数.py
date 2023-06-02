# 需求;判断一个数是否是素数【质数】
# 方式一
num1 = int(input("请输入一个数："))
# 思路：一个数能被其他数整除，将次数记录下来
# 条件：在2~num1 - 1的范围内，找到一个数能将num1整除，count1 + 1
count1 = 0
for i in range(2,num1):
    # 整除：求余【大数对小数求余】
    if num1 % i == 0:
        count1 += 1

if count1 == 0 and num1 != 1:
    print("是质数")
else:
    print("不是质数")

# # 方式二：
# # 思路：假设num2是质数，寻找不成立的条件【有数能被整除】将假设推翻掉
# num2 = int(input("请输入一个数："))
# # 定义一个布尔类型的变量，用于记录这个数是不是一个质数
# is_prime  = True
# for j in range(2,num2):
#     if num2 % j == 0:
#         is_prime = False
#         break
#
# if is_prime == True and num2 != 1:
#     print("是质数")
# else:
#     print("不是质数")


