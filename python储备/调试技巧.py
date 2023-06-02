# def digit_bit(number):
#     bit = 1
#     test = 1
#     divisor = 10
#     while test >= 1:
#         test = number // divisor
#         if test >= 1:
#             bit = bit + 1
#             divisor = divisor * 10
#     return bit
#
#
# def list_number_digit_bit(input_list):
#     result = [digit_bit(i) for i in input_list]
#     return result
#
#
# def lexicon_order(input_list):
#     digit_bit_list = list_number_digit_bit(input_list)
#     max_bit = max(digit_bit_list)
#     alpha = 1 / max_bit
#     dict_of_number = {}
#     for i in input_list:
#         if digit_bit(i) == max_bit:
#             dict_of_number[i] = i
#         else:
#             bit = digit_bit(i)
#             new_digit = (i * 10 ** (max_bit - bit)) - 0.5 * alpha * (max_bit - bit)
#             dict_of_number[new_digit] = i
#     key_of_dict_of_number = list(dict_of_number.keys())
#     key_of_dict_of_number.sort()
#     lexicon_order_number = [dict_of_number[i] for i in key_of_dict_of_number]
#     return lexicon_order_number
#
#
# def find_the_number(n, k):
#     number_list = list(range(1, n + 1))
#     lexicon_order_number = lexicon_order(number_list)
#     result = lexicon_order_number[k - 1]
#     print('The lexicographical order is: ', lexicon_order_number)
#     print('so the ', k, 'th smallest number is:', result)
#     return result
#
#
# # print(lexicon_order(range(130)))
# # exit()
# # find_the_number(n=130, k=5)
# # exit()
#
# for i in range(10):
#     print(i)
#     r = find_the_number(n=13, k=i)
#     print(r)
#     print('-'*100)
#
#
# # python调试技巧————断点操作
# # 断点打到哪程序就执行到那，挂住等你用调试里的操作
# import json
#
#
# def paixu():
#     alist = [3, 2, 5, 4, 9, 6, 7, 8]
#     for i in range(len(alist) - 1):
#         for j in range(len(alist) - 1 - i):
#             if alist[j] > alist[j + 1]:
#                 temp = alist[j]
#                 alist[j] = alist[j + 1]
#                 alist[j + 1] = temp
#     print(alist)


# python调试技巧————断点操作
# 断点打到哪程序就执行到那，挂住等你用调试里的操作
import json


def paixu():
    alist = [3, 2, 5, 4, 9, 6, 7, 8]
    for i in range(len(alist) - 1):
        for j in range(len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp
    print(alist)


if __name__ == '__main__':
    a = 'A'
    print('test')
    paixu()
    b = json.loads('{"test":123}')
    print(b)

# 两个函数：排序是自己写的代码，json.load是别人的包装好的函数
#
# 调试后有个特殊变量（Special Variables）里面有function 和 module；还有一个普通变量

# F7 进入函数内部，碰到函数就进入
# shift+F8 跳出函数 上箭头
# Alt+ shift + F8： 只进入自己的函数，第三方模块写的方法不进入
# F9 当大多个断点时。F9会到下一个断点，如果没有断点则执行至完成
# Alt + F9 移动到光标处
