''''''

''' 基础题 '''
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

# 3. 输出9行内容，第1行输出1，第2行输出12，第3行输出123，以此类推，第9行输出123456789。
'''
1
12
123
1234
12345
123456
1234567
12345678
123456789
'''

# 4. 计算10个99相加后的值并输出。(for)

# 5. 计算2的20次方。(要求使用for)

# 6. 计算从1到1000以内所有能被3或者17整除的数的和并输出

# 7. 计算从1到1000以内所有能同时被3，5和7整除的数的和并输出


''' 进阶题 '''
# 1. 给定一个不大于9的数n，打印nn乘法表



''' 挑战题 '''
# 1. 给定一个n位（不超过100）的整数，将该数按位逆置，例如给定12345变成54321，12320变成2321.(*****)
#  n = 12376
# 使用while, 每次对n取个位


# 2. 一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下。求它在第n次落地时，共经过多少米？(*****)
#   规律:
#       第1次落地: 100
#       第2次落地: 100 + 50*2
#       第3次落地: 100 + 50*2 + 25*2
#       第4次落地: 100 + 50*2 + 25*2 + 12.5*2
#       第5次落地: 100 + 50*2 + 25*2 + 12.5*2 + ...


# 3. 已知 abc+cba=1333, 其中的a,b,c均为一位数，编写一个程序，求出a,b,c分别代表什么数字 (*****)
# 穷举法:
#  a: 0~9
#  b: 0~9
#  c: 0~9
