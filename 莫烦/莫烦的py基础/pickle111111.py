import pickle
a_dict = {'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}

# 先保存
file = open('pickle_example.pickle','wb')
pickle.dump(a_dict,file)
file.close()

# 打开
file = open('pickle_example.pickle','rb')
a_dict1 = pickle.load(file)
file.close()
print(a_dict1)
# 输出：
# {'da': 111, 2: [23, 1, 4], '23': {1: 2, 'd': 'sad'}}

# 方便一点的话：
with open('pickle_example.pickle','rb') as file:
    a_dict1 = pickle.load(file)
print(a_dict1)
# 输出：
# {'da': 111, 2: [23, 1, 4], '23': {1: 2, 'd': 'sad'}}
