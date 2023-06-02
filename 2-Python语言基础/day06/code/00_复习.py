''''''
'''
Day01 安装软件

Day02 Python入门
    1. 注释
    2. 输入输出
    3. 变量
    4. 进制转换

Day03 Python运算符和分支语句
    1. 运算符: 
        算术运算符
        比较运算符
        逻辑运算符
        成员运算符
        身份运算符
        赋值运算符
        复合运算: 算术运算符 + 赋值运算符
        位运算符
    2. 分支语句
        if
        if else
        if elif else

Day04 Python循环
    1. while循环
    2. for循环
    3. break continue pass

Day05 列表
    1.基本操作
        1.创建列表
            ages = [1,2,3]
        2.索引
            ages[0], ages[-1]
        3.长度
            len(ages)
        4.遍历
            for n in ages:
            for i in range(len(ages)):
            for i,n in enumerate(ages):
        5.切片
            ages[:] 
            ages[1:4]
            ages[3:]
            ages[:5]
            ages[::-1]
        6.合并
            [1,2] + [3,4]
        7.重复
            [1,2] * 3
        8.成员
            3 in [1,2,3]
        9.删除
            del ages[0]
            del ages[2:4]
            del ages
    2.列表功能
        增删改查
            增: append(n), insert(i, n), extend([1,2,3])
            删: pop(i), remove(n), clear()
            改: ages[0] = 100
            查: ages[0] 或 遍历
        排序:
            sort()  升序
            sort(reverse=True) 降序
            reverse() 倒序
            
            sorted(list)  升序,不改变原列表
            sorted(list, reverse=True) 降序,不改变原列表
            reversed(list) 倒序,不改变原列表
        拷贝:
            copy()  浅拷贝
            copy.deepcopy()  深拷贝
        其他:
            index(n)

    2.数学操作
        sum()
        max()
        min()
        round() 四舍五入
        
        import math
        math.sqrt()
        math.pi
        math.ceil()
        math.floor()
        math.sin()
        math.factorial()  阶乘


'''
import math
n = math.factorial(10)
print(n)





