def discounts(price, rate):
    final_price = price * rate
    # final_price是局部变量，只在定义函数这块里面有用。

    return final_price


old_price = float(input('请输入原价：'))
# 折扣率在(0,1) 8折就是0.8
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price, rate)
print('打折后价格是：', new_price)
print('这里试图打印全局变量old_price的值：', old_price)

# print('这里试图打印局部变量final_price的值：',final_price)
# print不出来的，因为栈被清空。定义函数的变量和主程序里的变量存储空间不同。
# old_price、rate、new_price都是函数外面的，是全局变量
