import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

option = 's'

while option == 's':
    limpar_tela()

    try:
        speed = float(input('What is the speed of the car? '))

        if speed > 80:
            print('You were fined!')
            fine = (speed - 80) * 5
            print('Fine: R$', round(fine, 2))
        else:
            print('you were not fined')
    except ValueError: 
        print('Invalide value. Type a valid value for the speed.')

    print()

    option = input('Continue? [s] or [n] ')

