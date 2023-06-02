''''''
# 1.判断下面标识符是否合法并说明不合法的原因
# 	@abc.com   =>  False
# 	123ok      =>  False
# 	_xiaoming  =>  True
# 	Xiaoming_$ =>  False
# 	interface  =>  True
# 	sina@163   =>  False


# 2.从控制台输入圆的半径，计算周长和面积, π=3.14
# pi = 3.14
# r = int(input('请输入半径:'))
# c = 2 * pi * r
# s = pi * r * r
# print(c, s)

# 3.一辆汽车以40km/h的速度行驶,行驶了4567.89km,求所用的时间
speed = 40
length = 4567.89
t = length / speed
print(t)

# 4.华氏温度转摄氏温度
# 【提示：将华氏温度转换为摄氏温度(F是华氏温度)  F = 1.8C + 32】
# C = (F - 32)/1.8
F = 213.8
C = (F - 32) / 1.8
print(C)

# 5, 入职薪水10K，每年涨幅入职薪水的5%，50年后工资多少？
salary = 10
salary2 = salary + salary*0.05 * 50
print(salary2)  # 35K

# 6, 为抵抗洪水，战士连续作战89小时，编程计算共多少天零多少小时？
hours = 89
day = hours // 24
hour = hours % 24
print(f'{day}天{hour}小时')

# 7, 给定一个5位数，分别把这个数字的万位，千位，百位、十位、个位算出来并显示。如： 34567
n = 34567
a = n // 10000  # 万位
b = n // 1000 % 10  # 千位
c = n // 100 % 10  # 百位
d = n // 10 % 10  # 十位
e = n % 10  # 个位
print(a, b, c, d, e)


# 总共有5678秒, 转换成多少小时,多少分钟, 多少秒
t = 5678
h = t // (60*60)  # 小时
m = t // 60 % 60  # 分钟
s = t % 60  # 秒
print(h, m, s)


# 扩展: 总共有456789秒, 转换成多少天,多少小时,多少分钟, 多少秒




