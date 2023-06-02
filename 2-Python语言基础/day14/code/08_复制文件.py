

# 1、拷贝文件【考虑大文件拷贝，每次读取1024字节拷贝】
def copy_file(path):
    # 原文件名： 07_文件操作.py
    # 副本文件名： 07_文件操作-副本.py
    i = path.rfind('.')
    path2 = path[:i] + '-副本' + path[i:]

    fp1 = open(path, 'rb')
    fp2 = open(path2, 'wb')

    fp2.write(fp1.read())
    fp2.flush()  # 清空缓存

    fp1.close()
    fp2.close()

# copy_file(r'07_文件操作.py')


# 拷贝文件，考虑大文件
def copy_file2(path1, path2):
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


# copy_file2(r'07_文件操作.py', r'07_文件操作-2.py')
p1 = r'C:\Users\ijeff\Desktop\Python2103_video\day14_video\day14_08_异常处理.wmv'
p2 = r'C:\Users\ijeff\Desktop\Python2103_video\day14_video\day14_08_异常处理2.wmv'
copy_file2(p1, p2)

