numberList = [0] * 10

number = 5

for i in range(10):
    numberList[i] = number

    number = number + 5

for i in range(10):
    print('i -', i, ' = ', numberList[i])