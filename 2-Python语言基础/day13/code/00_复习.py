''''''
'''
1. 模块
    时间模块:
        time
            time.time()
            time.sleep()
        datetime
            日期对象
                d = datetime.datetime.now()    
                d = datetime.datetime(2030,2,3)
                d.year d.month d.day  d.hour d.minute d.second
                d.date()  d.time()
            日期字符串
                d.strftime('%Y-%m-%d %H:%M:%S') : 日期对象 => 字符串
                d.strptime() : 字符串 => 日期对象
            时间戳
                d.timestamp() : 日期对象 => 时间戳
                d.fromtimestamp(12312312) : 时间戳 => 日期对象
            时间差
                dt = datetime.timedelta(days=7)            
                d + dt

    加密模块
        import hashlib
        m = hashlib.md5()
        m.update('123'.encode())
        m.hexdigest()

2. 面向对象
    面向对象和面向过程的区别
    类和对象
    类中: 属性和方法
    属性: 类属性和对象属性
    
'''

