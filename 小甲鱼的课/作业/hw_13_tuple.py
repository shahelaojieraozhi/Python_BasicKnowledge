#  元组内加element：
temp = ('小甲鱼', '黑夜', '迷途', '小布丁')
# 如果我想在“黑夜”和“迷途”之间插入“怡静”，我们应该：
temp = temp[:2] + ('怡静',) + temp[2:]
print(temp)
# ('小甲鱼', '黑夜', '怡静', '迷途', '小布丁')
