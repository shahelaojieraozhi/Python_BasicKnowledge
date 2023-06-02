import time
# time( )函数用于返回当前时间的时间戳(从1970年1月1日00时00分00秒到现在的浮点秒数)
print("当前时间的时间的时间戳：%f" % time.time())
# 当前时间的时间的时间戳：1627041088.881963

# time.localtime( )函数的作用是格式化时间戳为本地时间(struct_time类型）。如果secs参数未传入，就以当前时间为转换标准
print(time.localtime())
# 输出：time.struct_time(tm_year=2021, tm_mon=7, tm_mday=23, tm_hour=19, tm_min=51,
# tm_sec=28, tm_wday=4, tm_yday=204, tm_isdst=0)


for i in range(4):
    print(str(int(time.time()))[-2:])   # 时间戳的整数部分的倒数两位
# sleep(secs)函数用于推迟调用线程的运行，可通过参数secs指定进程挂起的时间
    time.sleep(1)
# 当前时间的时间的时间戳：1627041364.592297
# time.struct_time(tm_year=2021, tm_mon=7, tm_mday=23, tm_hour=19, tm_min=56, tm_sec=4, tm_wday=4,
# tm_yday=204, tm_isdst=0)
# 64
# 65
# 66
# 67

