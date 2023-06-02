try:
    file = open('eee','r')
except Exception as e:
    print(e)
    response = input('do you want to creat a new file:')
    if response =='y':
        file = open('eee.txt','w')
    else:
        pass
else:
    file.write('sss')
file.close()
