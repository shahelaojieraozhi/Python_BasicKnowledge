"""
条件判断语句:
python 没有switch 语句，主要是if
"""

# # 网页登录页面
# username = 'admin'  # 没有登录
# if username != '':
#     print('嘿嘿！我登陆啦！')
#
# print('------------')

username = 'admin'
# python：判断的变量是 '' 、 0 、None 默认是False
# python:如果变量有值'abc','adadw',认为是True
if username:
    print('嘿嘿！我登陆啦！')

print('------------')
# 嘿嘿！我登陆啦！
# ------------

'''
if num :
    print('...........')
等效：
if num!=0:
    print('...........')
'''
