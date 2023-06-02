## day3 运算符和分支语句 作业

### 选择题

1. `print(100 - 25 * 3 % 4)` 应该输出什么? （  B   ）

   `A. 1`

   `B. 97`

   `C. 25`

   `D. 0`

2. 下列哪种说法是错误的（  A  ）。

   `A. 除字典类型外，所有标准对象均可以用于布尔测试`

   `B. 空字符串的布尔值是False`

   `C. 空列表对象的布尔值是False`

   `D. 值为0的数字的布尔值是False`

4. Python不支持的数据类型有（  A  ）。

   `A. char`

   `B. int`

   `C. float`

   `D. list`

5. （多选）n = 6784，以下能够获取到7 的方法有（   CD   ）。

   `A. n / 1000 % 100 `

   `B. n % 1000 / 100`

   `C. n // 100 % 10`

   `D. n // 10  % 100 // 10`

6. 运行以下程序，当从键盘上输入12,运行结果是（  A   ）。

   ```python
   x = (input())
   print(type(x))
   ```

   A. `<class 'str'>`

   B. `<class 'int'>`

   C. `出错`

   D. `class 'dict'`

7. 下列表达式的运算结果是(   D    ) 。

   ```python
   a = 100
   b = False
   print(a * b > -1)
   ```

   A.  `False`

   B. `1`

   C. `0`

   D.`True`

10. 下列关于print函数用法错误的是（  D   ）
      A. `print(100)`
      B. `print(100, 200)`
      C.` print(100, 'hello world!')`
      D. `print(10 20)`
    
8. 下列表达式的值为True的是（   B   ）。

     A. `3 > 2 > 2`

     B. `1 and 2 != 1`

     C. `not (11 and 0!=1)`

     D. `10 < 20 and 10 < 5`

### 填空题

1. 在Python中表示空类型的是（   NoneType   ）。
2. 查看变量中数据的类型的函数名是（   type  ）。
3. 已知`x = 3 == 3`,执行结束后，变量x的值为（    True    ）。
4. 已知 `x = 3`，那么执行语句 `x += 6` 之后，x的值为（    9    ）。
5. 表达式 `3 ** 2` 的值为（   9   ）,表达式 `3 * 2`的值为（   6   ），表达式 `4 ** 0.5 `的值为（  2  ）。
6. 语句a, b=10,20执⾏后，a的值是(   10   )；
7. 在Python中，布尔类型有（   2  ）个值，分别是（     True 和 False         ）。

### 编程题(可以在Pycharm写好后复制过来)

1. 假设本周的上课时间为156789秒，编程计算本周上课时间是多少天, 多少小时，多少分钟，多少秒；以‘XX天XX时XX分X秒’的方式表示出来。

```python
# 例如: 时间 67 秒  —> 00天 00 时 01 分 07 秒
```

```python
n = 156789
day = n // (60*60*24)
hour = n // (60*60) % 24
minute = n // 60 % 60
second = n % 60
print(f'{day}天{hour}时{minute}分{second}秒')
```

2. 写出判断一个数是否能同时被3和7整除的条件语句, 并且打印对应的结果。

```python
# 例如：输入 21 打印 True, 输入 9 打印 False。
```

```python
n = 21
if n%3==0 and n%7==0:
    print(True)
else:
    print(False)
```

3. 写出判断一个数是否能够被3或者7整除，但是不能同时被3和7整除的条件语句， 并且打印对应的结果。

```python
# 例如：输入 14 打印 True, 输入 4 打印 False, 输入 21 打印 False。
```

```python
n = 33
if (n%3==0 or n%7==0) and n%21!=0:
    print(True)
else:
    print(False)
```

4. 定义两个变量保存一个人的身高和体重，编程实现判断这个人的身材是否正常!

   公式: `体重(kg)/(身高(m)的平方值)` 在18.5 ~ 24.9之间属于正常。

```python
# 例如: 输入体重: 55, 输入身高：1.55, 输出: True
```

```python
height = 1.8
weight = 75
if 18.5 <= weight/(height**2) <= 24.9:
    print(True)
else:
    print(False)
```

### 简答题

1. Python内置数据类型有哪些?

   ```
   int, float, str, bool, NoneType, list, tuple, dict, set, bytes
   ```
   
2. 写出隐式判断bool类型中为False的值有哪些

   ```
   False, 0, "", [], (), {}
   ```

3. 写出你对今日授课内容中有疑问的地方(或者觉得有困难的知识点)。 

   ```
   无
   ```

   

