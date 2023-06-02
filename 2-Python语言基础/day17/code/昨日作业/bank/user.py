
# 用户
#   姓名，身份证号码，手机号，银行卡

class User:
    def __init__(self, name, idcard, phone, card):
        self.name = name
        self.idcard = idcard
        self.phone = phone
        self.card = card

    def __repr__(self):
        return f'姓名:{self.name}, 身份证:{self.idcard}, 手机号:{self.phone}, 卡:{self.card}'

