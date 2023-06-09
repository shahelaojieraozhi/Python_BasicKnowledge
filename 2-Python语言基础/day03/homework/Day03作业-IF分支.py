''''''
'''
    if分支语句实现
'''

''' 基础题 '''
# 1.x 为 0-99 取一个数, y 为 0-199 取一个数,
#   如果 x>y 则输出 x的值，
#   如果 x 等于 y 则输出 x+y的值，
#   否则输出y的值
import random
# n = random.randint(1,6)  # 随机取1~6中的某一个整数
x = random.randint(0, 99)  # 随机取0~99中的某一个整数
y = random.randint(0, 199)  # 随机取0~199中的某一个整数



# 2.从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”
# 该数的每一位的立方和等于自身的值,比如:153=1^3+5^3+3^3
# 	例如：153=1^3+5^3+3^3
# 	n = 153:
# 	个位：n%10
# 	十位：(n//10)%10
# 	百位：n//100

# 3.从控制台输入一个五位数，如果是回文数就打印“是回文数”，否则打印“不是回文数”
#  回文数: 对称的5位数
# 	例如：11111   12321   12221


# 4.从控制台输入两个数，输出较大的值

# 5,成绩判定,给一个成绩
# 	大于85  打印: 优秀
# 	大于等于75小于等于85 良好
# 	大于等于60小于75 及格
# 	小于60  不及格


''' 进阶题 '''
# 1,判断一个年份是闰年还是平年；
#  （1.能被4整除而不能被100整除.（如2004年就是闰年,1800年不是.）
#   2.能被400整除.（如2000年是闰年））
# 能整除: n%4 == 0

# 2,输入一个月份，然后输出对应月份有多少天，将天数输出(不考虑闰年)
# 比如：
# 输入 6 输出为30
# 输入 2 输出为28


# 3. 开发一款软件，根据公式（身高-108）*2=标准体重，可以有10斤左右的浮动。
# 来观察测试者体重是否合适, 输入真实身高(cm)，真实体重(斤)


# 4.模拟玩骰子游戏，根据骰子点数决定什么惩罚【例如：1.跳舞，2.唱歌....】
import random
n = random.randint(1,6)  # 随机取1~6中的某一个整数


''' 挑战题 (选做) '''
# 1.分别输入某年某月某日，判断这一天是这一年的第几天？（考虑闰年） (*****)
#     year, month， day
# 提示： 使用多个if单分支
year = int(input("年:"))
moth = int(input("月:"))
day = int(input("日:"))



# 2,输入一个时间，输出该时间的下一秒： (*****)
# 	如：23:59:59，
# 	输入：hour, min, sec
# 	输出 0: 0: 0
hour = int(input("时:"))
min = int(input("分:"))
sec = int(input("秒:"))



