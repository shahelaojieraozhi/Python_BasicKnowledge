import pandas as pd
import numpy as np
from  datetime  import  *
import time

basestation = r'E:\数学建模\研究生数学建模比赛\2021年研究生数学建模比赛\2021年中国研究生数学建模竞赛赛题 (2)\2021年B题/2019.xlsx'
df = pd.read_excel(basestation)
# print(df)

# print(datetime.today())
# dt = datetime.strptime("2012-09-12 21:08:12", "%Y-%m-%d %H:%M:%S")
# print(dt)
# print(type(dt))
# print(dt.year)
# df = pd.read_excel(r'E:\数学建模\研究生数学建模比赛\2021年研究生数学建模比赛\2021年中国研究生数学建模竞赛赛题 (2)\2021年B题/PY_处理_1.xlsx')
# print(df)
# print(df.dt.month)
# print(df['V1'])
# # 上面的例子取的都是连续的行和列，若取第一行和第四行、第一列和第四列对应的数据，则
#
# df1 = pd.DataFrame({'Joined date': pd.to_datetime(df['V1'])})


# list_of_dates = ['2019-11-20', '2020-01-02', '2020-02-05', '2020-03-10', '2020-04-16']
# employees = ['Hisila', 'Shristi', 'Zeppy', 'Alina', 'Jerry']
# df = pd.DataFrame({'Joined date': pd.to_datetime(list_of_dates)}, index=employees)
#
# df['Year'] = df['Joined date'].dt.year
# df['Month'] = df['Joined date'].dt.month
# print(df)
