import re
import os
import glob
import shutil

# str = "sajhaskdhj111sjh111dksd333"
# str1 = str.replace("111", "222")
# print(str1)

# # path – 需要列出的目录路径
# # 返回值 – 返回指定路径下的文件和文件夹列表
# path = "./Sample"
# dirs = os.listdir(path)
# lis = []
# for file in dirs:
#     print(file)
#     lis.append(file)
# print(len(lis))
# # 36.25HZ.241(Colour).jpg
# # 36.25HZ.241(DC).jpg
# # 36.25HZ.241(Flux).jpg
# # .....
#
# # 51


# -*- coding: utf-8 -*-
# 生成文件夹中所有文件的路径到txt


# def listdir(path, list_name):  # 传入存储的list
#     for file in os.listdir(path):
#         file_path = os.path.join(path, file)
#         if os.path.isdir(file_path):
#             listdir(file_path, list_name)
#         else:
#             list_name.append(file_path)
#
#
# list_name = []
# path = './test'  # 文件夹路径
# listdir(path, list_name)
# print(list_name)
#
# with open('./list.txt', 'w') as f:  # 要存入的txt
#     write = ''
#     for i in list_name:
#         write = write + str(i) + '\n'
#     f.write(write)

# import shutil
#
# shutil.move('36.jpg', './test')

# str = "36.25HZ.1(Colour).jpg"
# STR = "36.25HZ.241(DC).jpg"
#
# str1 = str.split("(Colour).")
# STR1 = STR.split("(Colour).")
# print(str1)
# print(STR1)
# # ['36.25HZ.1', 'jpg']
# # ['36.25HZ.241(DC).jpg']


# import shutil
#
# # shutil.copyfile(file1,file2)
# # file1为需要复制的源文件的文件路径,file2为目标文件的文件路径+文件名.
#
# # 如下:将c盘中A文件夹下的0.png复制到D盘中B文件夹下并重命名为1.png:
# # src_file = 'C:\\A\\0.png'
# # dst_file = 'D:\\B\\1.png'
# # shutil.copyfile(src_file, dst_file)
#
# # 操作：
# src_file = r'E:\code\python_code\Kaggle\titanic\test\36.25HZ.241(Colour).jpg'
# dst_file = r'E:\code\python_code\Kaggle\titanic\1.jpg'
# shutil.copyfile(src_file, dst_file)

# 如果不想修改名字可以使用shutil.copy(file,folder) .
# 如下:将src_file中的所有文件复制到dst_file中.

src_file = './Sample'
dst_file = './test'
current_list = glob.glob(os.path.join(src_file, '*'))

for x in current_list:
    shutil.copy(x, dst_file)


# 获取指定目录下的所有图片
# print(glob.glob(r"./Sample/*.jpg"), "\n")
# # 获取上级目录的所有.py文件
# print(glob.glob(r'../*.py'))  # 相对路径
