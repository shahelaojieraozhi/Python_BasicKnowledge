import random
secret = random.randint(1,10)
temp = input("猜数游戏开始了，输入你猜的数：")
# guess=int(temp)
times=1
while temp.isdigit() == 0:
    print("抱歉，输入不合法，", end='')
    temp = input("请输入一个整数：")
guess = int(temp)
while guess != secret and times < 3:
    if guess > secret:       
        print("你猜大了")
    else:
            print("你猜小了")
    temp = input("再猜一次吧，请重新输入你猜的数：")
    guess=int(temp)
    if guess==secret:
        print("你太厉害了")
        print("答案就是：",secret)
    else:
        times=times+1
        if guess > secret:       
            print("你猜大了")
        else:
            print("你猜小了")

print("游戏结束，拜拜")
