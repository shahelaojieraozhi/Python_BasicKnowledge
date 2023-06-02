import os
import re


""" 需要一点正则表达式知识 ！！！   """

path = "D:\\大一下学期\\课程\\new\\"  # 找到txt所在位置
files = os.listdir(path)  # 得到文件夹下所有txt
i = 0  # 定义变量
for file in files:  # 让txt循环起来
    i += 1  # 用于后续查看完成进度
    position = path + '\\' + file  # 构造绝对路径
    # print(position)
    f1 = open(position, "r", encoding='utf-8')  # 打开并读取文件信息
    data = f1.read()  # 读取信息
    # print(data)
    parrern = "[123456789].*\-[0-9].[0-9]{1}.*.[0-9]{3}.*.[0-9]{3}"  # 用正则匹配所需要的信息
    str2 = re.findall(parrern, data)  # 查找所有符合条件的信息
    # print(str2)
    f2 = open("提取的信息.text", "a+", encoding="utf-8")  # 打开并写入信息
    # print(";".join(str2).replace(";", "\n"))
    f2.write(";".join(str2).replace(";", "\n") + "\n")  # 先转为非数组类型，再用分行输出
    print("完成" + str(i))
    f2.close()  # 有开就有关
    f1.close()  # 有开就有关
