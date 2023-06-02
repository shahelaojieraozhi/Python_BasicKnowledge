import shutil
import os


# 注意：分类后的文件夹不要在原文件里面


def classify(filespath, outpath):
    files = os.listdir(filespath)  # 获取所有的文件
    for x in files:
        srcname = os.path.join(filespath, x)  # 每个文件的完整路径
        houzhui = x.split(".")[-1]  # 获取后缀名
        outfiles = os.path.join(outpath, houzhui)  # 要放入的文件夹的路径
        if not os.path.exists(outfiles):  # 路径不存在则创建
            os.mkdir(outfiles)
        filename = outfiles + "\\" + x
        print("复制文件---{}到--{}".format(srcname, filename))
        shutil.copyfile(srcname, filename)  # 复制文件


if __name__ == '__main__':
    filespath = r"D:\usefulfiles\WeChat Files\wxid_izegysef1q5n22\FileStorage\File\2021-12"  # 存放文件的文件夹路径
    outpath = r"D:\usefulfiles\WeChat Files\wxid_izegysef1q5n22\FileStorage\File\分类"  # 分类后的文件夹路径
    classify(filespath, outpath)
