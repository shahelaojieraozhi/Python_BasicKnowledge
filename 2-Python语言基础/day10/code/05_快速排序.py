''''''
# sort()

# 快速排序
'''
算法原理
                    [7, 8, 9, 6, 5, 4, 3, 2, 1]
    
              [4, 3, 2, 1]       [5]     [7, 8, 9, 6]
              [1] [2] [4, 3]     [5]     [7, 8, 9, 6]
              [1] [2] [][3][4]   [5]     [7, 8, 9, 6]
              [1] [2] [][3][4]   [5]     [7, 8, 6]       [9] []
              [1] [2] [][3][4]   [5]     [7,6] [8] []    [9] []
              [1] [2] [][3][4]   [5]     [][6][7] [8] [] [9] []
'''

def quick_sort(l):
    # 临界值
    if len(l) < 2:
        return l

    # 1. 从列表l中取一个中间数
    middle = l.pop( len(l)//2 )
    # 2. 创建2个列表,left, right
    left = []
    right = []
    for n in l:
        if n < middle:
            left.append(n)
        else:
            right.append(n)
    # print(left, [middle], right)

    # 递归
    return quick_sort(left) + [middle] + quick_sort(right)


ll = [7, 8, 9, 6, 5, 4, 3, 2, 1]
print( quick_sort(ll) )



