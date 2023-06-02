# member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
# for each in member:
#     print(each)
# # 小甲鱼
# # 88
# # 黑夜
# # 90
# # 迷途
# # 85
# # 怡静
# # 90
# # 秋舞斜阳
# # 88

# #   方法一：
# member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
# count = 0
# length = len(member)
# while count < length:
#     print(member[count], member[count + 1])
#     count += 2
# # 小甲鱼 88
# # 黑夜 90
# # 迷途 85
# # 怡静 90
# # 秋舞斜阳 88

# # 自己的办法
# member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
# for i in range(0, 9, 2):
#     print(member[i], member[i + 1])
# # 小甲鱼 88
# # 黑夜 90
# # 迷途 85
# # 怡静 90
# # 秋舞斜阳 88


# 第二种方法
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
for each in range(len(member)):
    if each % 2 == 0:
        print(member[each], member[each + 1])
# 小甲鱼 88
# 黑夜 90
# 迷途 85
# 怡静 90
# 秋舞斜阳 88
