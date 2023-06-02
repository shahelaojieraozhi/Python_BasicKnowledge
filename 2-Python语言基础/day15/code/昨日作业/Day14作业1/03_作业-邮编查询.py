
#
# 题目： 邮编查询
# 	创建函数， 传入一个邮编，得到归属地
#   提示：eval('[110100,"北京市市辖区"]')

def fn(post_code):
    fp = open('youbian.txt', encoding='utf-8')
    l1 = fp.readlines()
    fp.close()

    for s in l1:
        # print(s)
        l2 = eval(s[:-2])
        # print(l2, type(l2))
        if l2[0] == post_code:
            print(l2[1])

fn(110108)


