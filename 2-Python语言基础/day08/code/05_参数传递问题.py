
#
x = 10
y = {'name': "强东", 'age': 47}

def fn(x2, y2):  # x2=x; y2=y
    x2 += 1
    y2['age'] += 1
    print('x2:', x2)
    print('y2:', y2)

fn(x, y)

print('x:', x)
print('y:', y)

# x2: 11
# y2: {'name': '强东', 'age': 48}
# x: 10
# y: {'name': '强东', 'age': 48}
