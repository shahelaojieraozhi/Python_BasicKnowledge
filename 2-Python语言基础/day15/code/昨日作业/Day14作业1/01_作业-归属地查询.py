
#
# 题目：创建函数， 从文件guishudi.txt中获取数据，输入完整手机号11位，匹配前7位，输出对应的地址和卡类型
#
# 60268|1340475|0431|吉林省长春市|吉林移动大众卡
#   手机号前7位 ：1340475
#

def fn1(phone):
    # 读取文件内容：按行读取
    fp = open('guishudi.txt', 'r', encoding='utf-8')
    l1 = fp.readlines()
    fp.close()

    # print(l1)
    # 拆分字符串
    for s in l1:
        l2 = s.split('|')
        # print(l2)
        if l2[1] == str(phone)[:7]:
            print(l2[-2], l2[-1])

fn1(13404758888)







