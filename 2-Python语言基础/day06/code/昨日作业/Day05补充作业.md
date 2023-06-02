## 第5天-补充作业

### 基础题

1. 依次输入两个整数，如果两个数相减的结果为奇数则输出该结果，否则输出提示信息`结果不是奇数`。

```python
a = int(input("输入第1个数:"))
b = int(input("输入第2个数:"))
if (a-b)%2 == 1:
    print(a-b)
else:
    print('结果不是奇数')
```

2. 使用for循环输出 0到100内所有的奇数。

```python
for i in range(1, 101, 2):
    print(i)
```

3. 使用while循环输出0到100内所有的偶数。

```python
i = 0
while i<=100:
    print(i)
    i += 2
```



4. 3000米长的绳子， 每天减一半， 问多少天后这个绳子会小于5米 【不考虑小数】

```python
count = 0
n = 3000
while n >= 5:
    count += 1
    n //= 2
print(count)  # 10次
```

5. 输出1到100中能被3整除 or 个位为3的数

```python
for i in range(1, 101):
    if i%3==0 or i%10==3:
        print(i)
```



### 进阶题

1. 统计100以内个位数是2并且能够被3整除的数的个数。

```python
count = 0
for i in range(101):
    if i%10==2 and i%3==0:
        count += 1
print(count)
```

2. 输入任意一个正整数，求它是几位数。

> **注意**：不允许使用判断字符串长度的方式来求解。

```python
n = 10023123
count = 0
while n:
    count += 1
    n //= 10
print(count)

# n = 10023123
# print(len(str(n)))
```

3. 打印所有的水仙花数。

> **说明**：水仙花数是一个三位数，其各位数字⽴方和等于该数本身。
>
> 例如：153是⽔仙花数，因为 `153 = 1³ + 5³ + 3³ `。

```python
for i in range(100, 1000):
    if (i//100) ** 3 + (i//10%10)**3 + (i%10)**3 == i:
        print(i)
```

4. 写一个程序可以不断的输入数字，如果输入的数字是0，打印`程序结束`后结束该程序。

> **运行效果**：
> 请输入数字: 9
> 请输入数字: 762
> 请输入数字: 18
> 请输入数字: 0
> 程序结束

```python
while True:
    n = input('请输入数字:')
    if n == '0':
        print('程序结束')
        break
```



### 挑战题（选做）

1. 统计101~200中素数的个数，并且输出所有的素数。（素数又叫质数，就是只能被1和它本身整除的数）

```python

for n in range(101, 201):

    # n = 37797
    for i in range(2, n):
        if n%i == 0:
            # print('不是素数,是合数')
            break
    else:
        print(n, '是素数')
        
```

2. 求斐波那契数列中第n个数的值，n是正整数。n值由控制台输入

> **说明**：斐波那契数列是这样的一个数列：1、1、2、3、5、8、13、21、34、.... ，第一个数和第二个数是1，从第三个数开始每个元素是前两个元素相加的和。

```python
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
```

3. 一张纸的厚度大约是0.08mm，对折多少次之后能达到珠穆朗玛峰的高度（8848.13米）？

```python
height = 0.08
count = 0
while height < 8848.13*1000:
    count += 1
    height *= 2
print(count)
```

4. "百马百担"问题：一匹大马能驮3担货，一匹中马能驮2担货，两匹小马能驮1担货，如果用一百匹马驮一百担货，问有大、中、小马各几匹？

> **提示**：穷举法。

```python
for big in range(35):
    for middle in range(51):
        small = 100 - big - middle
        if big*3 + middle*2 + small*0.5 == 100:
            print(big, middle, small)
```

5. 请写出你对今天授课内容最疑惑的地方(或者有困难的知识点)

```

```

