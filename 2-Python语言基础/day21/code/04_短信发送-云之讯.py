
# 短信发送： 收费
#    第三方短信平台
#

# 云之讯
import requests

data = {
    "sid": "7d946861e6b2d74b2db38a442a19fd38",
    "token": "8712938e22c34a179b3cea43ff783b68",
    "appid": "36c083fcfdcf47b5b50d6a94fbb0e50c",
    "templateid": "422930",  # 短信模板id
    "param": "123456",  # 短信验证码
    "mobile": "18566218480",  # 接收验证码的手机号
}

url = 'https://open.ucpaas.com/ol/sms/sendsms'
res = requests.post(url, json=data)
print(res.text)

