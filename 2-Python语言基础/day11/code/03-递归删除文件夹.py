''''''

# 递归删除文件夹(可能包含子文件或子文件夹)
# 【温馨提示：创建一个文件夹，不要直接操作已有的文件夹】

# 提示：要先将文件夹中的所有子文件删除再删除本文件夹
# remove(): 删除文件
# rmdir()： 删除空目录

import os
def del_dir(path):
    file_list = os.listdir(path)

    # 先遍历path下的所有子文件和子目录,并删除
    for file in file_list:
        abs_path = os.path.join(path, file)

        if os.path.isfile(abs_path):
            # 删除子文件
            os.remove(abs_path)
        elif os.path.isdir(abs_path):
            # 删除子目录
            del_dir(abs_path)  # 递归
            # os.rmdir(abs_path)

    # 删除path路径对应的目录
    os.rmdir(path)

del_dir(r'C:\Users\ijeff\Desktop\Python2103\Python语言\day11\code\newdir2')




