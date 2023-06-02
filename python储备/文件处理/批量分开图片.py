import shutil
import os

# 注意：分类后的文件夹不要在原文件里面


def classify(filespath, outpath):
    files = os.listdir(filespath)  # 获取所有的文件
    for x in files:
        srcname = os.path.join(filespath, x)  # srcname = 每个文件的完整路径
        houzhui = x.split("(Flux).")[-1]  # 获取后缀名  houzhui：jpg
        if houzhui == "jpg":
            outfiles = os.path.join(outpath, "(Flux)")  # 要放入的文件夹的路径   outfiles ：.\test\jpg
            if not os.path.exists(outfiles):  # 路径不存在则创建 :(Flux)这个文件夹
                os.mkdir(outfiles)
            filename = outfiles + "\\" + x  # 前面一个斜杠“\”是转义
            print("复制文件---{}到--{}".format(srcname, filename))   # 格式化输出
            shutil.copy(srcname, filename)  # 复制文件


if __name__ == '__main__':
    filespath = r".\Sample"  # 存放文件的文件夹路径
    outpath = r".\test"  # 分类后的文件夹路径
    classify(filespath, outpath)


