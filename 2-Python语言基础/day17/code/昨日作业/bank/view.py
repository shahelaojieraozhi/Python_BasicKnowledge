
import time

# 界面
class View:

    @classmethod
    def welcome_view(cls):
        print('****************************************')
        print('***********                  ***********')
        print('***********     天地银行      ***********')
        print('***********      V1.0        ***********')
        print('***********                  ***********')
        print('***********     welcome!     ***********')
        print('***********                  ***********')
        print('****************************************')

        time.sleep(0.3)

    # 用户登录
    @classmethod
    def login(cls):
        # 提供模拟用户
        user_dict = {'zhangsan': '123456', 'lisi': '123'}

        # 用户输入用户名和密码
        username = input('请您输入用户名:')
        if username not in user_dict:
            print('=>用户名不存在')
            return

        password = input('请您输入密码:')
        if user_dict[username] != password:
            print('=>密码错误')
            return

        # 登录成功
        print('=>恭喜您！ 登录成功！ 正在进入银行主界面...')
        time.sleep(1)
        return True

    # 银行主界面
    @classmethod
    def main_view(cls):
        # 银行系统
        #   开户，查询，存款，取款，转账，改密，锁卡，解锁，补卡，销户
        print('****************************************')
        print('****                                ****')
        print('****       天地银行的功能主界面        ****')
        print('****        (1)开户   (2)查询        ****')
        print('****        (3)存款   (4)取款        ****')
        print('****        (5)转账   (6)改密        ****')
        print('****        (7)锁卡   (8)解锁        ****')
        print('****        (9)补卡   (0)销户        ****')
        print('****             (q)退出             ****')
        print('****                                ****')
        print('****************************************')
