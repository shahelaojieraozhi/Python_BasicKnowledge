
# 复制目录（考虑拷贝所有子文件）
import os

def copyPath(sourcePath, targetPath):

    # 判断原目录是否存在
    if not os.path.exists(sourcePath):
        return "目录不存在"

    # 判断目标目录是否存在，如果不存在则创建
    if not os.path.exists(targetPath):
        os.mkdir(targetPath)

    # 提示：
    # 遍历sourcePath下的所有子目录和子文件
    #   1，如果是子文件，则复制文件
    #   2，如果是子目录，在目标目录创建相同的目录名称，递归调用
    #  注意：子文件或子目录的绝对路径


if __name__ == "__main__":
    # 将sourcePath目录的所有内容拷贝到targetPath目录下
    sourcePath = r"../code"
    targetPath = r"../code2"
    copyPath(sourcePath, targetPath)