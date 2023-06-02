#   if成立后执行if下面的语句，不成立则跳出下个module
for i in range(1, 10):
    if i % 2 != 0:
        print(i)
        #   对比一下
        # else:
        #     print(2*i)
        continue
    i += 2
    print(i)
