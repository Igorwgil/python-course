fibonacci_list = [0] * 16

n1 = 1
n2 = 1

print('i - 0 = ', n1)
print('i - 1 = ', n2)

for i in range(2, 16):
    n3 = n1 + n2

    n1 = n2
    n2 = n3

    fibonacci_list[i] =  n3
    print('i -', i, ' = ',fibonacci_list[i])