
# 字典: dict  dictionary
# key-value 键值对
#   1. 字典的元素是由键值对组成
#   2. key的特点: 1.唯一  2.无序  3.key必须为不可变类型

# 基本操作
# 1.创建字典
d = {'name': '鹿晗', 'movie': '上海堡垒'}
# d2 = {1: 2, 10: 6, False: True, (): []}
# print(d2)

# 2.索引:没有索引,需要使用key
# print(d[0])  # 不能使用索引
# print(d.keys())  # 所有的key
# print(d.values())  # 所有的value
# print(d.items())  # 所有的元素(key:value)

print(d['movie'])
# print(d['movie2'])  # 如果key不存在,则报错

print(d.get('movie'))
print(d.get('movie2'))  # None, 但是不报错
print(d.get('movie2', '长城'))  # 第二个参数是默认值

# 练习: 得到每个主播的名字: nn
douyu = {
    "code": 0,
    "msg": "success",
    "data": {
        "ct": {
            "iv": 1,
            "ivcv": 1,
            "tag": 0,
            "tn": "",
            "vmcrr": 0,
            "vmcm": ""
        },
        "rl": [
            {
                "rid": 3853457,
                "rn": "承蒙厚爱我是小爵啊",
                "uid": 180315123,
                "nn": "一条小爵不可爱茶miya",
                "cid1": 2,
                "cid2": 311,
                "cid3": 1746,
                "iv": 0,
                "av": "avatar_v3/201810/27ffed59b2d817ffb44be8a4a672e702",
                "ol": 1418496,
                "url": "/3853457",
                "c2url": "/directory/game/XX",
                "c2name": "颜值",
                "dot": 2103,
                "subrt": 0,
                "topid": 0,
                "oaid": 0,
                "bid": 0,
                "gldid": 0,
                "rs1": "https://rpic.douyucdn.cn/live-cover/appCovers/2019/08/14/3853457_20190814094651_big.jpg/dy2",
                "rs16": "https://rpic.douyucdn.cn/live-cover/appCovers/2019/08/14/3853457_20190814094651_small.jpg/dy1",
                "utag": [],
                "rpos": 0,
                "rgrpt": 1,
                "rkic": "",
                "rt": 2103,
                "ot": 0,
                "clis": 2,
                "chanid": 0,
                "ioa": 0,
                "od": "",
                "isShowUp": 0,
                "authInfo": None
            },
            {
                "rid": 533813,
                "rn": "感谢翘哥三十级粉丝牌",
                "uid": 36922190,
                "nn": "TD丶正直博",
                "cid1": 2,
                "cid2": 311,
                "cid3": 1746,
                "iv": 0,
                "av": "avatar_v3/202012/815e1c1c652f4d7783034ab9089f75be",
                "ol": 1473191,
                "url": "/533813",
                "c2url": "/directory/game/XX",
                "c2name": "颜值",
                "dot": 1852,
                "subrt": 0,
                "topid": 0,
                "oaid": 0,
                "bid": 0,
                "gldid": 0,
                "rs1": "https://rpic.douyucdn.cn/live-cover/roomCover/2021/01/31/30433e745e15347b71485afbb7049f0f_small.png/dy2",
                "rs16": "https://rpic.douyucdn.cn/live-cover/roomCover/2021/01/31/30433e745e15347b71485afbb7049f0f_big.png/dy1",
                "utag": [],
                "rpos": 0,
                "rgrpt": 1,
                "rkic": "",
                "rt": 1852,
                "ot": 0,
                "clis": 2,
                "chanid": 0,
                "ioa": 1,
                "od": "国内外城市旅行家",
                "isShowUp": 0,
                "authInfo": None
            },
        ],
        "pgcnt": 6
    }
}

rl = douyu['data']['rl']
for d in rl:
    print(d['nn'])


# 3.长度
d = {'name': '鹿晗', 'movie': '上海堡垒'}
print(len(d))

# 4.遍历
for k in d:
    print(k, d[k])
# for k in d.keys():
#     print(k)
# for v in d.values():
#     print(v)
for k,v in d.items():
    print(k, v)

# 5.切片: 不支持
# 6.合并
d1 = {1: 2}
d2 = {3: 4}
d1.update(d2)
print(d1)  # {1: 2, 3: 4}

# 7.重复: 不支持
# print(d1 * 3)

# 8.成员: 判断的是key
print('name' in d)

# 9.删除
# del d['name']
# print(d)


# 字典的功能
# 增删改查
# 增 改
d = {'name': '蔡徐坤', 'like': '篮球'}
d['age'] = 25  # 增
d['like'] = '女'  # 改
print(d)  # {'name': '蔡徐坤', 'like': '女', 'age': 25}

# 删
d.pop("age")  # 弹出指定key对应的元素
# d.popitem()  # 删除最后一项
# d.clear()  # 清空字典
print(d)

# 查: d['name'] 或 d.get('name') 或 遍历


# zip()
d = dict(name='李四', age=44)
# d = {'name': '李四', 'age': 44}

d = dict(zip(('name', 'age'), ('李四', 44)))
print(d)

print( list(zip(('name', 'age'), ('李四', 44))) )
# [('name', '李四'), ('age', 44)]

d = dict( [('name', '李四'), ('age', 44)] )
print(d)




