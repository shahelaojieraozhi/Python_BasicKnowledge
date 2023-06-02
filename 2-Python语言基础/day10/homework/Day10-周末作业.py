''''''

''' 简答题 '''
# 1， Python中的循环有几种:


# 2， Python的数据类型有哪些:


# 3， Python中空类型特殊值是:


# 4， 判断下列赋值方式正确与否（True or False）
'''
    x = y = z = 1           =>
    x=1, y=2                =>
    x, *y, z = 1,2,3,4      =>
    x, y, z = (1,2,3)       =>
'''


# 5, 列举至少5种常用的内置函数,并解释函数的作用：


# 6，判断下面变量名不正确的有哪些：
# ABC, aBC, a-bc, a_bc， _num123, 123num, NUM123, num_123，
# True, false, true1, false0， print, id, __id__, python


# 7，列举列表list中的至少6个函数，且说明每个函数对应的作用


# 8，列举字典dict中的至少3个函数，且说明每个函数对应的作用



''' 编程题 '''
# 1， 将列表中元素去重, 使用至少2种方式



# 2、编写一个函数gcd(x,y) 求最大公约数，编写一个函数lcm(x,y)求最小公倍数。
# 最大公约数
def gcd(x, y):
    pass


# 最小公倍数
def lcm(x, y):
    pass


# 3、使用Python编程实现下面图形打印,n行：
'''
    *
   **
  ***
 ****
*****
'''


# 4、使用Python编程实现下面图形打印,n行：
'''
    *
   ***
  *****
 *******
********* 
'''

'''
    *
   ***
  *****
 *******
********* 
 *******
  *****
   ***
    *
'''

# 5，将字典的key和value置换，
# 如使用字典: d1 = {'a':1,'b':2,'c':3}，
# 置换后生成字典: d2 = {1:'a', 2:'b', 3:'c'}


# 6、使用Python写一个按照下面方式调用都能正常工作的 my_sum() 方法
'''
    print(my_sum(2,3))     输出 5
    print(my_sum(2)(3))    输出 5
'''
# 提示:
#   通过参数数量判断不同的情况
#   1.有1个参数, 嵌套函数
#   2.有2个参数, 返回和


# 7， 封装函数，传入不定数量的数值型参数，返回所有数字的乘积,
# 提示: *args


# 8， 封装一个函数random_color，该函数的返回值为随机十六进制颜色。
# 说明： 十六进制颜色#开头后面接6个十六进制数， 例: #FFFFFF， #000000， #0033CC
# 提示: colors = '0123456789ABCDEF'
#      random模块
colors = '0123456789ABCDEF'



# 9， 封装函数，
# 第一个函数create_persons()，
#   创建并返回包含5个字典(例如:{"name":"xx","age":xx, "faceValue":100})的列表
#      其中name的值：从["张三","李四","王五","赵六","钱七"]依次取
#      其中age的值：10-100之间的随机整数
#      其中faceValue的值：0-100之间的随机整数
# 第二个函数get_old(), 传入第一个函数创建的列表, 找出列表中年龄最大的人，并将其所有信息打印
# 第三个函数sort_facevalue(), 传入第一个函数创建的列表, 根据颜值升序排列，并打印排序后的信息

def create_persons():
    pass


def get_old(persons):
    pass


def sort_facevalue(persons):
    pass


# 调用
persons = create_persons()

get_old(persons)
sort_facevalue(persons)






