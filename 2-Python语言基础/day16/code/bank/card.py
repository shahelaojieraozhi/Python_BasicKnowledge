
# 银行卡
#   卡号，密码，金额，是否锁卡
class Card:
    def __init__(self, cardid, passwd, money, islock=False):
        self.cardid = cardid  # 卡号
        self.passwd = passwd  # 密码
        self.money = money  # 金额
        self.islock = islock  # 是否锁卡，默认不锁

    def __repr__(self):
        return f'<卡号:{self.cardid}, 密码:{self.passwd}, 金额:{self.money}, 锁卡:{self.islock}>'

