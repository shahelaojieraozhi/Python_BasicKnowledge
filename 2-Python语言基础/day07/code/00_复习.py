''''''

'''
1. 随机数:
    random.choice()
    random.randint()
    # random.randrange()
    random.random()
    # random.uniform(2, 4)
    # random.shuffle(list)

2. 元组
    基本操作
        1.创建元组  
            t = (1,)
        2.索引
            t[0]
        3.长度
            len(t)
        4.遍历
            for n in t:
            for i in range(len(t)):
            for i,n in enumerate(t):
        5.切片
            t[:]
        6.合并
            (1,2) + (3,4)
        7.重复
            t * 3
        8.成员
            3 in t
        9.删除
            del t
    其他功能:
        增删改: 没有这些功能
        排序: sorted(), reversed()
        count(), index()
    
3. 字典
    特点:
        1.元素都是键值对 key-value
        2.key的特点: 唯一,无序,不可变类型
    基本操作
        1.创建字典
            d = {}
            d = dict(name="张三")
            d = dict(zip(['name','age'], ['鹿晗',31]))
        2.没有索引, 通过key查找
            d['name']
            d.get('name') 
            d.get('name', default)
        3.长度
            len(d)
        4.遍历
            for k in d:
            # for v in d.values():
            for k,v in d.items():
        5.没有切片
        6.合并
            d.update(d2)
        7.没有重复
        8.成员
             key in d
        9.删除
            del d
    其他功能:
        增删改查
        增改: 
            d = {'name': "张三", 'age': 31}
            d['sex'] = '男'
            d['name'] = '李四'
        删:
            d.pop(key)
            # d.popitem()
            # d.clear()
            # del d[key]
'''

