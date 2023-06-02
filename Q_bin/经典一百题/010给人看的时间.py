import time

# time.localtime( )函数的作用是格式化时间戳为本地时间(struct_time类型）。如果secs参数未传入，就以当前时间为转换标准
print(time.localtime())
# 输出：
# time.struct_time(tm_year=2021, tm_mon=7, tm_mday=23, tm_hour=20, tm_min=8, tm_sec=26, tm_wday=4,
# tm_yday=204, tm_isdst=0)


# strftime()
# 方法用于接收时间元组，并返回以可读字符串表示的当地时间。格式由format参数决定。
# strftime()
# 只能接受struct_time类型的参数，若提供的是9位元素的时间元组，则需要将其转化为时间戳再转化为struct_time类型的时间元组
#
# 如果不提供
# t(tupletime)，则默认使用
# localtime()
# 函数返回的当前时间。格式必须是字符串。如果
# tupletime
# 的任何字段在允许的范围之外，那么异常
# ValueError
# 将会被引发。
#
# strftime()
# 方法的语法：
#
# time.strftime(format[, t]  )
# 1、参数
# t - - 这是要被格式化以秒为单位的时间，为一个可选参数。
# 2、参数format - - 这将用于格式化给定时间的指令。
# 3、返回值：返回以可读字符串表示的当地时间


for i in range(4):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(1)
