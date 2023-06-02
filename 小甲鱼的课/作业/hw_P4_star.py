temp = input('请输入一个整数：')
guess = int(temp)
while guess:
    print(' ' * (guess - 1) + '*' * guess)
    guess -= 1
# 请输入一个整数：5
#     *****
#    ****
#   ***
#  **
# *
