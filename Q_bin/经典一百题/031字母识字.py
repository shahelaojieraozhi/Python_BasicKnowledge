# **题目：**请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

weekT = {'h': 'thursday',
         'u': 'tuesday'}
weekS = {'a': 'saturday',
         'u': 'sunday'}
week = {'t': weekT,
        's': weekS,
        'm': 'monday',
        'w': 'wensday',
        'f': 'friday'}
str1 = input('请输入一个字母：')
