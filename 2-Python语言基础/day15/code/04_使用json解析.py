
import requests
import json

url = 'https://www.douyu.com/gapi/rknc/directory/yzRec/1'
# 获取url网址的数据
res = requests.get(url)
result = res.text
print(result, type(result))  # str

# json解析 : result
result2 = json.loads(result)
print(result2, type(result2))  # dict

# 取出每个主播的 昵称nn 和 图片路径rs1
rl = result2['data']['rl']
for meinv in rl:
    name = meinv['nn']
    img = meinv['rs1']
    # print(name, img)

    # 下载图片
    res = requests.get(img)
    result = res.content  # 图片二进制数据
    # 将图片二进制数据写入文件
    with open(f'douyu/{name}.png', 'wb') as fp:
        fp.write(result)
        fp.flush()


