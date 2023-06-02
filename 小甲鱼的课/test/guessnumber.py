temp = input("猜数游戏开始了，输入你猜的数：")
guess=int(temp)
while guess != 8:
    temp = input("哎呀！猜错了，请重新输入你猜的数：")
    guess=int(temp)
    answer=8
    if guess==answer:
        print("你太厉害了")
    else:
        if guess > answer:       
            print("你猜大了")
        else:
            print("你猜小了")
print("游戏结束，拜拜")
