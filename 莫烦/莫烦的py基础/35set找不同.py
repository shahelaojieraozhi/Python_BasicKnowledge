char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']
print(set(char_list))
# 输出：{'c', 'a', 'd', 'b'}

# 集合中没有顺序
sentence = 'Welcome Back to This Tutorial'
print(set(sentence))
# 输出：{'l', ' ', 'k', 'i', 'B', 'u', 'o', 's', 'r', 'e', 'c', 'm', 'T', 'h', 't', 'a', 'W'}

# 集合加数
unique_char = set(char_list)
unique_char.add('x')
print(unique_char)
# 输出：
# {'x', 'c', 'b', 'd', 'a'}

# 单独地去掉某个：
unique_char.remove('c')
print(unique_char)
# 输出：{'a', 'b', 'd', 'x'}

# 找set1中set2没有的元素
set1 = unique_char
set2 = {'a', 'e', 'i'}
print(set1.difference(set2))
# 输出：{'d', 'b', 'x'}

# 找set1中与set2交叉的部分（相同的部分）
set1 = unique_char
set2 = {'a', 'e', 'i'}
print(set1.intersection(set2))
# 输出：{'d', 'b', 'x'}

# 清除所有
unique_char.clear()
print(unique_char)
# 输出：set()
