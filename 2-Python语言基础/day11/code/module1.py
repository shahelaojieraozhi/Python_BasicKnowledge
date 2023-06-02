
print('hello python')

name = "张三"


print('__name__:', __name__)


def test():
    print(name, "逍遥法外")


# 1. 可以当作一个文件运行的入口
# 2. 可以测试当前文件的功能
if __name__ == '__main__':
    print('如果我执行了,则说明你运行了我这个文件')
    test()

