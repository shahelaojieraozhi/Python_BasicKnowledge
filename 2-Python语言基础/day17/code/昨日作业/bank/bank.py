
# 银行系统
#   开户，查询，存款，取款，转账，  改密，锁卡，解锁，补卡，销户

from user import User
from card import Card
import random
import pickle
import os
from functiontools import save

class Bank:
    def __init__(self):
        # 保存当前银行系统中的所有用户
        self.users = []
        self.file = 'users.txt'

        # 每次启动系统后，需要在最开始就加在文件中的所有用户
        self.__get_users()
        print('=> 系统所有用户:', self.users)

    # 保存用户对象到文件中
    def save_users(self):
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
        self.save_users()  # 同时存储到文件中

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
        ret = self.input_passwd(user)
        if not ret:
            return

        # 3.显示余额
        print('=> 当前余额：', user.card.money)

    # 输入卡号
    def input_cardid(self, tips=''):
        while True:
            cardid = input(f'请输入{tips}卡号:')
            for user in self.users:
                if user.card.cardid == cardid:
                    return user
            else:
                print("=> 卡号不存在,请重新输入...")

    # 输入密码
    def input_passwd(self, user, tips=''):
        for i in range(3):
            passwd = input(f'请输入{tips}密码:')
            if passwd == user.card.passwd:
                return True
            else:
                if 2-i > 0:
                    print(f'=>密码错误，还有{2-i}次机会，请重新输入...')
        else:
            print('=> 密码输错3次，锁卡')
            user.card.islock = True  # 锁卡
            self.save_users()  # 让文件同步修改
            return False

    # 存款
    @save
    def save_money(self):
        pass
        # 1.输入卡号
        user = self.input_cardid()

        # 2.输入密码
        ret = self.input_passwd(user)
        if not ret:
            return

        # 3.输入存款金额，将user.card.money+=100
        money = float(input('请输入存款金额:'))
        user.card.money += money
        print('=>当前余额：', user.card.money)

        # 4.调用self.save_users()

    # 取款
    @save
    def get_money(self):
        pass
        # 1.输入卡号
        user = self.input_cardid()

        # 2.输入密码
        ret = self.input_passwd(user)
        if not ret:
            return

        # 3.输入取款金额，将user.card.money-=100
        while True:
            money = float(input('请输入取款金额:'))
            if user.card.money < money:
                print('=> 余额不足!')
            else:
                user.card.money -= money
                print('=>当前余额：', user.card.money)
                break

        # 4.调用self.save_users()

    # 转账
    @save
    def transform_money(self):
        pass
        # 1.输入转出卡号
        user = self.input_cardid('自己的')

        # 2.输入转出卡密码
        ret = self.input_passwd(user)
        if not ret:
            return

        # 3.输入转入的卡号
        user2 = self.input_cardid('对方的')

        # 4.输入转账金额:
        #       将自己的余额 user.card.money-=100
        #       将对方的余额 user2.card.money+=100
        while True:
            money = float(input('请输入转账金额:'))
            if user.card.money < money:
                print('=> 余额不足!')
            else:
                user.card.money -= money
                user2.card.money += money
                print('=>当前余额：', user.card.money)
                break

        # 5.调用self.save_users()

    # 改密
    @save
    def modify_password(self):
        pass
        # 1.输入卡号
        user = self.input_cardid()

        # 2.输入旧密码
        ret = self.input_passwd(user, tips='旧')
        if not ret:
            return

        # 3.输入新密码
        while True:
            new_passwd = input('请输入新密码:')
            # 新密码和旧密码不能一样
            if new_passwd == user.card.passwd:
                print('=> 新密码不能和旧密码一样! 请重新输入...')
                continue
            user.card.passwd = new_passwd
            print('=> 修改密码成功!')
            break

        # 4.调用self.save_users()

    # 锁卡
    def lock_card(self):
        pass

    # 解锁
    @save
    def unlock_card(self):
        pass
        # 1.输入卡号
        user = self.input_cardid()

        # 2.输入密码
        ret = self.input_passwd(user)
        if not ret:
            return

        # 3.解锁  user.card.islock=False
        user.card.islock = False
        print('=> 解锁成功！')

        # 4.调用self.save_users()

    # 补卡
    @save
    def makeup_card(self):
        pass
        # 1.输入身份证
        user = self.__input_idcard()

        # 2.创建新卡对象newcard，将原卡的余额存入， user.card = newcard
        print('=> 正在创建新卡，请输入新卡信息:')
        cardid = self.create_cardid()  # 新卡号
        passwd = self.create_password()  # 新密码
        money = user.card.money  # 旧卡的余额
        new_card = Card(cardid, passwd, money)
        # 替换旧卡对象
        user.card = new_card
        print('=> 补卡成功！')
        # 3.调用self.save_users()

    # 输入身份证
    def __input_idcard(self):
        while True:
            idcard = input('请输入身份证号码:')
            for user in self.users:
                if user.idcard == idcard:
                    return user
            else:
                print("=> 身份证号码不存在,请重新输入...")

    # 销户
    def delete_user(self):
        pass
        # 1.输入身份证
        user = self.__input_idcard()

        # 2.删除用户
        money = user.card.money
        ret = input(f'当前卡余额{money}, 确定要删除用户吗? (y/n)')
        if ret == 'y' or ret == 'yes':
            self.users.remove(user)
            print('=> 销户成功')
            self.save_users()
        else:
            print('=> 销户失败!')

        # 3.调用self.save_users()

