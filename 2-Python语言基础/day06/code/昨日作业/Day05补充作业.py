# count = 0
# n = 3000
# while n >= 5:
#     count += 1
#     n //= 2
# print(count)

c = a = b = 1
n = 1

for i in range(n):
    if i < 2:
        # print(1, end=" ")
        pass
    else:
        c = a + b
        a = b
        b = c
        # print(c, end=' ')

print(c)


height = 0.08
count = 0
while height < 8848.13*1000:
    count += 1
    height *= 2
print(count)

# 百马百担: 一匹大马能驮3担货，一匹中马能驮2担货，两匹小马能驮1担货，
for big in range(35):
    for middle in range(51):
        small = 100 - big - middle
        if big*3 + middle*2 + small*0.5 == 100:
            print(big, middle, small)



