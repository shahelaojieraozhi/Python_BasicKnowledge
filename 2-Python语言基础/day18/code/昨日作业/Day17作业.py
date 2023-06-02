import re

# 练习
# 匹配中文
chinese_pattern = "[\u4e00-\u9fa5]+"
print(re.search(chinese_pattern, "你好"))

# 提示: 下面要使用完全匹配
# 匹配手机号: 长度11,必须1开头,都是数字
# 匹配qq号： 5-11位, 第一位不能为0
# 匹配任意一个邮箱: 必须包含@,@前是数字字母下户线, @后必须由.
#   如：jack@163.com，11@qq.com, aaa@sina.com.cn
# 匹配身份证: 18位，最后一位可能是X
# 邮政编码(共6位数字, 第一位不能为0)

# 用户名(只能使用数字字母下划线, 且数字不能开头, 长度在6-15位)
pattern = '^[a-zA-Z_]\w{5,14}$'
print(re.search(pattern, 'hello1'))

# 作业
# 简单日期格式 如："2022-11-11"，"2022-1-1"
print(re.search('^\d{4}-\d{1,2}-\d{1,2}$', '2022-11-11'))

# 图片文件格式 如："nbb.jpg", "aa.jpeg","aa.png", "aa.gif"
# 提示: 用|
print(re.search('^\w+\.(jpg|jpeg|png|gif)$', 'aa.jpeg'))

# 匹配网址
# url: https://www.baidu.com:8080/aa/bb?name=lisi&password=123456
#   协议： https://
#   域名： www.baidu.com， 域名对应 IP
#   端口： 8080
#   路径： /aa/bb
#   ? ： 左边是服务器地址，右边是对应的参数
#   参数：name=lisi，&是隔开2个参数的符号

# 1,匹配下列url网址
# http://www.baidu.com
# https://org.baidu.net
# https://www.sina.com.cn
print(re.search('^https?://\w+(\.\w+){2,3}$', 'https://www.sina.com.cn'))

# 2,匹配下列url网址
# https://www.baidu.com/index.html
# https://www.baidu.com:8080/aaa/bbb/index.asp
# https://www.baidu.com:80/ccc/ddd/login.html

print(re.search('^https?://\w+(\.\w+){2,3}(:\d{,5})?(/\w+)+\.\w+$', 'https://www.baidu.com:80/ccc/ddd/login.html'))








