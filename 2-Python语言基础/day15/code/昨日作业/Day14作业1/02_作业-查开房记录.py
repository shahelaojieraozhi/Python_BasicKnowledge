
#
# 题目： 开房查询
# 	创建函数，传入一个名字，查找到这哥们所有的开房记录，
#           然后写入到以这哥们名字为名的txt文件中 如：张三.txt
#

def fn(name):
    fp = open('kaifanglist.txt', encoding='utf-8')
    l1 = fp.readlines()
    fp.close()

    fp2 = open(f'{name}.txt', 'a', encoding='utf-8')

    for s in l1:
        if s.startswith(f'{name},'):
            fp2.write(s)

    fp2.close()

fn('孙旸')