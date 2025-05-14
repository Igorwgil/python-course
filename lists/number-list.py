from random import randint

end = 100

numberList = [0] * end

for i in range(end):
    numberList[i] = randint(0, 1001)

for i in range(end):
    print(numberList[i])

print('Numbers')

for i in range(end):
    if numberList[i] % 10 == 0:
        print('i', i,' = ', numberList[i] )
