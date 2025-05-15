try:
    number = int(input('White a number: '))
except:
    print('White a valid value. Just numbers.')

match number:
    case 1:
        print('One')
    case 2:
        print('This is may a fuction')
    case 3:
        print('Result of something')
    case _:
        print('Others cases')



