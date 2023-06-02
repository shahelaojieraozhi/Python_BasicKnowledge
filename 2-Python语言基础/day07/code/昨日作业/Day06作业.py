''''''

'''
    for循环题目
'''
''' 基础题 '''
# 1,打印100以内7的倍数
for i in range(101):
    if i%7 == 0:
        print(i)

# 2,打印100以内的奇数
for i in range(1, 101, 2):
    print(i)

# 3,打印100以内所有偶数的和
print(sum(range(0, 101, 2)))

# 4,判断一个数是不是合数。(指自然数中除了能被1和本身整除外，还能被其他的数整除（不包括0)的数。)
# 5,判断一个数是不是素数。(除了1和它本身以外不再有其他的除数整除。)
n = 10889
for i in range(2, n):
    if n%i == 0:
        print(n, '是合数')
        break
else:
    print(n, '是素数')

# 6,求整数1～100的累加值，但要求跳过所有个位为3的数。
s = 0
for i in range(1, 101):
    # if i%10 == 3:
    #     continue
    # s += i

    if i%10 != 3:
        s += i
print(s)

# 7, 一个新入职，月工资为10000元的员工，每年涨当年工资5%，20年后的月工资是多少？
salary = 10000
print(salary * 1.05**20)

salary = 10000
for i in range(20):
    salary = salary + salary*0.05
print(salary)

# 8, 山上有一口缸可以装50升水，现在有15升水。老和尚叫小和尚下山挑水，每次可以挑5升。
#    问：小和尚要挑几 次水才可以把水缸挑满？通过循环解决这个问题。
count = 0
for i in range(15, 50, 5):
    count += 1
print(count)

count = 0
x = 15
while x < 50:
    count += 1
    x += 5
print(count)

# 9, 打印100–200之间所有能被3或者7整除的数
for i in range(100, 201):
    if i%3==0 or i%7==0:
        print(i)

# 10, 计算10的阶乘(1*2*3*4*5*6*7*8*9*10, n的阶乘:1*2……*n)
import math
print(math.factorial(10))

# 11, 计算1+3+5+...+99的和
print(sum(range(1, 100, 2)))

# 12, 输出20~80之间能被3整除的整数, 每行5个
count = 0
for i in range(20, 81):
    if i%3 == 0:
        print(i, end=' ')

        count += 1
        if count % 5 == 0:
            print()

# 13, 打印1000~2000年中所有的闰年, 每行4个
count = 0
for i in range(1000, 2001):
    if i%4==0 and i%100 !=0 or i%400==0:
        print(i, end=' ')
        count += 1
        if count%4 == 0:
            print()
print()

# 14, 求: 1-1/2+1/3-1/4 …  1/100的和
#   提示: 1/1-1/2+1/3-1/4 …  1/100
s = 0
for i in range(1, 101):
    if i % 2:
        s += 1/i
    else:
        s -= 1 / i
print(s)

# 15, 输出99乘法表
'''
1 * 1 = 1
1 * 2 = 2	2 * 2 = 4
1 * 3 = 3	2 * 3 = 6	3 * 3 = 9
1 * 4 = 4	2 * 4 = 8	3 * 4 = 12	4 * 4 = 16
1 * 5 = 5	2 * 5 = 10	3 * 5 = 15	4 * 5 = 20	5 * 5 = 25
1 * 6 = 6	2 * 6 = 12	3 * 6 = 18	4 * 6 = 24	5 * 6 = 30	6 * 6 = 36
1 * 7 = 7	2 * 7 = 14	3 * 7 = 21	4 * 7 = 28	5 * 7 = 35	6 * 7 = 42	7 * 7 = 49
1 * 8 = 8	2 * 8 = 16	3 * 8 = 24	4 * 8 = 32	5 * 8 = 40	6 * 8 = 48	7 * 8 = 56	8 * 8 = 64
1 * 9 = 9	2 * 9 = 18	3 * 9 = 27	4 * 9 = 36	5 * 9 = 45	6 * 9 = 54	7 * 9 = 63	8 * 9 = 72	9 * 9 = 81
'''
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j} * {i} = {i*j}', end='\t')
    print()

'''
    字典题目
'''
# 1. 声明一个字典保存一个学生的信息，学生信息中包括:
#       姓名、年龄、成绩(单科)、电话、性别(男、女、不明)
stu_info = {'name': '张三', 'age': 18, 'score': 88, 'tel': 18866669999, 'sex': '不明'}

# 2. 声明一个列表，在列表中保存6个学生的信息(6个(题1)中的字典)
stu_list = [
    {'name': '刘一', 'age': 18, 'score': 8, 'tel': 18866669999, 'sex': '男'},
    {'name': '陈二', 'age': 13, 'score': 88, 'tel': 17777778888, 'sex': '不明'},
    {'name': '张三', 'age': 9, 'score': 99, 'tel': 18866669999, 'sex': '不明'},
    {'name': '李四', 'age': 20, 'score': 77, 'tel': 16666667778, 'sex': '不明'},
    {'name': '王五', 'age': 80, 'score': 55, 'tel': 18866669999, 'sex': '女'},
    {'name': '赵六', 'age': 60, 'score': 99, 'tel': 18866669999, 'sex': '不明'},
]
#   (1) 统计不及格学生的个数
#   (2) 打印不及格学生的名字和对应的成绩
#   (3) 统计未成年学生的个数
#   (4) 打印手机尾号是8的学生的名字
'''
count1 = 0  # 不及格学生的个数
count2 = 0  # 未成年学生的个数
for stu in stu_list:
    if stu['age'] < 18:
        count2 += 1
    if stu['score'] < 60:
        count1 += 1
        print('不及格学生的名字和对应的成绩:', stu['name'], stu['score'])
    if stu['tel'] % 10 == 8:
        print('手机尾号是8的学生的名字:', stu['name'])

print('不及格学生的个数:', count1)
print('未成年学生的个数:', count2)
'''

#   (5) 打印最高分和对应的学生的名字
# max_score = max(stu_list, key=lambda stu:stu['score'])['score']
# print(max_score)

# max_score = stu_list[0]['score']
# for stu in stu_list:
#     if stu['score'] > max_score:
#         max_score = stu['score']
# print(max_score)

score_list = []
for stu in stu_list:
    score_list.append(stu['score'])
max_score = max(score_list)
print("max_score:", max_score)

for stu in stu_list:
    if stu['score'] == max_score:
        print(stu['name'])

# 时间复杂度
# 空间复杂度

#   (6) 删除性别不明的所有学生(选做)
stu_list = [
    {'name': '刘一', 'age': 18, 'score': 8, 'tel': 18866669999, 'sex': '男'},
    {'name': '陈二', 'age': 13, 'score': 88, 'tel': 17777778888, 'sex': '不明'},
    {'name': '张三', 'age': 9, 'score': 99, 'tel': 18866669999, 'sex': '不明'},
    {'name': '李四', 'age': 20, 'score': 77, 'tel': 16666667778, 'sex': '不明'},
    {'name': '王五', 'age': 80, 'score': 55, 'tel': 18866669999, 'sex': '女'},
    {'name': '赵六', 'age': 60, 'score': 99, 'tel': 18866669999, 'sex': '不明'},
]
i = 0
while i < len(stu_list):
    stu = stu_list[i]

    if stu['sex'] == '不明':
        stu_list.pop(i)
        i -= 1
    i += 1

# 打印
for stu in stu_list:
    print(stu)
print()

#   (7) 将列表按学生成绩从大到小排序(难,选做)
    # 提示:
    # 方式一: 排序算法
    # 方式二: sort(key=)

stu_list = [
    {'name': '刘一', 'age': 18, 'score': 8, 'tel': 18866669999, 'sex': '男'},
    {'name': '陈二', 'age': 13, 'score': 88, 'tel': 17777778888, 'sex': '不明'},
    {'name': '张三', 'age': 9, 'score': 99, 'tel': 18866669999, 'sex': '不明'},
    {'name': '李四', 'age': 20, 'score': 77, 'tel': 16666667778, 'sex': '不明'},
    {'name': '王五', 'age': 80, 'score': 55, 'tel': 18866669999, 'sex': '女'},
    {'name': '赵六', 'age': 60, 'score': 99, 'tel': 18866669999, 'sex': '不明'},
]

stu_list.sort(key=lambda x: x['score'], reverse=True)

# 打印
for stu in stu_list:
    print(stu)

# 请写出你对今天授课内容最疑惑的地方(或者有困难的知识点)
