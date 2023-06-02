''''''
'''
1. 集合(了解)

2. 占位符
    f''
    .format()
    %s %d %f

3. 字符串
    基本操作:
        1.创建字符串
            s = "hello"
        2.索引
            s[0], s[-1]
        3.长度
            len(s)
        4.遍历
            for c in s:
            for i in range(len(s)):
            for i,c in enumerate(s):
        5.切片
            s[:]
        6.合并
            "a" + "b"
        7.重复
            "s" * 3
        8.成员
            "hello" in "hello world"
        9.删除
            del s
    
    功能:
        计数
            count()
        大小写
            upper()
            lower()
            title()
            capitalize()
            swapcase()
        判断
            isupper()
            islower()
            istitle()
            isspace()
            isalpha()
            isdigit()
            isalnum()
        查找
            find()
            rfind()
            # index()
            # rindex()
        拆分,分隔
            split()
            splitlines()
        合并:
            join()
        替换
            replace(old, new)  # 默认替换所有    
        对齐(了解)
            center(60, '-')
            ljust()
            rjust()
            zfill()
        去除首尾(了解)
            strip()
            lstrip()
            rstrip()
        编码解码
            str.encode() : str => bytes
            bytes.decode() : bytes => str
        ASCII码
            chr(65) : ASCII码 => 字符
            ord('a') : 字符 => ASCII码
        把字符串当成表达式运算:
            eval('1 + 3')
            eval('[1,2,3]')
        转义:
            \  对单个字符转义
            r''  对整个字符串进行转义
        简单加密(了解)
            str.maketrans()
            translate()
        首尾匹配:
            startswith()
            endswith()
'''

# t = str.maketrans('', '')
# "".translate(t)



