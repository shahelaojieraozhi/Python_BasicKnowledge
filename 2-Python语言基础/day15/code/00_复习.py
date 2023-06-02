''''''
'''
1. __str__ 和 __repr__
    
2. 特殊属性 和 运算符重载（了解）

3. 多态（了解）

4. 限制属性__slots__

5. 单例模式
    __new__() : 创建对象
    __init__() : 初始化属性
    __del__() : 析构函数

6. 异常处理
    try-except
    try:    
        a = 1/0
    except:
        print("报错了")
    
    try:    
        a = 1/0
    except Exception as e:
        print("报错了:", e)
    
    try-except-else
    try-except-finally
    
    自定义异常
    class MyException(Exception):
        pass

    抛出异常
    raise 

    断言 Assert

7. 文件操作
    1.打开文件
        mode='r': 只读，如果文件不存在则报错， encoding='utf-8'
        mode='rb': 只读二进制，如果文件不存在则报错
        mode='w': 清空写，如果文件不存在则创建， encoding='utf-8'
        mode='wb': 清空写二进制，如果文件不存在则创建
        mode='a': 追加写，如果文件不存在则创建， encoding='utf-8'
        mode='ab': 追加写二进制，如果文件不存在则创建

    2.操作文件内容
        读：
            read() : 读取所有内容
            read(10) : 读取接下来的10个字符
            readline() : 读取一行
            readlines() : 读取所有行
        写：
            fp.write()
            fp.flush()
        
    3.关闭文件
        fp.close()
    
8. 复制文件

'''
