# **题目：**两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
# 有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

# **程序分析：**找到条件下不重复的三个对手即可：
list_jia = ['x', 'y', 'z']
a = set(list_jia)
b = set(list_jia)
c = set(list_jia)
# 这样写以后加任何条件，直接往下填就行了
c -= set(['x', 'z'])
a -= set('x')
# print(a)
# print(b)
# print(c)
# # {'y', 'z'}
# # {'y', 'x', 'z'}
# # {'y'}
for i in a:
    for j in b:
        for k in c:
            if len(set((i, j, k))) == 3:
                print('a:%s,b:%s,c:%s' % (i, j, k))
