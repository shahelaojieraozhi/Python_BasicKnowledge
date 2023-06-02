
# Python循环: while, for-in

# range(start, stop, step): 获取一个整数范围, 前闭后开 [start, stop)
print( list(range(4)) )  # [0, 1, 2, 3], 范围: [0,4)
# print( list(range(0, 4)) )  # [0, 1, 2, 3], 范围: [0,4)
print( list(range(2, 5)) )  # [2, 3, 4], 范围: [2,5)
print( list(range(1, 9, 2)) )  # [1, 3, 5, 7]
print( list(range(9, 1, -1)) )  # [9, 8, 7, 6, 5, 4, 3, 2]
print( list(range(9, 1, -2)) )  # [9, 7, 5, 3]
# [6,5,4,3,2,1,0]
print( list(range(6, -1, -1)) )

# for-in
# 1+2+3+...+100
s = 0
for i in range(1, 101):
    # print(i, end=' ')
    s += i

print()
print('i:', i)  # i: 100
print('s:', s)  # s: 5050

# 列表
# 列表的简单使用
# 1. 列表定义
ages = [11, 22, 33, 44]

# 2. 索引/下标: 从0开始
print( ages[0] )  # 11
print( ages[1] )  # 22
print( ages[2] )  # 33
print( ages[3] )  # 44
# print( ages[4] )  # 报错
print( ages[-1] )  # 倒数第1个

# for遍历
for n in ages:
    print(n)  # 元素

# for i in range(4):
#     print(i, ages[i])  # 下标,元素

# 列表的长度: 列表中元素的个数
print( len(ages) )
for i in range( len(ages) ):
    print(i, ages[i])  # 下标,元素

# enumerate() : 枚举,列举
for i,n in enumerate(ages):
    print(i, n)  # 下标,元素

# 将 10,9,8,7,6,5,4,3,2,1遍历, range()
for i in range(10, 0, -1):
    print(i, end=' ')
print()

# 将ages倒过来打印每个元素
ages = [11, 22, 33, 44, 55]
for i in range(len(ages)-1, -1, -1):
    print(ages[i], end=' ')
print()


# for循环嵌套
# 1. 输出10行内容，每行的内容都是“*****”, 每次只能输出一颗*。
'''
*****
*****
*****
*****
*****
*****
*****
*****
*****
*****
'''
for i in range(10):  # 10行 i: 0,1,2,3,4,5,6,7,8,9
    # 只考虑其中的一行
    for j in range(5):  # 5列 j:0,1,2,3,4
        print('*', end='')
    print()  # 换行


# 2. 输出10行内容，每行的内容都不一样，第1行一个星号，第2行2个星号，依此类推第10行10个星号。
#   每次只能输出一个星
'''
*
**
***
****
*****
******
*******
********
*********
**********
'''
for i in range(1, 11):  # i:1,2,3,4,5,6,7,8,9,10
    for j in range(i):
        print('*', end='')
    print()


# 打印99乘法表
'''
1*1=1	
1*2=2	2*2=4	
1*3=3	2*3=6	3*3=9	
1*4=4	2*4=8	3*4=12	4*4=16	
1*5=5	2*5=10	3*5=15	4*5=20	5*5=25	
1*6=6	2*6=12	3*6=18	4*6=24	5*6=30	6*6=36	
1*7=7	2*7=14	3*7=21	4*7=28	5*7=35	6*7=42	7*7=49	
1*8=8	2*8=16	3*8=24	4*8=32	5*8=40	6*8=48	7*8=56	8*8=64	
1*9=9	2*9=18	3*9=27	4*9=36	5*9=45	6*9=54	7*9=63	8*9=72	9*9=81	
'''
for i in range(1, 10):  # 行
    for j in range(1, i+1):  # 列
        print(f'{j}*{i}={i*j}', end='\t')
    print()



