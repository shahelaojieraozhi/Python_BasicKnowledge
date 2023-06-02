
list1 = [1, 2, 3]
def func():
    list1.extend([4, 6, 8, 9])

func()
print(list1)

d = dict([(1,'a'), (2,'b')])
# d = dict((1,'a'), (2,'b'))
print(d)



a = list(filter(lambda x: x%2==0, range(1, 11)))
print(a)

b = list(filter(None,range(10)))
print(b)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


def func(a, b, *args):
    print(a, b, args)

# func(1,2,a=3)
print('*' * 100)

def A(func):
    print('-->1')
    def wrapper(*args,**kwargs):
        func()
        print('-->hello')
    return wrapper


@A  # show = A(show)
def show():
    print('-->python')


