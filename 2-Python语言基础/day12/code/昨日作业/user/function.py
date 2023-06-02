
# 1. 使用快速排序对列表进行降序排序
#     def fn1(l):
def fn1(l):
    if len(l) <= 1:
        return l

    middle = l.pop(len(l)//2)
    left = []
    right = []
    for n in l:
        if n < middle:
            right.append(n)
        else:
            left.append(n)

    return fn1(left) + [middle] + fn1(right)

# 2. 查找列表的元素: 仿照 str.find()
#     找到元素第一次出现的下标并返回, 找不到返回-1
#     def find(l, n):
def find(l, n):
    for i, m in enumerate(l):
        if m == n:
            return i
    return -1


# 3.顺序查询，获取列表中所有与指定元素重复的元素下标
#   def fn4(l, n):
def fn4(l, n):
    # i_list = []
    # for i, m in enumerate(l):
    #     if m == n:
    #         i_list.append(i)
    # return i_list
    return [i for i, m in enumerate(l) if m==n]

