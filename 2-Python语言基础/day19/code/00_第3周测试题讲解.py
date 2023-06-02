import os

# os.path.exists()

# d = dict({'a': 1})
d = dict(a=1)
print(d)

print([1,2] + [3])

print(3 == '3')
print(3>2>=2)

print(('3','2') < ('3','4'))
print()

a = [['x','y'], 1, 2]
b = a
c = a.copy()
a.insert(1, 3)  # [['x','y'], 3, 1, 2]
a[0].append(3)  # [['x','y', 3], 3, 1, 2]

print(b)  # [['x', 'y', 3], 3, 1, 2]
print(c)  # [['x', 'y', 3], 1, 2]

s = 'abcdefg'
print('+'.join(list(s)[:3]))
print('+'.join(['a', 'b', 'c']))
# a+b+c

# m = m0 / math.sqrt(1-v**2/c**2)

a, b = b, a
# c=a;a=b;b=c;

# [4,3,2,1]

def f(x, L=[]):
    for i in range(x):
        L.append(i*i)
    print(L)

f(2)  # [0, 1]
f(3, [3,2,1])  # [3,2,1,0,1,4]
f(3)  # [0, 1, 0, 1, 4]


class Student:
    def __init__(self, name, age, sno, cls):
        self.__name = name
        self.__age = age
        self.__sno = sno
        self.__cls = cls

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return f'{self.__name},{self.__age},{self.__sno},{self.__cls}'

class Teacher:
    def __init__(self, stu_list):
        self.stu_list = stu_list

    def add_stu(self, name, age, sno, cls):
        s = Student(name, age, sno, cls)
        self.stu_list.appen(s)

import time
def outer(fn):
    def inner(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print(end - start)
    return inner

@outer
def fn():
    pass


s = 'abc123'
print(s[::-1])

print(''.join(reversed(s)))

l = list(s)
l.reverse()
print(''.join(l))

s2 = ''
for c in s:
    s2 = c + s2
print(s2)

s2 = ''
for i in range(len(s)-1, -1, -1):
    s2 += s[i]
print(s2)

