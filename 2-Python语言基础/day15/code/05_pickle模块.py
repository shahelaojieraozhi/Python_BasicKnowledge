
import pickle

# pickle模块：将Python对象直接存入文件

d = {"name": '巴勒斯坦', 'name2': '以色列'}

# 将字典 存入 文件中
pickle.dump(d, open('e.txt', 'wb'))

# 将文件中的 字典取出
d2 = pickle.load(open('e.txt', 'rb'))
print(d2)

