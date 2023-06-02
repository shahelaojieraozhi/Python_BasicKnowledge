
# f-string
name = '渣渣辉'
age = 50
weight = 65.5

print('大家好,我是渣渣辉,今年50岁,体重65.5kg,是兄弟就来砍我!')

print(f'大家好,我是{name},今年{age}岁,体重{weight}kg,是兄弟就来砍我!')

# format()
print('大家好,我是{},今年{}岁,体重{}kg,是兄弟就来砍我!'.format(name, age, weight))
print('大家好,我是{name},今年{age}岁,体重{weight}kg,是兄弟就来砍我!'.format(age=age, name=name, weight=weight))

# 占位符:
#   %d: 整数
#   %f: 小数
#   %s: 字符串
print('大家好,我是%s,今年%d岁,体重%fkg,是兄弟就来砍我!' % (name, age, weight))
print('大家好,我是%s,今年%d岁,体重%.2fkg,是兄弟就来砍我!' % (name, age, weight))





