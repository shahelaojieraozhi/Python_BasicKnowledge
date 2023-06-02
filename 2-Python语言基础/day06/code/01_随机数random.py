
import random

# random.choice(): 在指定列表(或其他序列)中随机获取一个元素
girlfriends = ['刘亦菲', '迪丽热巴', '贾玲', '如花', '古力娜扎']
print(random.choice(girlfriends))
print(random.choice(range(10)))

# randint(a, b) : 从[a,b]范围中随机获取一个整数
print(random.randint(2, 4))

# print(random.randrange(2, 4))  # 不包括4
# print(random.randrange(1, 11, 2))

# random.random() : 0~1的随机小数 [0,1)
print(random.random())

# random.uniform(2, 4) : 2~4之间的随机小数
# a + (b-a) * self.random()
#   uniform(2,4) : [2,4)
#   uniform(2,2) : [2,2]
print(random.uniform(2, 4))
# print(random.uniform(2, 2))

# random.shuffle() : 打乱列表的顺序
# x = [1, 2, 3, 4]
# random.shuffle(x)
# print(x)





