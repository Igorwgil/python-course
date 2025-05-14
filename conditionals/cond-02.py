from random import randint
import os 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

userNumber = input('Choice a number: ')

computerNumber = randint(1, 5)

if userNumber == computerNumber:
    print('You win!', computerNumber)
else:
    print('You lose. The number was', computerNumber)

