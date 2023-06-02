''''''
import os
# 1.显示指定路径下所有视频格式文件, 提示: 视频格式 mp4，avi，rmvb
#   filename.endswith('mp4')
def search_dir(path):
    if not os.path.exists(path):
        return "path路径不存在"

    for file in os.listdir(path):
        abs_path = os.path.join(path, file)
        if os.path.isfile(abs_path):  # 文件
            if file.endswith('mp4') or file.endswith('avi') or file.endswith('rmvb'):
                print(file)
        elif os.path.isdir(abs_path):  # 目录
            search_dir(abs_path)  # 递归

search_dir(r'C:\Users\ijeff\Desktop\Python2103\Python语言\day12\code\昨日作业\dir')

# 2.自定义模块:
# 	a.建立一个包
# 	b.在包的下创建一个排序的模块
# 	 	模块下的功能
# 			1. 使用快速排序对列表进行降序排序
# 			    def fn1(l):
#
# 			2. 查找列表的元素: 仿照 str.find()
# 				找到元素第一次出现的下标并返回, 找不到返回-1
# 				def find(l, n):
#
# 			3.顺序查询，获取列表中所有与指定元素重复的元素下标
#               def fn4(l, n):
#
# 	在另外一个文件中导入上述包中的模块，完成模块中功能的调用
from user import function
print(function.fn1([3, 2, 4, 5, 6]))
print(function.find([2, 3, 3, 3, 4, 3], 30))
print(function.fn4([2, 3, 3, 3, 4, 3], 3))

# 3. 统计文件夹大小 (os.path.getsize()：获取文件大小)
# 提示: 遍历目录
# size = 0
# def dir_size(path):
#     global size
#
#     if not os.path.exists(path):
#         return 'path路径不存在'
#
#     for file in os.listdir(path):
#         abs_path = os.path.join(path, file)
#         if os.path.isfile(abs_path):  # 文件
#             # 获取文件大小
#             file_size = os.path.getsize(abs_path)
#             size += file_size
#         elif os.path.isdir(abs_path):  # 目录
#             dir_size(abs_path)  # 递归
#
#
# dir_size(r'C:\Users\ijeff\Desktop\Python2103\Python语言\第1周')
# print("size:", size)


def dir_size(path):
    if not os.path.exists(path):
        return 'path路径不存在'

    size = 0

    for file in os.listdir(path):
        abs_path = os.path.join(path, file)
        if os.path.isfile(abs_path):  # 文件
            # 获取文件大小
            size += os.path.getsize(abs_path)
        elif os.path.isdir(abs_path):  # 目录
            size += dir_size(abs_path)  # 递归

    return size

size2 = dir_size(r'C:\Users\ijeff\Desktop\Python2103\Python语言\第1周')
print('size:', size2)
