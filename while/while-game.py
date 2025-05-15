import os
from random import randint

def cleam_scream():
    os.system('cls')

option = 's'

while option == 's':
    cleam_scream()

    print('YOU VS COMPUTER!')
    print()

    attempts = 1

    while attempts < 5:
        userNumber = input('Choice a number between 1 and 10: ')
        computerNumber = randint(1, 10)

        if userNumber == computerNumber:
            print('You Win! The number was', computerNumber, '\n\n')
            
        else:
            print('You Lose! The number was', computerNumber, '\n\n')
        
        attempts += 1

    option = input('You have not more attempts\nDo you want keep playing? [s] or [n]')

cleam_scream()
