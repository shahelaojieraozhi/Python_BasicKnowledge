
import os
# os : operating system

# print(os.name)  # nt=>windows
# print(os.environ)  # 环境变量

print(os.getcwd())  # 得到当前路径
# C:\Users\ijeff\Desktop\Python2103\Python语言\day11\code

# print(os.curdir)
# .  当前路径
# .. 表示上一级目录

# 重点掌握
# os.listdir() : 得到指定路径下的所有文件名和文件夹名 所组成的列表
print(os.listdir(r'C:\Users\ijeff\Desktop\Python2103\Python语言\day11\code'))

# os.mkdir() : 创建目录
# os.mkdir('aaa')
# os.makedirs('a/b/c')  # 创建多层目录

# os.rmdir('aaa')  # 删除空目录
# os.remove('aaaaaa.py')  # 删除文件

# os.rename('a', 'a.a')  # 重命名文件或目录

# print( os.stat('01_os模块.py') )  # 文件属性,了解


# os.path
#   path: 本地路径
#   url: 网络路径,网址

# os.path.join() : 拼接路径
# print( os.path.join('aaa', 'bbb', 'ccc') )
print(os.path.join(r'C:\Users\ijeff\Desktop\Python2103\Python语言\day11', 'code'))
# 'C:\Users\ijeff\Desktop\Python2103\Python语言\day11\code'

# os.path.split() : 拆分路径
print(os.path.split(r'C:\Users\ijeff\Desktop\Python2103\Python语言\day11'))
# ('C:\\Users\\ijeff\\Desktop\\Python2103\\Python语言', 'day11')

# os.path.splitext(): 拆分文件名和扩展名
print(os.path.splitext('abc.txt'))
# ('abc', '.txt')

# os.path.abspath() : 得到绝对路径
# 绝对路径: absolute 从盘符开始的完整路径
# 相对路径: relative 相对于当前文件的路径
print(os.path.abspath('01_os模块.py'))

# os.path.getsize() : 获取文件大小
print(os.path.getsize('01_os模块.py'))

# os.path.exists() : 判断文件或目录是否存在
# os.path.isfile() : 判断是否为文件
# os.path.isdir() : 判断是否为目录
print(os.path.exists(r'C:\Users\ijeff\Desktop\Python2103\Python语言\day11\code\newdir'))
print(os.path.isfile(r'C:\Users\ijeff\Desktop\Python2103\Python语言\day11\code\newdir'))
print(os.path.isdir(r'C:\Users\ijeff\Desktop\Python2103\Python语言\day11\code\newdir'))

# print( os.path.dirname('newdir/test1.txt') )  # 父目录, 了解
# print( os.path.basename('newdir/test1.txt') )  # 得到文件名, 了解


