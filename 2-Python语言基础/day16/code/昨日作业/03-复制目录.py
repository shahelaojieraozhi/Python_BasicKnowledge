
# 复制目录（考虑拷贝所有子文件）
import os


def copy_path(source_path, target_path):
    # 判断原目录是否存在
    if not os.path.exists(source_path):
        return "目录不存在"

    # 判断目标目录是否存在，如果不存在则创建
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    # 遍历source_path下的所有子文件和子目录
    for file in os.listdir(source_path):
        src_abs_path = os.path.join(source_path, file)  # 源文件
        tgt_abs_path = os.path.join(target_path, file)  # 目标文件

        # 如果是文件,则拷贝文件
        if os.path.isfile(src_abs_path):
            copy_file(src_abs_path, tgt_abs_path)
        # 如果是目录，则创建目录
        elif os.path.isdir(src_abs_path):
            copy_path(src_abs_path, tgt_abs_path)


    # 提示：
    # 遍历source_path下的所有子目录和子文件
    #   1，如果是子文件，则复制文件
    #   2，如果是子目录，在目标目录创建相同的目录名称，递归调用
    #  注意：子文件或子目录的绝对路径


# 复制文件
def copy_file(path1, path2):
    fp1 = open(path1, 'rb')
    fp2 = open(path2, 'wb')

    while True:
        content = fp1.read(1024)
        if not content:
            # 如果content为空，表示已经读完了
            print('复制完成!')
            break
        fp2.write(content)
        fp2.flush()  # 清空缓存


if __name__ == "__main__":
    # 将source_path目录的所有内容拷贝到target_path目录下
    source_path = r"C:\Users\ijeff\Desktop\Python2103\Python语言\day15"
    target_path = r"C:\Users\ijeff\Desktop\Python2103\Python语言\day15-2"
    copy_path(source_path, target_path)