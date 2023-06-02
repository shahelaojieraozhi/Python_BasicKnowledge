# i = 0
# string = 'ILoveFishC.com'
# while i < len(string)):
#     print(i)
#     i += 1
#   why stongen?
#   这段代码之所以“效率比较低”是因为每次循环都需要调用一次 len() 函数（我们还没有学到函数的概念，
#   小甲鱼这里为零基础的朋友形象的解释下：就像你打游戏打得正HIGH的时候，老妈让你去买盐......你有两种选择，
#   一次买一包，一天去买五次，或者一次性买五包回来，老妈要就直接给她。）

i = 0
string = 'ILoveFishC.com'
length = len(string)
while i < length:
    print(i)
    i += 1
