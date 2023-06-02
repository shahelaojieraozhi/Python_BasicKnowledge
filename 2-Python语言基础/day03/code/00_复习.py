''' '''
'''
1.计算机基础介绍
2.Python介绍
3.进制
    a.进制分类: 
        二进制: 0 1
        八进制: 0~7
        十进制: 0~9
        十六进制: 0~9 A~F
    b.单位
        1bit(1位) = 1个0或者1
        1byte(1字节) = 8位
        1KB = 1024B
        1MB = 1024KB
        1GB = 1024MB
        1TB = 1024GB
        ..
    c.进制转换
        二进制 => 十进制:
            例: 1010 => 2^3 + 2 = 10
        十进制 => 二进制:
            倒除法/8421法
            例: 10 => 8+2 => 1010
        二进制 => 八进制:
            例: 10101001 => 10 101 001 => 251
        八进制 => 二进制:
            例: 251 => 10 101 001 => 10101001
        二进制 => 十六进制:
            例: 10101001 => 1010 1001 => A9
        十六进制 => 二进制:
            例: A9 => 1010 1001 => 10101001
        
        其他进制转换: 可以先转换成二进制,再由二进制转换为其他进制
    
4.Python注释
    单行注释: #
    多行注释: """
    
5.输入输出
    input(): 输入
        1. 会暂停,需要在控制台输入内容,然后按回车
        2. 一定会得到字符串,不是整数
        int():转换成整数
        float():转换成小数
        str():转换成字符串
    print(): 输出
        sep=' ' : 分隔符
        end='\n' : 结束符
        
6. 变量
    定义变量:
        a = 10
        a = b = 1
        a,b = 3,4
        a=3; b=4;
        # a=3, b=4  # 不可以,报错
    交换2个变量的值:
        a,b = b,a
    
    变量的命名规范
    
    删除变量
        del a
        
'''


