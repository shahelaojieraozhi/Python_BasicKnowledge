# 用来写只有满足要求后才能能结束游戏的情形
bingo = '饶治是帅哥'
answer = input('请输入你内心最真实的一句话：')
while True:
    if answer == bingo:
        break
    answer = input('抱歉，错了，请重新输入（只有说出你内心最真实的话才能退出哦！）：')
print('niubi')
