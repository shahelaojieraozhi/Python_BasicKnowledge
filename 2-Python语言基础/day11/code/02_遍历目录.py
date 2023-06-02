
import os

# 遍历目录:第一层
def search_dir(path):
    # 1.先获取path下的所有文件名和文件夹名
    file_list = os.listdir(path)
    # print(file_list)

    # 2.遍历所有文件名和文件夹名
    for file in file_list:
        # 将file的文件名和path拼接: 得到子目录或子文件的绝对路径
        abs_path = os.path.join(path, file)
        # print('abs_path:', abs_path)

        # 判断是文件
        if os.path.isfile(abs_path):
            print('文件:', file)
        # 判断是目录
        elif os.path.isdir(abs_path):
            print('目录:', file)


# search_dir(r'C:\Users\ijeff\Desktop\Python2103\Python语言\day11\code\newdir')


# 遍历目录: 深度遍历
def search_dir2(path):
    # 1.先获取path下的所有文件名和文件夹名
    file_list = os.listdir(path)

    # 2.遍历所有文件名和文件夹名
    for file in file_list:
        # 将file的文件名和path拼接: 得到子目录或子文件的绝对路径
        abs_path = os.path.join(path, file)

        # 判断是文件
        if os.path.isfile(abs_path):
            print('文件:', file)
        # 判断是目录
        elif os.path.isdir(abs_path):
            print('目录:', file)

            # 递归
            search_dir2(abs_path)

search_dir2(r'C:\Users\ijeff\Desktop\Python2103\Python语言\day11\code\newdir')
