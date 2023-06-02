
import csv

# 读
def read_csv():
    fp = open('text.csv', 'r', encoding='utf-8')

    # csv读取
    reader = csv.reader(fp)
    print(list(reader))
    # for row in reader:
    #     print(row)

    fp.close()


# 写
def write_csv():
    fp = open('text.csv', 'a', encoding='utf-8', newline='')

    # csv写入
    writer = csv.writer(fp)
    # writer.writerow(['wangwu', '123456', 55, '深圳'])  # 写入一行
    writer.writerows([['wangwu', '123456', 55, '深圳'], ['zhaoliu', '123456', 55, '深圳']])  # 写入多行

    fp.close()


if __name__ == '__main__':
    # read_csv()
    write_csv()

