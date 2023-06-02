# 抽到的8个球其中红球个数为x个，黄球为y，绿球为z
for x in range(0, 4):
    for y in range(0, 4):
        for z in range(0, 7):
            if (x + y + z == 8):
                print(x, y, z)
#   range(0,4):是0，1，2，3
#   range(0,7) 和 range(2,7)是一样的


# print('red yellow green')
# for red in range(0, 4):
#     for yellow in range(0, 4):
#         for green in range(2, 7):
#             if red + yellow + green == 8:
#                 # 注意，下边不是字符串拼接，因此不用“+”哦~
#                 print(red, '\t', yellow, ' \t', green)  # 这里有个空格
