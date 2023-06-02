
# 栈: 一种数据结构 , 先进后出,后进先出

# 列表来实现栈
stack = []  # 空栈

stack.append(1)
print(stack)
stack.append(2)
print(stack)
stack.append(3)
print(stack)
stack.append(4)
print(stack)

n = stack.pop()
print(stack, n)
n = stack.pop()
print(stack, n)
n = stack.pop()
print(stack, n)
n = stack.pop()
print(stack, n)
print()


# 队列: 一种数据结构 , 先进先出,后进后出
from collections import deque

# 空队列
queue = deque()
print(queue)

queue.append(1)
print(queue)
queue.append(2)
print(queue)
queue.append(3)
print(queue)
queue.append(4)
print(queue)

n = queue.popleft()
print(queue, n)
n = queue.popleft()
print(queue, n)
n = queue.popleft()
print(queue, n)
n = queue.popleft()
print(queue, n)




