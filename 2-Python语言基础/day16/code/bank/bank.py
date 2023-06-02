
# 银行系统
#   开户，查询，存款，取款，转账，  改密，锁卡，解锁，补卡，销户

from user import User
from card import Card
import random
import pickle
import os


class Bank:
    def __init__(self):
        # 保存当前银行系统中的所有用户
        self.users = []
        self.file = 'users.txt'

        # 每次启动系统后，需要在最开始就加在文件中的所有用户
        self.__get_users()
        print('=> 系统所有用户:', self.users)

    # 保存用户对象到文件中
    def __save_users(self):
        fp = open(self.file, 'wb')
        pickle.dump(self.users, fp)
        fp.close()

    # 从文件中取出用户对象
    def __get_users(self):
        if os.path.exists(self.file):
            fp = open(self.file, 'rb')
            self.users = pickle.load(fp)
            fp.close()


    # 开户
    def create_user(self):
        # 1.创建卡
        # 卡号
        cardid = self.create_cardid()
        # print('=> 创建卡号成功:', cardid)
        # 卡密码
        passwd = self.create_password()
        # 卡余额
        '''
        # money = input('请您输入要预存的金额:')
        # try:
        #     money = float(money)
        # except:
        #     print('money输入不合法')
        #     money = 0
        '''
        money = float(input('请您输入要预存的金额:'))
        # 创建卡对象
        card = Card(cardid, passwd, money)
        print("=> 创建卡成功:", card)

        # 2.创建用户
        name = input('请输入您的真实姓名:')
        idcard = input('请输入您的身份证号码:')
        phone = input('请输入您的手机号:')
        # 创建用户对象
        user = User(name, idcard, phone, card)
        print('=> 创建用户成功:', user)

        # 3. 将新用户user添加到self.users中
        self.users.append(user)
        self.__save_users()  # 同时存储到文件中

    # 创建卡号：保证唯一性
    def create_cardid(self):
        while True:
            # 产生一个随机的卡号
            cardid = '6666'
            for i in range(4):
                cardid += str(random.randint(0, 9))

            # 判断是否该卡号已存在
            for user in self.users:
                if user.card.cardid == cardid:
                    break
            else:
                return cardid

    # 创建卡密码: 需要确认密码
    def create_password(self):
        while True:
            passwd1 = input('请您输入密码:')
            passwd2 = input('请您再输入一次:')
            # 验证2次密码的一致性
            if passwd1 and passwd1 == passwd2:
                return passwd1
            print('=>2次密码不一致，请您重新输入...')


    # 查询
    def search_money(self):
        pass
        # 1.输入卡号
        user = self.input_cardid()

        # 2.输入密码
        for i in range(3):
            passwd = input('请输入密码:')
            if passwd == user.card.passwd:
                break
            else:
                if 2-i > 0:
                    print(f'=>密码错误，还有{2-i}次机会，请重新输入...')
        else:
            print('=> 密码输错3次，锁卡')
            user.card.islock = True  # 锁卡
            self.__save_users()
            return

        # 3.显示余额
        print('=> 当前余额：', user.card.money)

    # 输入卡号
    def input_cardid(self):
        while True:
            cardid = input('请输入卡号:')
            for user in self.users:
                if user.card.cardid == cardid:
                    return user
            else:
                print("=> 卡号不存在,请重新输入...")

    # 存款
    def save_money(self):
        pass
        # 1.输入卡号
        # 2.输入密码
        # 3.输入存款金额，将user.card.money+=100
        # 4.调用self.__save_users()

    # 取款
    def get_money(self):
        pass
        # 1.输入卡号
        # 2.输入密码
        # 3.输入取款金额，将user.card.money-=100
        # 4.调用self.__save_users()

    # 转账
    def transform_money(self):
        pass
        # 1.输入转出卡号
        # 2.输入转出卡密码
        # 3.输入转入的卡号
        # 4.输入转账金额:
        #       将自己的余额 user.card.money-=100
        #       将对方的余额 user.card.money+=100
        # 5.调用self.__save_users()

    # 改密
    def modify_password(self):
        pass
        # 1.输入卡号
        # 2.输入旧密码
        # 3.输入新密码
        # 4.调用self.__save_users()

    # 锁卡
    def lock_card(self):
        pass

    # 解锁
    def unlock_card(self):
        pass
        # 1.输入卡号
        # 2.输入密码
        # 3.解锁  user.card.islock=False
        # 4.调用self.__save_users()

    # 补卡
    def makeup_card(self):
        pass
        # 1.输入身份证
        # 2.创建新卡对象newcard，将原卡的余额存入， user.card = newcard
        # 3.调用self.__save_users()

    # 销户
    def delete_user(self):
        pass
        # 1.输入身份证
        # 2.删除用户
        # 3.调用self.__save_users()

