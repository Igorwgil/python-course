end = 7
nameList = [0] * end

for i in range(end):
    nameList[i] = input('White the name: ')

for i in range(end - 1, -1, -1): 
    print('i', i, '-', nameList[i])