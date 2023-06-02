import os
import re

"""批量修改文件夹的图片名"""


def ReFileName(dirPath, pattern):
    """
    :param dirPath: 文件夹路径
    :pattern:正则

    :return:
    """
    # 对目录下的文件进行遍历
    i = 1
    for file in os.listdir(dirPath):
        # 判断是否是文件

        if os.path.isfile(os.path.join(dirPath, file)) == True:
            # c= os.path.basename(file)
            newName = re.sub(pattern, str(i) + '.png', file)
            newFilename = file.replace(file, newName)
            # 重命名
            os.rename(os.path.join(dirPath, file), os.path.join(dirPath, newFilename))
            i += 1
    print("图片名已全部修改成功")


if __name__ == '__main__':
    dirPath = r"F:\治\PURE\10-06\10-06"
    pattern = re.compile(r'.*.png')
    ReFileName(dirPath, pattern)

# print(re.sub(r"r[au]ns", "catches", "dog runs to cat"))
# # dog catches to cat

# # 4.compile  分部操作
# complied_re = re.compile(r"r[ua]n")
# # 先把匹配的格式编译出来，再.search(...)
# print(complied_re.search("dog ran to cat"))
# # <re.Match object; span=(4, 7), match='ran'>


# Path1 = 'home'
# Path2 = 'develop'
# Path3 = 'code'
#
# Path10 = Path1 + Path2 + Path3
# Path20 = os.path.join(Path1, Path2, Path3)
# print('Path10 = ', Path10)
# print('Path20 = ', Path20)
#
# # Path10 =  homedevelopcode
# # Path20 =  home\develop\code

# os.listdir()： 列出路径下所有的文件
# os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 ‘.’ 和’…’ 即使它在文件夹中。

# # path – 需要列出的目录路径
# # 返回值 – 返回指定路径下的文件和文件夹列表
# path = "./test"
# dirs = os.listdir(path)
# for file in dirs:
#     print(file)
# 1836.jpg
# 1837.jpg
# 1838.jpg
# ....
