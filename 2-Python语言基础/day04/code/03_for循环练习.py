
# 1.求1-100之间可以被7整除的数的个数
count = 0
for i in range(1, 101):
    if i%7 == 0:
        count += 1

# 2.计算从1到100以内所有奇数的和。
s = 0
for i in range(1, 101, 2):
    s += i

# 3.计算从1到100以内所有能被3或者17整除的数的和。
s = 0
for i in range(1, 101):
    if i%3==0 or i%17==0:
        s += i

# 4.计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数。
count = 0
for i in range(1, 101):
    if (i%7==0 or i%3==0) and i%21!=0:
        count += 1

# 5.计算1到500以内能被7整除但不是偶数的数的个数。
count = 0
for i in range(1, 501):
    if i%7==0 and i%2!=0:
        count += 1

