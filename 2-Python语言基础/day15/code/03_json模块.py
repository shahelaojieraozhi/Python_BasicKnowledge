
import json

# json: 表示数据的一种格式
# xml: 表示数据的一种格式

# json解析(反序列化): json字符串 => json对象(Python字典,列表等)
# json序列化: json对象 => json字符串

# json解析(反序列化): json字符串 => json对象(Python字典,列表等)
json_str = '{"name": "以色列", "place": "中东"}'
# json_obj = eval(json_str)
json_obj = json.loads(json_str)
print(json_obj, type(json_obj))
# {'name': '以色列', 'place': '中东'}  <class 'dict'>

# json序列化: json对象 => json字符串
json_str2 = json.dumps(json_obj)
print(json_str2, type(json_str2))
# {"name": "\u4ee5\u8272\u5217", "place": "\u4e2d\u4e1c"} <class 'str'>




