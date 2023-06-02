
import time

# 时间戳timestamp: 距离1970年1月1日0点的总秒数
# UTC: 国际协调时间, 格林尼治时间
# 北京: 东八区

# 得到当前时间的时间戳
print(time.time())  # 1620870285.1684206
print(1620870285 // (60*60*24*365) + 1970)

# 暂停1.5秒
time.sleep(0.1)
print()


# datetime: date日期  time时间
import datetime

# 1.创建日期对象
d = datetime.datetime.now()  # 当前时间
d = datetime.datetime(2030, 2, 3, 11, 12, 13)  # 指定时间
print(d, type(d))

# 日期的属性
print(d.year, d.month, d.day, d.hour, d.minute, d.second)
print(d.date(), d.time())

# 日期对象 => 日期字符串 : strftime
# 日期字符串 => 日期对象 : strptime
print(d.strftime('%Y-%m-%d %I:%M:%S %p'))
print(d.strftime('%j'))
print(d.strftime('%x %X'))
# print(d.strftime('%Y年%m月%d日%H时%M分%S秒'))  # 报错
print( d.strftime('%Y{}%m{}%d{} %H{}%M{}%S{}') .format('年','月','日','时','分','秒') )

d2 = d.strptime('2030-10-12', '%Y-%m-%d')
print(d2, type(d2))

'''
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00-59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %% %号本身
'''


# 时间戳
# 日期 => 时间戳
print(d.timestamp())  # 1896318733.0
# 时间戳 => 日期
print(d.fromtimestamp(1886318733.0))


# 时间差
dt = datetime.timedelta(days=10, hours=2)
now = datetime.datetime.now()
print(now + dt)
print(now - dt)

d1 = datetime.datetime(2022, 11, 12)
d2 = datetime.datetime(2021, 5, 13)
d3 = d1 - d2
print(d3, type(d3), d3.days)  # timedelta


