
# 项目入口文件
import time

from view import View
from bank import Bank


# 主函数
def main():
    # 欢迎界面
    View.welcome_view()

    # 登录
    r = View.login()
    if not r:
        return

    # 银行主界面
    bank = Bank()

    # 实现功能
    while True:
        View.main_view()

        # 输入对应功能的数字，调用对应的方法
        n = input('请输入对应功能的编号:')
        if n == '1':
            bank.create_user()
        elif n == '2':
            bank.search_money()
        elif n == '3':
            bank.save_money()
        elif n == '4':
            bank.get_money()
        elif n == '5':
            bank.transform_money()

        elif n == '6':
            bank.modify_password()
        elif n == '7':
            bank.lock_card()
        elif n == '8':
            bank.unlock_card()
        elif n == '9':
            bank.makeup_card()
        elif n == '0':
            bank.delete_user()

        elif n == 'q':
            print('=>感谢您的使用，欢迎下次再来!')
            break
        else:
            print('=>输入错误，请重新输入...')

        time.sleep(2)


if __name__ == '__main__':
    main()

