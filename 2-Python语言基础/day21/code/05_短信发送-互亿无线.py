import requests

account = "C80604386"
password = "16874f2ed0a2d0bb225747370f9aedc4"
mobile = "18566218480"
text = "您的验证码是：121254。请不要把验证码泄露给其他人。"

data = {
    'account': account,
    'password': password,
    'content': text,
    'mobile': mobile,
    'format': 'json'
}

url = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
res = requests.post(url, data=data)
content = res.text
print(content)

