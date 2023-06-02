
# 1、使用函数递归，分别统计文件夹newdir中文件和文件夹的个数
#    提示：统计当前目录下的文件数量和文件夹数量
#         如果碰到文件，则文件数量+1
#         如果碰到文件夹，则文件夹数量+1，递归调用fn()并传入当前子文件夹目录，
import os

'''
file_count = 0
dir_count = 0

def fn(dir_path):
    global file_count,dir_count

    for file in os.listdir(dir_path):
        abs_path = os.path.join(dir_path, file)
        if os.path.isfile(abs_path):  # 文件
            file_count += 1
        else:  # 目录
            dir_count += 1
            fn(abs_path)
'''
# fn(r'C:\Users\ijeff\Desktop\Python2103\Python语言\day16\code\昨日作业\newdir')
# print(file_count, dir_count)



def fn(dir_path):
    file_count = 0
    dir_count = 0

    for file in os.listdir(dir_path):
        abs_path = os.path.join(dir_path, file)
        if os.path.isfile(abs_path):  # 文件
            file_count += 1
        else:  # 目录
            dir_count += 1
            file_count2, dir_count2 = fn(abs_path)
            file_count += file_count2
            dir_count += dir_count2

    return file_count, dir_count


a, b = fn(r'C:\Users\ijeff\Desktop\Python2103\Python语言\day16\code\昨日作业\newdir')
print(a, b)

