''''''

'''
1. while循环
    一般用于未知循环次数, 死循环的情况
    i = 1
    while i <= 100:
        pass
        i += 1
    
    while True:
        pass

2. for循环
    range(start, stop, step) : 取整数范围 [start, stop)
        range(4): 0,1,2,3
        range(1,5): 1,2,3,4
        range(4,2): 没有整数
        range(1,6,2): 1,3,5
        range(6,1,-1): 6,5,4,3,2
        range(5,-1,-2): 5,3,1 
    
    for循环
        for i in range():
            pass
        for n in ages:
            pass
    
    循环嵌套:
        for i in range():
            for j in range():
                pass
        while :
            while:
    
    for-else
    while-else
    
3.break, continue, pass
    break:
        1.在循环中使用,作用是立刻终止当前这层循环
        2.break之后的语句不执行
        3.break可以和for-else/while-else结合使用
    continue:
        1.在循环中使用,作用是跳过这一次循环
        2.continue之后的语句不执行
    pass:
        空语句,占位
        保证代码的完整性, 防止报错    
    
'''

# print(list(range(4,2)))  # []
# print(list(range(5,-1,-2)))  # [5, 3, 1]



